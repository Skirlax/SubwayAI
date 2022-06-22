import pyautogui


class Collision:
    def is_game_over(self):
        match = pyautogui.locateOnScreen('cauth.png', confidence=0.9)
        return match is not None
