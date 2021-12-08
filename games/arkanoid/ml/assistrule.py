# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 08:57:48 2021

@author: User
"""
import random
class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.last_x = 0
        self.last_y = 0
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
            nx = scene_info["ball"][0]
            ny = scene_info["ball"][1]
            plat_x = scene_info["platform"][0]
            lx = self.last_x
            ly = self.last_y
            if (ly-ny) !=0:
                n = (lx *(400-ny)-nx*(400-ny))/(ly-ny)
                px = self.adjust(n)+random.randint(-8, 8)
                if abs(px-(plat_x+20)) <0:
                    command = "NONE"
                elif px >plat_x+20:
                    command = "MOVE_RIGHT"
                else:
                    command = "MOVE_LEFT"
            self.last_x = nx
            self.last_y = ny
        return command

    def adjust(self, n):
        while n<0 or n>195:
            if n<0:
                n*=-1
            else:
                n=190-n
        return n

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False