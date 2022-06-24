import cv2
import pyautogui


class Obsticles:
    def __init__(self):
        self.window = pyautogui.getWindowsWithTitle('BlueStacks App Player')[0]
        self.general_obstacle = cv2.imread('Obsticles/general.png')

    def find_small_obsticle(self):
        match = pyautogui.locateOnWindow('Obsticles/small.png', 'BlueStacks App Player', confidence=0.6)
        if match is not None:
            return match[1] - self.window.height / 2

    def find_large_obsticle(self, return_x=False):
        match = pyautogui.locateOnWindow('Obsticles/large.png', 'BlueStacks App Player', confidence=0.6)
        if match is not None:

            return [match[0], match[1]]

        else:

            return None

    def find_smallest_obsticle(self):
        match = pyautogui.locateOnWindow('Obsticles/smallest.png', 'BlueStacks App Player', confidence=0.6)
        if match is not None:
            return match[1] - self.window.height / 2

    def find_general_obsticle(self, return_x=False):
        match = pyautogui.locateOnScreen(self.general_obstacle, region=self.window.box, confidence=0.55, grayscale=True)
        if match is not None:

            return [(match[0] - self.window.left) + match[2] / 2, match[1]]

        else:

            return None

    def find_all_obsticles(self):
        matches = []
        matches.append(self.find_general_obsticle(return_x=True))
        matches.append(self.find_large_obsticle(return_x=True))
        return matches
