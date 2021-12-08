# -*- coding: utf-8 -*-
"""
Created on Tue May 18 23:31:07 2021

@author: User
"""

import pickle
from os import path
import numpy as np

def getdata(filename):
    file = open(filename,'rb')
    log = pickle.load(file)
    Frames = []
    Head = []
    Food = []
    Body = []
    for sceneInfo in log["scene_info"]:
        Frames.append(sceneInfo["frame"])
        Head.append([sceneInfo["snake_head"][0],sceneInfo["snake_head"][1]])
        Food.append([sceneInfo["food"][0],sceneInfo["food"][1]])
        k = sceneInfo["snake_body"]
        a = []
        for obj in k:
            a.append(obj[0])
        Body.append(a)
        print(Body)
    frame_ary=np.array(Frames)
    frame_ary=frame_ary.reshape((len(Frames),1))
    data = np.hstack((frame_ary, Head,Food,Body))
    # print(k)
    return data

if  __name__  == '__main__':
    filename = path.join(path.dirname(__file__), 'ml_2021-05-18_23-30-46.pickle')
    data = getdata(filename)
    for i in range(len(data)):
        print(data[i])