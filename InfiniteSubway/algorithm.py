import pyautogui

import Controls.movement
import Game.collision
import Game.detect_obsticles
import Game.detect_trains
import Game.rails

dtt = Game.detect_trains.StaticTrains()
dto = Game.detect_obsticles.Obsticles()
collision = Game.collision.Collision()
rails = Game.rails.Rails()
move = Controls.movement.Movement()


class InfiniteSubwayAlgo:
    def __init__(self):
        self.window = None

    def run_algo(self):
        run = True

        while run:
            # trains = self.filter_not_none(dtt.find_every_train())
            large_obstacle = dto.find_large_obsticle()
            general_obstacle = dto.find_general_obsticle()
            self.window = pyautogui.getWindowsWithTitle('BlueStacks App Player')[0]
            print(self.window.width)
            self.algo( general_obstacle, large_obstacle)
            if collision.is_game_over():
                run = False
                print("Game over")

    def coords_in_range(self, coords):
        middle_line = self.window.width / 2
        for x in coords:
            if x - 100 > middle_line:
                return 'right'
            elif x + 100 < middle_line:
                return 'left'
            else:
                return 'middle'

    def filter_not_none(self, given_list):
        return not_none if (not_none := [x for x in given_list if x is not None]) else None

    def algo(self, general_obstacle, large_obstacle):
        modern_train = dtt.find_modern_trains()

        if modern_train is not None:
            coords_range = self.coords_in_range(modern_train)
            if coords_range == 'left':
                print("moving right")
                move.move(3)

            elif coords_range == 'right':
                print("moving left")
                move.move(2)

            else:
                if rails.lef_or_right_free() == "left":
                    move.move(2)
                elif rails.lef_or_right_free() == "right":
                    move.move(3)

        if general_obstacle is not None:
            if general_obstacle[1] > self.window.height / 2 - 10:
                if large_obstacle is not None:
                    move.move(0)
                else:
                    move.move(1)

