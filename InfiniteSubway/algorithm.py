import pyautogui

import Controls.movement
import Game.collision
import Game.detect_obsticles
import Game.detect_trains
import Game.rails
import Game.play

dtt = Game.detect_trains.StaticTrains()
dto = Game.detect_obsticles.Obsticles()
collision = Game.collision.Collision()
rails = Game.rails.Rails()
move = Controls.movement.Movement()
game = Game.play.Play()


class InfiniteSubwayAlgo:
    def __init__(self):
        self.window = None

    def run_algo(self):
        run = True

        self.window = pyautogui.getWindowsWithTitle('BlueStacks App Player')[0]
        while run:
            # trains = self.filter_not_none(dtt.find_every_train())


            self.algo()
            if collision.is_game_over():
                run = False
                print("Game over")

    def coords_in_range(self, coords):
        middle_line = self.window.width / 2
        for x in coords:
            if x - 50 > middle_line:
                return 'right'
            elif x + 50 < middle_line:
                return 'left'
            else:
                return 'middle'

    def filter_not_none(self, given_list):
        return not_none if (not_none := [x for x in given_list if x is not None]) else None

    def algo(self):
        modern_train = dtt.find_modern_trains()
        general_obsticle = dto.find_general_obsticle()



        # general_obsticle_line = self.coords_in_range(general_obsticle)
        if modern_train is not None:
            modern_train_line = self.coords_in_range(modern_train)
            if modern_train_line == 'left':
                print(move.get_line())
                print("line:" + modern_train_line)
                if move.get_line() == 'left':
                    move.move(3)

            elif modern_train_line == 'right':
                print(move.get_line())
                if move.get_line() == 'right':
                    move.move(2)

            elif modern_train_line == 'middle':
                print(move.get_line())
                print("line:" + modern_train_line)
                if move.get_line() == 'middle':
                    move.move(2)
        if general_obsticle is not None:
            general_obsticle_line = self.coords_in_range(general_obsticle)
            if general_obsticle_line == move.get_line():
                move.move(1)




        # player_coords = game.find_player()


