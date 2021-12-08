# -*- coding: utf-8 -*-
"""
Created on Mon Jun  7 23:59:10 2021

@author: User
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.head_x = 40
        self.head_y = 40
    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] == "GAME_OVER":
            return "RESET"
        body_x = []
        body_y = []
        head_x = scene_info["snake_head"][0]
        head_y = scene_info["snake_head"][1]
        food_x = scene_info["food"][0]
        food_y = scene_info["food"][1]
        x_speed = head_x - self.head_x
        y_speed = head_y - self.head_y
        check = 0
        cannotright = False
        cannotleft = False
        cannotup = False
        cannotdown = False
        for obj in scene_info["snake_body"]:
            if head_x != obj[0] and head_y != obj[1]:
                break
            check+=1
        if check < len(scene_info["snake_body"]):
            for obj in scene_info["snake_body"][check:]:
                body_x.append(obj[0])
                body_y.append(obj[1])
        self.head_x = head_x
        self.head_y = head_y
        if y_speed > 0:
            if body_x != [] and head_x in body_x:
                index = []
                for i in range(len(body_x)):
                    if head_x == body_x[i]:
                        index.append(i)
                for i in range(len(index)):
                    if body_y[index[i]] == head_y + 10:
                        cannotdown = True
            if body_x != [] and head_y in body_y:
                index = []
                for i in range(len(body_y)):
                    if head_y == body_y[i]:
                        index.append(i)
                for i in range(len(index)):
                    if body_x[index[i]] == head_x + 10:
                        cannotright = True
                    if body_x[index[i]] == head_x - 10:
                        cannotleft = True
        if y_speed < 0:
            if body_x != [] and head_x in body_x:
                index = []
                for i in range(len(body_x)):
                    if head_x == body_x[i]:
                        index.append(i)
                for i in range(len(index)):
                    if body_y[index[i]] == head_y - 10:
                        cannotup = True
            if body_x != [] and head_y in body_y:
                index = []
                for i in range(len(body_y)):
                    if head_y == body_y[i]:
                        index.append(i)
                for i in range(len(index)):
                    if body_x[index[i]] == head_x + 10:
                        cannotright = True
                    if body_x[index[i]] == head_x - 10:
                        cannotleft = True
        if x_speed > 0:
            if body_x != [] and head_y in body_y:
                index = []
                for i in range(len(body_y)):
                    if head_y == body_y[i]:
                        index.append(i)
                for i in range(len(index)):
                    if body_x[index[i]] == head_x + 10:
                        cannotright = True
            if body_x != [] and head_x in body_x:
                index = []
                for i in range(len(body_x)):
                    if head_x == body_x[i]:
                        index.append(i)
                for i in range(len(index)):
                    if body_y[index[i]] == head_y + 10:
                        cannotdown = True
                    if body_y[index[i]] == head_y - 10:
                        cannotup = True
        if x_speed < 0:
            if body_x != [] and head_y in body_y:
                index = []
                for i in range(len(body_y)):
                    if head_y == body_y[i]:
                        index.append(i)
                for i in range(len(index)):
                    if body_x[index[i]] == head_x - 10:
                        cannotleft = True
            if body_x != [] and head_x in body_x:
                index = []
                for i in range(len(body_x)):
                    if head_x == body_x[i]:
                        index.append(i)
                for i in range(len(index)):
                    if body_y[index[i]] == head_y + 10:
                        cannotdown = True
                    if body_y[index[i]] == head_y - 10:
                        cannotup = True
        if head_x ==0 :
            if head_y ==0:
                if x_speed < 0:
                    return "DOWN"
                elif y_speed < 0 :
                    return "RIGHT"
            elif head_y ==290:
                if x_speed < 0:
                    return "UP"
                elif y_speed > 0 :
                    return "RIGHT"
            else:
                if x_speed < 0:
                    if cannotdown:
                        return "UP"
                    elif cannotup:
                        return "DOWN"
                    elif head_y < food_y:
                        return "DOWN"
                    else:
                        return "UP"
                elif y_speed != 0:
                    if head_x != food_x and cannotright ==False:
                        return "RIGHT"
                    else:
                        return "NONE"
        elif head_x ==290 :
            if head_y ==0:
                if x_speed > 0:
                    return "DOWN"
                elif y_speed < 0 :
                    return "LEFT"
            elif head_y ==290:
                if x_speed > 0:
                    return "UP"
                elif y_speed > 0 :
                    return "LEFT"
            else:
                if x_speed > 0:
                    if cannotdown:
                        return "UP"
                    elif cannotup:
                        return "DOWN"
                    elif head_y < food_y:
                        return "DOWN"
                    else:
                        return "UP"
                elif y_speed != 0:
                    if head_x != food_x and cannotleft == False:
                        return "LEFT"
                    else:
                        return "NONE"
        elif head_y ==0:
            if y_speed < 0:
                if cannotright:
                    return "LEFT"
                elif cannotleft :
                    return "RIGHT"
                elif head_x < food_x:
                    return "RIGHT"
                else:
                   return "LEFT"
            elif x_speed !=0:
                if head_y != food_y and cannotdown == False:
                    return "DOWN"
                else:
                    return "NONE"
        elif head_y ==290:
            if y_speed > 0:
                if cannotright:
                    return "LEFT"
                elif cannotleft :
                    return "RIGHT"
                elif head_x < food_x:
                    return "RIGHT"
                else:
                    return "LEFT"
            elif x_speed != 0:
                if head_y != food_y and cannotup == False:
                    return "UP"
                else:
                    return "NONE"
        if cannotup and cannotright:
            if y_speed < 0:
                return "LEFT"
            elif x_speed > 0:
                return "DOWN"
        if cannotup and cannotleft:
            if y_speed < 0:
                return "RIGHT"
            elif x_speed < 0:
                return "DOWN"
        if cannotdown and cannotright:
            if y_speed > 0:
                return "LEFT"
            elif x_speed > 0:
                return "UP"
        if cannotdown and cannotleft:
            if y_speed > 0:
                return "RIGHT"
            elif x_speed < 0:
                return "UP"
        if y_speed != 0:
            if cannotdown and  y_speed > 0:
                if abs(head_x -10-body_x[0]) > abs(head_x+10-body_x[0]):
                    return "LEFT"
                else:
                    return "RIGHT"
            if cannotup and y_speed < 0:
                if abs(head_x -10-body_x[0]) > abs(head_x+10-body_x[0]):
                        return "LEFT"
                else:
                    return "RIGHT"
            if cannotleft:
                if food_x > head_x:
                    return "RIGHT"
                else:
                    return "NONE"
            if cannotright:
                if food_x < head_x:
                    return "LEFT"
                else:
                    return "NONE"
            else:
                if head_x > food_x:
                    return "LEFT"
                elif head_x < food_x:
                    return "RIGHT"
                elif head_y > food_y:
                    return "UP"
                elif head_y < food_y:
                    return "DOWN"
        if x_speed !=0:
            if cannotright and x_speed > 0:
                if abs(head_y -10-body_y[0]) > abs(head_y+10-body_y[0]):
                    return "UP"
                else:
                    return "DOWN"
            if cannotleft and x_speed < 0:
                if abs(head_y -10-body_y[0]) > abs(head_y+10-body_y[0]):
                    return "UP"
                else:
                    return "DOWN"
            else:
                if head_x > food_x:
                    return "LEFT"
                elif head_x < food_x:
                    return "RIGHT"
                elif head_y > food_y:
                    if cannotup:
                        return "DOWN"
                    else:
                        return "UP"
                elif head_y < food_y:
                    return "DOWN"

    def reset(self):
        """
        Reset the status if needed
        """
        pass
