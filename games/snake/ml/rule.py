# -*- coding: utf-8 -*-
"""
Created on Sun Jun 20 10:28:14 2021

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
        body = []
        head_x = scene_info["snake_head"][0]
        head_y = scene_info["snake_head"][1]
        food_x = scene_info["food"][0]
        food_y = scene_info["food"][1]
        x_speed = head_x - self.head_x
        y_speed = head_y - self.head_y
        cannotright = False
        cannotleft = False
        cannotup = False
        cannotdown = False
        check = 0
        for obj in scene_info["snake_body"]:
            if head_x != obj[0] and head_y != obj[1]:
                break
            check+=1
        if check >= len(scene_info["snake_body"]):
            check = 0
        for obj in scene_info["snake_body"]:
            body.append((obj[0],obj[1]))
        self.head_x = head_x
        self.head_y = head_y
        for bo in body:
            if bo[0]==head_x and bo[1] == head_y + 10:
                cannotdown = True
            if bo[0]==head_x and bo[1] == head_y - 10:
                cannotup = True
            if bo[0]==head_x +10 and bo[1] == head_y:
                cannotright = True
            if bo[0]==head_x - 10 and bo[1] == head_y:
                cannotleft = True
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
                    if head_x == food_x or cannotright ==True:
                        return "NONE"
                    else:
                        return "RIGHT"
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
                    if head_x == food_x or cannotleft == True:
                        return "NONE"
                    else:
                        return "LEFT"
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
                if head_y == food_y or cannotdown == True:
                    return "NONE"
                else:
                    return "DOWN"
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
                if head_y == food_y or cannotup == True:
                    return "NONE"
                else:
                    return "UP"
        if y_speed > 0:
            if cannotdown and cannotright:
                return "LEFT"
            elif  cannotdown and cannotleft:
                return "RIGHT"
            elif cannotdown:
                if abs(head_x -10-body[check][0]) > abs(head_x+10-body[check][0]):
                    return "LEFT"
                else:
                    return "RIGHT"
            elif cannotleft:
                if food_x > head_x:
                    return "RIGHT"
                else:
                    return "NONE"
            elif cannotright:
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
        if y_speed < 0:
            if cannotup and cannotright:
                return "LEFT"
            elif  cannotup and cannotleft:
                return "RIGHT"
            elif cannotup:
                if abs(head_x -10-body[check][0]) > abs(head_x+10-body[check][0]):
                    return "LEFT"
                else:
                    return "RIGHT"
            elif cannotleft:
                if food_x > head_x:
                    return "RIGHT"
                else:
                    return "NONE"
            elif cannotright:
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
        if x_speed > 0:
            if cannotup and cannotright:
                return "DOWN"
            elif  cannotdown and cannotright:
                return "UP"
            elif cannotright:
                if abs(head_y -10-body[check][1]) > abs(head_y+10-body[check][1]):
                    return "UP"
                else:
                    return "DOWN"
            elif cannotup:
                if food_x == head_x:
                    return "DOWN"
                else:
                    return "NONE"
            elif cannotdown:
                if food_x == head_x:
                    return "UP"
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
        if x_speed < 0:
            if cannotup and cannotleft:
                return "DOWN"
            elif  cannotdown and cannotleft:
                return "UP"
            elif cannotleft:
                if abs(head_y -10-body[check][1]) > abs(head_y+10-body[check][1]):
                    return "UP"
                else:
                    return "DOWN"
            elif cannotup:
                if food_x == head_x:
                    return "DOWN"
                else:
                    return "NONE"
            elif cannotdown:
                if food_x == head_x:
                    return "UP"
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

    def reset(self):
        """
        Reset the status if needed
        """
        pass
