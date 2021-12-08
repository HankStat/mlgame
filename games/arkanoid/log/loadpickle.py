# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 10:43:13 2021

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
    Commands = []
    Platform = []
    for sceneInfo in log["scene_info"]:
         Frames.append(sceneInfo["frame"])
         Balls.append([sceneInfo["ball"][0],sceneInfo["ball"][1]])
         Platform.append(sceneInfo["platform"])
    for i in log["command"]:
        Commands.append(i)
    commands_ary = np.array([Commands])
    commands_ary=commands_ary.reshape((len(Commands),1))
    frame_ary=np.array(Frames)
    frame_ary=frame_ary.reshape((len(Frames),1))
    data = np.hstack((frame_ary, Balls, Platform, commands_ary))
    return data

if  __name__  == '__main__':
    filename = path.join(path.dirname(__file__), 'random_successe4(3).pickle')
    data = getdata(filename)
    for i in range(len(data)):
        print(data[i])
