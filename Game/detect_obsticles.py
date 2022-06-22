import pyautogui


class Obsticles:
    def __init__(self):
        self.window = pyautogui.getWindowsWithTitle('BlueStacks App Player')[0]

    def find_small_obsticle(self):
        match = pyautogui.locateOnWindow('Obsticles/small.png', 'BlueStacks App Player', confidence=0.6)
        if match is not None:
            return match[1] - self.window.height / 2

    def find_large_obsticle(self):
        match = pyautogui.locateOnWindow('Obsticles/large.png', 'BlueStacks App Player', confidence=0.6)
        if match is not None:
            return match[1] - self.window.height / 2

    def find_smallest_obsticle(self):
        match = pyautogui.locateOnWindow('Obsticles/smallest.png', 'BlueStacks App Player', confidence=0.6)
        if match is not None:
            return match[1] - self.window.height / 2

    def find_general_obsticle(self):
        match = pyautogui.locateOnWindow('Obsticles/general.png', 'BlueStacks App Player', confidence=0.6)
        if match is not None:
            return match[1] - self.window.height / 2
        else:
            return 0
