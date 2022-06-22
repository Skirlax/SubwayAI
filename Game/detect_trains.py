import pyautogui

import container


class StaticTrains(container.Container):
    def __init__(self):
        super().__init__()
        self.window = pyautogui.getWindowsWithTitle('BlueStacks App Player')[0]




    # def find_modern_trains(self):
    #     match = pyautogui.locateOnScreen('Trains_imgs/modern_train.png', confidence=0.6)
    #     if match is not None:
    #         return match[1] - self.window.height / 2
    #
    # def find_old_trains(self):
    #     match = pyautogui.locateOnScreen('Trains_imgs/old_train.png', confidence=0.6)
    #     if match is not None:
    #         print(match[1])
    #         return match[1] - self.window.height / 2
    #
    # def find_cargo_trains(self):
    #     match = pyautogui.locateOnScreen('Trains_imgs/cargo_train.png', confidence=0.6)
    #     if match is not None:
    #         return match[1] - self.window.height / 2
    #
    # def find_ramp_trains(self):
    #     match = pyautogui.locateOnScreen('Trains_imgs/ramp_train.png', confidence=0.6)
    #     if match is not None:
    #         return match[1] - self.window.height / 2

    # copy all the methods above, but find the match on a window with a title "BlueStacks App Player"
    def find_modern_trains(self):
        match = pyautogui.locateOnWindow('Trains_imgs/modern_train.png', 'BlueStacks App Player', confidence=0.6)
        if match is not None:
            return match[1] - self.window.height / 2
        else:
            return 0

    def find_old_trains(self):

        match = pyautogui.locateOnWindow('Trains_imgs/old_train.png', 'BlueStacks App Player', confidence=0.6)
        if match is not None:
            return match[1] - self.window.height / 2
        else:
            return 0

    def find_cargo_trains(self):
        match = pyautogui.locateOnWindow('Trains_imgs/cargo_train.png', 'BlueStacks App Player', confidence=0.6)
        if match is not None:
            return match[1] - self.window.height / 2
        else:
            return 0

    def find_ramp_trains(self):
        match = pyautogui.locateOnWindow('Trains_imgs/ramp_train.png', 'BlueStacks App Player', confidence=0.7)
        if match is not None:
            return match[1] - self.window.height / 2
        else:
            return 0
