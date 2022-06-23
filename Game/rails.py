import pyautogui

import container


class Rails(container.Container):
    def __init__(self):
        super().__init__()

    def are_free_rails(self):
        match = list(pyautogui.locateAllOnScreen('rails.png', confidence=0.5))
        if match:
            freest_rails = min(match, key=lambda x: x[1])
            return freest_rails[1] - self.screen_height / 2
        else:
            return 0

    def lef_or_right_free(self):
        right = pyautogui.locateOnWindow('right.png', 'BlueStacks App Player', confidence=0.5)
        left = pyautogui.locateOnWindow('left.png', 'BlueStacks App Player', confidence=0.5)
        if right is not None:
            return 'right'
        elif left is not None:
            return 'left'
        else:
            return 'none'

    # def are_free_rails(self):
    #     match = pyautogui.locateAOnWindow('rails.png','BlueStacks App Player' ,confidence=0.6)
    #     if match is not None:
    #         freest_rails = min(match, key=lambda x: x[1])
    #         return freest_rails[1] - self.screen_height / 2
