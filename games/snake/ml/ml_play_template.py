"""
The template of the script for playing the game in the ml mode
"""

class MLPlay:
    def __init__(self):
        """
        Constructor
        """
        self.state = 2
        pass

    def update(self, scene_info):
        """
        Generate the command according to the received scene information
        """

        command = self.state
        snake_head = scene_info["snake_head"]
        food = scene_info["food"]
        snake_body = scene_info["snake_body"]
        tail_index = len(snake_body) - 1
        actions = [0, 1, 2, 3]
        actions_2 = [0, 1, 2, 3]
        if self.state == 1:
            actions.remove(0)
            actions_2.remove(0)
            if snake_body[tail_index][1] > snake_head[1]:
                if snake_body[tail_index][0] > snake_head[0]:
                    actions.remove(3)
                else:
                    actions.remove(2)
        if self.state == 0:
            actions.remove(1)
            actions_2.remove(1)
            if snake_body[tail_index][1] < snake_head[1]:
                if snake_body[tail_index][0] > snake_head[0]:
                    actions.remove(3)
                else:
                    actions.remove(2)
        if self.state == 3:
            actions.remove(2)
            actions_2.remove(2)
            if snake_body[tail_index][0] > snake_head[0]:
                if snake_body[tail_index][1] > snake_head[1]:
                    actions.remove(1)
                else:
                    actions.remove(0)
        if self.state == 2:
            actions.remove(3)
            actions_2.remove(3)
            if snake_body[tail_index][0] < snake_head[0]:
                if snake_body[tail_index][1] > snake_head[1]:
                    actions.remove(1)
                else:
                    actions.remove(0)
        if 0 in actions_2:
            if (snake_head[0], snake_head[1] - 10) in snake_body or snake_head[1] - 10 < 0:
                if 0 in actions:
                    actions.remove(0)
                actions_2.remove(0)
        if 1 in actions_2:
            if (snake_head[0], snake_head[1] + 10) in snake_body or snake_head[1] + 10 >= 300:
                if 1 in actions:
                    actions.remove(1)
                actions_2.remove(1)
        if 2 in actions_2:
            if (snake_head[0] - 10, snake_head[1]) in snake_body or snake_head[0] - 10 < 0:
                if 2 in actions:
                    actions.remove(2)
                actions_2.remove(2)
        if 3 in actions_2:
            if (snake_head[0] + 10, snake_head[1]) in snake_body or snake_head[0] + 10 >= 300:
                if 3 in actions:
                    actions.remove(3)
                actions_2.remove(3)

        if len(actions) == 0:
            actions = actions_2 if len(actions_2) != 0 else [4]

        if snake_head[0] > food[0]:
            if 2 in actions:
                command = 2
            elif self.state in actions:
                command = self.state
            else:
                command = actions[0]
        elif snake_head[0] < food[0]:
            if 3 in actions:
                command = 3
            elif self.state in actions:
                command = self.state
            else:
                command = actions[0]
        elif snake_head[1] > food[1]:
            if 0 in actions:
                command = 0
            elif self.state in actions:
                command = self.state
            else:
                command = actions[0]
        elif snake_head[1] < food[1]:
            if 1 in actions:
                command = 1
            elif self.state in actions:
                command = self.state
            else:
                command = actions[0]

        self.state = command
        if scene_info["status"] == "GAME_OVER":
            print(scene_info["snake_head"], scene_info["food"], self.state)
            print(command, actions)
            return "RESET"
        else:
            if command == 0:
                return "UP"
            elif command == 1:
                return "DOWN"
            elif command == 2:
                return "LEFT"
            elif command == 3:
                return "RIGHT"
            else:
                return "NONE"

    def reset(self):
        """
        Reset the status if needed
        """
        self.state = 2
        pass
