import cv2
import pyautogui


class Play:
    def __init__(self):
        self.window = pyautogui.getWindowsWithTitle('BlueStacks App Player')[0]
        self.image = cv2.imread('player.png')


    def click_play(self):
        for _ in range(5):
            play_button = pyautogui.locateOnWindow('play_button.png', 'BlueStacks App Player', confidence=0.8)
            if play_button is not None:

                pyautogui.click(play_button[0] + play_button[2] / 2, play_button[1] + play_button[3] / 2)
            else:
                break

    def find_player(self):

        match = pyautogui.locateOnScreen(self.image, region=self.window.box, confidence=0.7, grayscale=True)
        if match is not None:
            pyautogui.moveTo(match[0] + match[2] / 2, match[1] + match[3] / 2)
            return [(match[0] - self.window.left) + match[2] / 2, match[1] + match[3] / 2]
