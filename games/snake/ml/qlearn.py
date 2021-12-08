# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 23:24:08 2021

@author: User
"""
import pickle
import numpy as np
epoch_rewards = []
EPOCHS = 3
LOSE_PENALTY = 601
EAT_REWARD = 60
MOVE_PENALTY = 1
EPS = 1
EPS_DECAY = 0.9997
SHOW_WHEN = 2000
STEPS = 220
LEARNING_RATE = 0.8
DISCOUNT = 0.99
q_table = {}
for x in range(-29, 30):
    for y in range(-29, 30):
        for left in range(2):
            for right in range(2):
                for up in range(2):
                    for down in range(2):
                        for direction in range(4):
                            q_table[(x, y), left, right, up, down, direction] = np.zeros(4) 

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.head_x = 40
        self.head_y = 40
        self.body = []
        self.food_x = 40
        self.food_y = 40
        self.command = 1
        self.game = 1
    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """
        if scene_info["status"] == "GAME_OVER":
            self.game = 0
            return "RESET"
        
        head_x = scene_info["snake_head"][0]
        head_y = scene_info["snake_head"][1]
        food_x = scene_info["food"][0]
        food_y = scene_info["food"][1]
        x_speed = head_x - self.head_x
        y_speed = head_y - self.head_y
        for obj in scene_info["snake_body"]:
            self.body.append(obj)
        self.head_x = head_x
        self.head_y = head_y
        self.food_x = food_x
        self.food_y = food_y
        if y_speed < 0:
            self.command = 0
        if y_speed > 0:
            self.command = 1
        if x_speed < 0:
            self.command = 2
        if x_speed > 0:
            self.command = 3
    def act(self,k):
        if k==0:
            return "UP"
        if k==1:
            return "DOWN"
        if k==2:
            return "LEFT"
        if k==3:
            return "RIGHT"

    def reset(self):
        """
        Reset the status if needed
        """
        self.head_x = 40
        self.head_y = 40
        self.body = []
        self.food_x = 40
        self.food_y = 40
        self.command = 1
        self.game = 1
# FPS = 30
# SCALING = SW // SIZE
# starting_q_table = None

for epoch in range(EPOCHS + 2):
    snake = MLPlay()
    totalrewards = 0
    for i in range(1000):
        left = 0
        right = 0
        up = 0
        down = 0
        for part in snake.body:

            if part == (snake.head_x - 10, snake.head_y):                       #x-1说明向左移动了
                left = 1
            if part == (snake.head_x + 10, snake.head_y):
                right = 1
            if part == (snake.head_x , snake.head_y - 10):
                up = 1
            if part == (snake.head_x , snake.head_y + 10):
                down = 1

        obs = ((snake.head_x//10 - snake.food_x//10, snake.head_y//10 - snake.food_y//10), left, right, up, down, snake.command)  #当前移动位置的索引
        if np.random.random() > EPS:
            action = np.argmax(q_table[obs])                 #返回最大索引

        else:
            action = np.random.randint(0, 4)

        # snake.act(action)
        if snake.head_x == snake.food_x and snake.head_y == snake.food_y:
            reward = EAT_REWARD

        else:
            reward = 0
            if snake.game == 0:
                reward = -LOSE_PENALTY
                suicides += 1

                break

            if reward == 0:
                reward = -MOVE_PENALTY
        new_observation = ((snake.head_x//10 - snake.food_x//10, snake.head_y//10 - snake.food_y//10), left, right, up, down, snake.command)
        max_future_q = np.max(q_table[new_observation])
        current_q = q_table[obs][action]
        if reward == EAT_REWARD:
            new_q = EAT_REWARD

        else:
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)
        q_table[obs][action] = new_q
        # pg.event.get()

        totalrewards += reward
        if reward == -LOSE_PENALTY:
            break



    # if current_mean > best_mean:
    #     best_q_table = q_table
    #     best_mean = current_mean

    epoch_rewards.append(totalrewards)
    EPS *= EPS_DECAY
