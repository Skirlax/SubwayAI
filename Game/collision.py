import pyautogui


class Collision:
    def is_game_over(self):
        match = pyautogui.locateOnScreen('cauth.png', confidence=0.9)
        keys_match = pyautogui.locateOnScreen('keys.png', confidence=0.9)
        return match or keys_match is not None
