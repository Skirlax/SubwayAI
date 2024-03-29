import time

import pyautogui

import container


class Collectibles(container.Container):
    def __init__(self):
        super().__init__()

    def find_coins(self):
        window = pyautogui.getWindowsWithTitle('BlueStacks App Player')[0]
        match = list(pyautogui.locateAllOnScreen('Collectibles_imgs/coin.png', confidence=0.6, region=(window.box.left, window.box.top, window.box.width, window.box.height)))
        if match:
            # print(match)
            closest = max(match, key=lambda x: x[1])
            # pyautogui.moveTo(closest[0], closest[1])
            return closest[1] - self.screen_height / 2
        else:
            return 0



    # def find_coins(self):
    #     match = pyautogui.locateOnWindow('Collectibles_imgs/coin.png','BlueStacks App Player' ,confidence=0.6)
    #     if match is not None:
    #         closest = max(match, key=lambda x: x[1])
    #         return closest[1] - self.screen_height / 2
