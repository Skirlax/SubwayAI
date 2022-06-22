import pyautogui


class Movement:

    def move(self, direction_num):
        if direction_num == 0:
            pyautogui.press('down')

        elif direction_num == 1:
            pyautogui.press('up')
        elif direction_num == 2:
            pyautogui.press('left')

        elif direction_num == 3:
            pyautogui.press('right')
