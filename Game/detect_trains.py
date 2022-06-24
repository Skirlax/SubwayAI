import cv2
import pyautogui

import container


class StaticTrains(container.Container):
    def __init__(self):
        super().__init__()
        self.window = pyautogui.getWindowsWithTitle('BlueStacks App Player')[0]
        self.modern_train = cv2.imread('Trains_imgs/modern_train.png')
        self.cargo_train = cv2.imread('Trains_imgs/cargo_train.png')

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
        window = pyautogui.getWindowsWithTitle('BlueStacks App Player')[0]
        match = pyautogui.locateOnScreen(self.modern_train, region=window.box, confidence=0.6,
                                         grayscale=True)
        if match is not None:
            # print("X is " + str(match[0] - window.left))
            return [(match[0] - window.left) + match[2] / 2, match[1]]


        else:

            return None

    def find_old_trains(self):

        match = pyautogui.locateOnWindow(self.cargo_train, 'BlueStacks App Player', confidence=0.6,
                                         grayscale=True)
        if match is not None:

            return[(match[0] - self.window.left) + self.window.width / 2, match[1]]

        else:

            return None

    def find_cargo_trains(self):
        match = pyautogui.locateOnWindow('Trains_imgs/cargo_train.png', 'BlueStacks App Player', confidence=0.55,
                                         grayscale=True)
        if match is not None:

            return [(match[0] - self.window.left) + self.window.width / 2, match[1]]

        else:

            return None

    def find_ramp_trains(self):
        match = pyautogui.locateOnWindow('Trains_imgs/ramp_train.png', 'BlueStacks App Player', confidence=0.7)
        if match is not None:

            return [match[0], match[1]]


        else:

            return None

    def find_locomotive_trains(self):
        match = pyautogui.locateOnWindow('Trains_imgs/locomotive_train.png', 'BlueStacks App Player', confidence=0.6)
        if match is not None:
            return [match[0], match[1]]
        else:

            return None

    def find_every_train(self):
        return [self.find_modern_trains(), self.find_old_trains(),
                self.find_cargo_trains(), self.find_ramp_trains(),
                self.find_locomotive_trains()]
