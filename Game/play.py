import pyautogui


class Play:
    def click_play(self):
        for _ in range(5):
            play_button = pyautogui.locateOnWindow('play_button.png', 'BlueStacks App Player', confidence=0.8)
            if play_button is not None:

                pyautogui.click(play_button[0] + play_button[2] / 2, play_button[1] + play_button[3] / 2)
            else:
                break
