import pyautogui


class Container:
    screen_width, screen_height = pyautogui.size()
    subway_width, subway_height = pyautogui.getWindowsWithTitle("BlueStacks App Player")[0].size
