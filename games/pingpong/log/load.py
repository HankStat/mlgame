# -*- coding: utf-8 -*-
"""
Created on Fri Apr  9 15:08:35 2021

@author: User
"""

import pickle
from os import path
import numpy as np

def getdata(filename):
    file = open(filename,'rb')
    log = pickle.load(file)
    Frames = []
    Balls = []
    Speeds = []
    Commands_1 = []
    Commands_2 = []
    Platform_1 = []
    Platform_2 = []
    Block = []
    for sceneInfo in log["scene_info"]:
        Frames.append(sceneInfo["frame"])
        Balls.append([sceneInfo["ball"][0],sceneInfo["ball"][1]])
        Speeds.append([sceneInfo["ball_speed"][0],sceneInfo["ball_speed"][1]])
        Platform_1.append([sceneInfo["platform_1P"][0]])
        Platform_2.append([sceneInfo["platform_2P"][0]])
        Block.append([sceneInfo["blocker"][0]])
       
    
    for i in log["command"]:
        if i == log["command"][-1]:
            i = ['over','over']
        Commands_1.append(i[0])
        Commands_2.append(i[1])
    commands1_ary = np.array([Commands_1])
    commands2_ary = np.array([Commands_2])
    commands1_ary=commands1_ary.reshape((len(Commands_1),1))
    commands2_ary=commands2_ary.reshape((len(Commands_2),1))
    frame_ary=np.array(Frames)
    frame_ary=frame_ary.reshape((len(Frames),1))
    data = np.hstack((frame_ary, Balls,Speeds, Block, Platform_1, Platform_2,commands1_ary, commands2_ary))
    return data

if  __name__  == '__main__':
    filename = path.join(path.dirname(__file__), 'dec(2).pickle')
    data = getdata(filename)
    for i in range(len(data)):
        print(data[i])
