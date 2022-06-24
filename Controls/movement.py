import pyautogui


class Movement:
    def __init__(self):
        self._line = "middle"
        self.moves = []

    def move(self, direction_num):
        if direction_num == 0:
            pyautogui.press('down')

        elif direction_num == 1:
            pyautogui.press('up')
        elif direction_num == 2:
            pyautogui.press('left')
            self._find_current_line("left")



        elif direction_num == 3:
            pyautogui.press('right')
            self._find_current_line("right")

    def _find_current_line(self, direction):
        if not self.moves:
            self._line = direction
        elif len([x for x in self.moves if x == direction]) == 2:
            self._line = self._not_direction(direction)
        elif len([x for x in self.moves if x == direction]) == 1 and not [x for x in self.moves if x == "middle"]:
            self._line = "middle"
        elif len([x for x in self.moves if x == direction]) == 1 and self.moves[-1] == "middle":
            self._line = direction

        if len(self.moves) > 10:
            self.moves.clear()

    def _not_direction(self, direction):
        if direction == "left":
            return "right"
        elif direction == "right":
            return "left"  # elif direction == "up":  #     return "down"  # elif direction == "down":  #     return "up"

    def get_line(self):
        return self._line