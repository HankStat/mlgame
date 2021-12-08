import random
class MLPlay:
    def __init__(self, side):
        """
        Constructor

        @param side A string "1P" or "2P" indicates that the `MLPlay` is used by
               which side.
        """
        self.ball_served = False
        self.side = side
        self.move_plat = False
        self.count=0
        self.final = random.randint(-15,17)
        self.block = 0
        

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] != "GAME_ALIVE":
            print(scene_info["ball_speed"])
            return "RESET"

        if not self.ball_served:
            self.ball_served = True
            command = "SERVE_TO_LEFT"
        else:
            if self.side =="1P":
                judge = False
                side = True
                x_ball = scene_info["ball"][0]
                y_ball = scene_info["ball"][1]
                x_speed = scene_info["ball_speed"][0]
                y_speed = scene_info["ball_speed"][1]
                plat_1 = scene_info["platform_1P"][0]
                if "blocker" in scene_info.keys():
                    block = scene_info["blocker"][0]
                    block_speed = block-self.block
                    judge = True
                    wall = -1
                dest = 100
                if y_speed != 0:
                    slope=x_speed/y_speed
                if y_speed <0 and y_ball >260 and judge:
                    times = (y_ball-260)//abs(y_speed)+1
                    pred = x_ball - (y_ball-260)*slope
                    coll_pred = x_ball + times*x_speed
                    pred_blo = block + (y_ball-260)/abs(y_speed)*block_speed
                    if coll_pred >=195:
                        wall=1
                        if (195-x_ball)%abs(x_speed) ==0:
                            coll_pred = 390-coll_pred
                            pred = 390-pred
                        else:
                            coll_pred = 390-coll_pred + abs(y_speed) - (195-x_ball)%abs(y_speed)
                            pred = 390-pred + abs(y_speed) - (195-x_ball)%abs(y_speed)
                    elif coll_pred < 0:
                        wall = 1
                        if x_ball%abs(x_speed) == 0:
                            coll_pred = coll_pred*(-1)
                            pred = pred*(-1)
                        else:
                            pred = pred*(-1) - (abs(y_speed) - (x_ball)%abs(y_speed))
                            coll_pred = coll_pred*(-1) - (abs(y_speed) - (x_ball)%abs(y_speed))
                    if pred_blo >=170:
                        pred_blo = 340 - pred_blo
                    elif pred_blo <0:
                        pred_blo=pred_blo*(-1)
                    if pred_blo-10  <= pred and pred<= pred_blo + 35:
                        dest = coll_pred + 155*slope*wall
                if y_speed > 0 and y_ball < 236 and judge:
                    times = (235-y_ball)//abs(y_speed)+1
                    while y_ball+times*y_speed <= 260:
                        blo = 1
                        wall=-1
                        #pred = x_ball - (y_ball-260)*slope
                        coll_pred = x_ball + times*x_speed
                        pred_blo = block + times*block_speed
                        if coll_pred >=195:
                            wall=1
                            coll_pred = 390-coll_pred + abs(y_speed) - (195-x_ball)%abs(y_speed)
                            #pred = 390-pred + abs(y_speed) - (195-x_ball)%abs(y_speed)
                        elif coll_pred < 0:
                            wall = 1
                            #pred = pred*(-1) - (abs(y_speed) - (x_ball)%abs(y_speed))
                            coll_pred = coll_pred*(-1) - (abs(y_speed) - (x_ball)%abs(y_speed))
                        if pred_blo >=170:
                            pred_blo = 340 - pred_blo
                            blo = -1
                        elif pred_blo <=0:
                            pred_blo=pred_blo*(-1)
                            blo = -1
                        if pred_blo-5  <= coll_pred and coll_pred<= pred_blo + 30:
                            if wall*x_speed < 0:
                                dest = pred_blo-5+(415-y_ball-times*y_speed)*slope*wall
                            else:
                                dest = pred_blo+30+(415-y_ball-times*y_speed)*slope*wall
                            side = False
                            break
                        times+=1
                    if y_ball+(times-1)*y_speed != 260:
                        x = coll_pred-(260-y_ball-(times-1)*y_speed)/slope*wall
                        pred_blo = pred_blo + block_speed*blo
                        if pred_blo-5  <= x and x <= pred_blo + 30:
                            if wall*x_speed < 0:
                                dest = pred_blo-5+(415-y_ball-times*y_speed)*slope*wall
                            else:
                                dest = pred_blo+30+(415-y_ball-times*y_speed)*slope*wall
                            side = False
                if y_speed > 0 and side:
                    dest=x_ball+(415-y_ball)*slope
                if dest >= 390:
                    dest=dest-390
                elif dest >=195:
                    if (195-x_ball)%abs(x_speed) == 0:
                        dest=390-dest
                    else:
                        dest=390-dest + abs(y_speed) - (195-x_ball)%abs(y_speed)
                elif dest <=0 and dest >=-195:
                    if x_ball%abs(x_speed) == 0:
                        dest=dest*(-1)
                    else:
                        dest=dest*(-1) - (abs(y_speed) - (x_ball)%abs(y_speed))
                elif dest < -195:
                    dest =dest +390
                k=15+random.randint(-2, 2)
                if plat_1 + k <= dest  and dest <= plat_1+40-k:
                    command = "NONE"
                elif plat_1 +k > dest:
                    command = "MOVE_LEFT"
                else:
                    command = "MOVE_RIGHT"
                if judge:
                    self.block = scene_info["blocker"][0]
            else:
                judge = False
                side = True
                x_ball = scene_info["ball"][0]
                y_ball = scene_info["ball"][1]
                x_speed = scene_info["ball_speed"][0]
                y_speed = scene_info["ball_speed"][1]
                plat_2 = scene_info["platform_2P"][0]
                if "blocker" in scene_info.keys():
                    block = scene_info["blocker"][0]
                    block_speed = block-self.block
                    judge = True
                    wall = -1
                dest = 100
                if y_speed != 0:
                    slope=x_speed/y_speed
                if y_speed >0 and y_ball <235 and judge:
                    times = (234-y_ball)//abs(y_speed)+1
                    pred = x_ball + (235-y_ball)*slope
                    coll_pred = x_ball + times*x_speed
                    pred_blo = block + (235-y_ball)/abs(y_speed)*block_speed
                    if coll_pred >=195:
                        wall=1
                        if (195-x_ball)%abs(x_speed) ==0:
                            coll_pred = 390-coll_pred
                            pred = 390- pred
                        else:
                            coll_pred = 390-coll_pred + abs(x_speed) - (195-x_ball)%abs(x_speed)
                            pred = 390-pred + abs(y_speed) - (195-x_ball)%abs(y_speed)
                    elif coll_pred < 0:
                        wall = 1
                        if x_ball%abs(x_speed) == 0:
                             coll_pred = coll_pred*(-1)
                             pred = pred*(-1)
                        else:
                            pred = pred*(-1) - (abs(y_speed) - (x_ball)%abs(y_speed))
                            coll_pred = coll_pred*(-1) - (abs(x_speed) - (x_ball)%abs(x_speed))
                    if pred_blo >=170:
                        pred_blo = 340 - pred_blo
                    elif pred_blo <0:
                        pred_blo=pred_blo*(-1)
                    if pred_blo-10  <= pred and pred<= pred_blo + 35:
                        dest = coll_pred - 155*slope*wall
                if y_speed < 0 and y_ball >260 and judge:
                    times = (y_ball - 261)//abs(y_speed)+1
                    while y_ball+times*y_speed >= 235:
                        blo = 1
                        wall=-1
                        #pred = x_ball - (y_ball-260)*slope
                        coll_pred = x_ball + times*x_speed
                        pred_blo = block + times*block_speed
                        if coll_pred >=195:
                            wall=1
                            coll_pred = 390-coll_pred + abs(y_speed) - (195-x_ball)%abs(y_speed)
                            #pred = 390-pred + abs(y_speed) - (195-x_ball)%abs(y_speed)
                        elif coll_pred < 0:
                            wall = 1
                            #pred = pred*(-1) - (abs(y_speed) - (x_ball)%abs(y_speed))
                            coll_pred = coll_pred*(-1) - (abs(y_speed) - (x_ball)%abs(y_speed))
                        if pred_blo >=170:
                            pred_blo = 340 - pred_blo
                            blo = -1
                        elif pred_blo <=0:
                            pred_blo=pred_blo*(-1)
                            blo = -1
                        if pred_blo-5  <= coll_pred and coll_pred<= pred_blo + 30:
                            if wall*x_speed < 0:
                                dest = pred_blo-5-(y_ball+times*y_speed-80)*slope*wall
                            else:
                                dest = pred_blo+30-(y_ball+times*y_speed-80)*slope*wall
                            side = False
                            break
                        times+=1
                    if y_ball+(times-1)*y_speed != 235:
                        x = coll_pred+(y_ball+(times-1)*y_speed-235)/slope*wall
                        pred_blo = pred_blo + block_speed*blo
                        if pred_blo-5  <= x and x <= pred_blo + 30:
                            if wall*x_speed < 0:
                                dest = pred_blo-5-(y_ball+times*y_speed-80)*slope*wall
                            else:
                                dest = pred_blo+30-(y_ball+times*y_speed-80)*slope*wall
                            side = False
                if y_speed < 0 and side:
                    dest=x_ball+(80-y_ball)*slope
                if dest >= 390:
                    dest=dest-390
                elif dest >=195:
                    if (195-x_ball)%abs(x_speed) == 0:
                        dest=390-dest
                    else:
                        dest=390-dest +  abs(y_speed) - (195-x_ball)%abs(y_speed)
                elif dest <=0 and dest >=-195:
                    if x_ball%abs(x_speed) == 0:
                        dest=dest*(-1)
                    else:
                        dest=dest*(-1) - (abs(y_speed) - (x_ball)%abs(y_speed))
                elif dest < -195:
                    dest =dest +390
                k=15+random.randint(-2, 2)
                if plat_2 + k <= dest  and dest <= plat_2+40-k:
                    command = "NONE"
                elif plat_2 +k > dest:
                    command = "MOVE_LEFT"
                else:
                    command = "MOVE_RIGHT"
                if judge:
                    self.block = scene_info["blocker"][0]
            
        return command

    def reset(self):
        """
        Reset the status
        """
        self.ball_served = False
        self.move_plat = False
        self.count=0
        self.block = 0
        self.final = random.randint(-15,17)