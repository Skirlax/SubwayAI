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

    # def are_free_rails(self):
    #     match = pyautogui.locateAOnWindow('rails.png','BlueStacks App Player' ,confidence=0.6)
    #     if match is not None:
    #         freest_rails = min(match, key=lambda x: x[1])
    #         return freest_rails[1] - self.screen_height / 2
