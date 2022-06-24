import time
from importlib import reload

import numpy as np

import Game.detect_trains
import Game.detect_collectibles
import Game.collision
import Game.rails
import Game.detect_obsticles
import AI.ai
import Game.play
import InfiniteSubway.algorithm

algo = InfiniteSubway.algorithm.InfiniteSubwayAlgo()

dst = Game.detect_trains.StaticTrains()
dtc = Game.detect_collectibles.Collectibles()
rails = Game.rails.Rails()
coll = Game.collision.Collision()
ai = AI.ai.AI()
obsticles = Game.detect_obsticles.Obsticles()
play = Game.play.Play()


class Main:
    def __init__(self):
        self._main()

    def _main(self):
        run = True
        counter = 5
        # time.sleep(3)
        #
        for x in range(6):
            print(f"Starting in {counter} seconds")
            counter -= 1
            time.sleep(1)
        reload(Game.detect_trains)
        reload(Game.detect_obsticles)
        algo.run_algo()

        # while run:
            # print(dst.find_cargo_trains())
            # player_coords = play.find_player()

                # coords_range = self.coords_in_range(modern_train)
                # print(player_coords)

            # print(dst.find_modern_trains())
            # print(obsticles.find_general_obsticle())
            # old_train_loc = dst.find_old_trains()
            # cargo_train_loc = dst.find_cargo_trains()
            # ramp_train_loc = dst.find_ramp_trains()
            # coin_loc = dtc.find_coins()
            # free_rails_loc = rails.are_free_rails()
            # print(modern_train_loc, old_train_loc, cargo_train_loc, ramp_train_loc, coin_loc, free_rails_loc)

            # if coll.is_game_over():
            #     run = False
            #     print("Game over")





if __name__ == "__main__":
    Main()
