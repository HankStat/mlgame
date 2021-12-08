"""
The template of the main script of the machine learning process
"""
class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.ball_served = False
        self.prev_ball = (93,395)
        self.brickkk = False
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
            for i in scene_info["bricks"]:
                if i[1] > 320 :
                    self.brickkk = True
                    break
            x_ball = scene_info["ball"][0]
            y_ball = scene_info["ball"][1]
            x_speed = x_ball-self.prev_ball[0]
            y_speed = y_ball-self.prev_ball[1]
            plat = scene_info["platform"][0]
            dest = -1
            if self.brickkk == True and  y_ball >270 :
                #     if plat +20 > x_ball and x_speed < 0:
                #         command = "MOVE_LEFT"
                #     elif plat - 20 < x_ball and x_speed > 0:
                #         command = "MOVE_RIGHT"
                #     else :
                #         command = "NONE"
                # else:
                #     if plat == 80:
                #         command = "NONE"
                #     else :
                #         if plat <80:
                #             command = "MOVE_RIGHT"
                #         else:
                #             command = "MOVE_LEFT"
                    if x_ball <= plat +35 and x_ball>=plat +5:
                        command = "NONE"
                    elif x_ball > plat +35:
                        command = "MOVE_RIGHT"
                    else:
                        command = "MOVE_LEFT"
            elif y_speed > 0 and y_ball > 150 :
                slope = x_speed/y_speed
                dest=(400-y_ball+slope*x_ball)/slope
                if dest >= 390:
                    dest=dest-390
                elif dest >=195:
                    dest=390-dest
                elif dest <=0 and dest >=-195:
                    dest=dest*(-1)
                elif dest < -195:
                    dest =dest +390
                # print(dest)
                if plat +10 <= dest  and dest <= plat+30:
                    command = "NONE"
                elif plat +10 > dest:
                    command = "MOVE_LEFT"
                else:
                    command = "MOVE_RIGHT"
            else :
                if plat == 80:
                    command = "NONE"
                else :
                    if plat <80:
                        command = "MOVE_RIGHT"
                    else:
                        command = "MOVE_LEFT"
            self.prev_ball = scene_info["ball"]
            self.brickkk = False
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
