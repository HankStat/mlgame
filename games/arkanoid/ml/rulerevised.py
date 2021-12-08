# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 12:12:50 2021

@author: User
"""

import random
class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.prev_ball = (93,395)

    def update(self, scene_info):
        """
        Generate the command according to the received `scene_info`.
        """
        # Make the caller to invoke `reset()` for the next round.
        if (scene_info["status"] == "GAME_OVER" or
            scene_info["status"] == "GAME_PASS"):
            return "RESET"
        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
        else:
            x_ball = scene_info["ball"][0]
            y_ball = scene_info["ball"][1]
            x_speed = x_ball-self.prev_ball[0]
            y_speed = y_ball-self.prev_ball[1]
            plat = scene_info["platform"][0]
            dest = 100
            if y_speed != 0:
                slope=x_speed/y_speed
            if y_ball > 320 and y_speed <0:
                dest = x_ball
            # elif y_ball <= 260 and y_speed >0:
            #     dest = x_ball
            elif y_speed > 0 and y_ball > 270 :
                dest=x_ball+(395-y_ball)*slope
                if dest >= 390:
                    dest=dest-390
                elif dest >=195:
                    dest=390-dest
                elif dest <=0 and dest >=-195:
                    dest=dest*(-1)
                elif dest < -195:
                    dest =dest +390
            k=15+random.randint(-2, 2)
            if plat + k <= dest  and dest <= plat+40-k:
                command = "NONE"
            elif plat +k > dest:
                command = "MOVE_LEFT"
            else:
                command = "MOVE_RIGHT"
            self.prev_ball = scene_info["ball"]
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
        self.prev_ball = (93,395)
