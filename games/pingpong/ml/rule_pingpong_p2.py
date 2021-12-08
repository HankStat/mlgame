# -*- coding: utf-8 -*-
"""
Created on Thu Apr  8 16:17:29 2021

@author: User
"""

import random
class MLPlay:
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = "2P"
        self.move_plat = False
        self.count=0
        self.final = random.randint(-15,17)

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            return "RESET"

        if not self.ball_served:
            if not self.move_plat:
                if self.count< abs(self.final):
                    if self.final < 0:
                        command = "MOVE_LEFT"
                    else:
                        command = "MOVE_RIGHT"
                    self.count+=1
                else:
                    self.move_plat=True
            if self.move_plat:
                self.ball_served = True
                k= random.randint(0, 1)
                if k==0:
                    command = "SERVE_TO_LEFT"
                else:
                    command = "SERVE_TO_RIGHT"
        else:
            x_ball = scene_info["ball"][0]
            y_ball = scene_info["ball"][1]
            x_speed = scene_info["ball_speed"][0]
            y_speed = scene_info["ball_speed"][1]
            plat_2 = scene_info["platform_2P"][0]
            dest = 100
            if y_speed != 0:
                slope=x_speed/y_speed
            if y_speed < 0 :
                dest=x_ball+(80-y_ball)*slope
                if dest >= 390:
                    dest=dest-390
                elif dest >=195:
                    dest=390-dest
                elif dest <=0 and dest >=-195:
                    dest=dest*(-1)
                elif dest < -195:
                    dest =dest +390
            k=15+random.randint(-2, 2)
            if plat_2 + k <= dest  and dest <= plat_2+40-k:
                command = "NONE"
            elif plat_2 +k > dest:
                command = "MOVE_LEFT"
            else:
                command = "MOVE_RIGHT"
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
        self.move_plat = False
        self.count=0
        self.final = random.randint(-15,17)