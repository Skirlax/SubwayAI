import time
import pickle
import neat
import pyautogui
from stopwatch import Stopwatch

import Controls.movement
import Game.collision
import Game.detect_collectibles
import Game.detect_obsticles
import Game.detect_trains
import Game.play
import Game.rails

dtt = Game.detect_trains.StaticTrains()
dtc = Game.detect_collectibles.Collectibles()
coll = Game.collision.Collision()
rails = Game.rails.Rails()
play = Game.play.Play()
obsticles = Game.detect_obsticles.Obsticles()

move = Controls.movement.Movement()
sw = Stopwatch()
live_stopwatch = Stopwatch().reset()
obsticle_stopwatch = Stopwatch().reset()


class AI:
    def __init__(self):
        self.counter = 5
        self.fitness = 0
        self.window = None
        self.inputs = None

    def run(self):
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                             neat.DefaultSpeciesSet, neat.DefaultStagnation,
                             "config.txt")
        p = neat.Population(config)
        # p = neat.Checkpointer.restore_checkpoint('neat-checkpoint-0')
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        p.add_reporter(neat.Checkpointer(1))
        best = p.run(self.evaluation, 50)
        # save it to pickle file
        with open('best_genome.pickle', 'wb') as f:
            pickle.dump(best, f)

    def evaluation(self, genomes, config):
        for index, (genome_id, genome) in enumerate(genomes):
            self.calculate_fitness(genome)
            self.get_inputs()
            live_stopwatch.reset()
            obsticle_stopwatch.reset()
            sw.start()
            print(f"Evaluating genome {index}")
            genome.fitness = 0 if genome.fitness is None else genome.fitness

            while not coll.is_game_over():
                self.calculate_fitness(genome)
                self.get_inputs()
                self.play(genome, config, self.inputs)

                self.counter = 5
                self.calculate_fitness(genome)
                self.get_inputs()

            self.fitness = 0

            pyautogui.press("esc")
            time.sleep(10)

            # if genome.fitness is not None:
            #     genome.fitness -= 100

            print(genome.fitness)

            play.click_play()

            sw.reset()

    def play(self, genome, config, inputs):
        self.calculate_fitness(genome)
        self.get_inputs()
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        output = net.activate(inputs)
        decision = output.index(max(output))
        move.move(decision)
        # self.calculate_fitness(genome)

    def get_inputs(self):
        inputs = [dtt.find_modern_trains(), dtt.find_old_trains(), dtt.find_cargo_trains(),
                  dtt.find_ramp_trains(), dtt.find_locomotive_trains(),
                  rails.lef_or_right_free(), obsticles.find_general_obsticle(), obsticles.find_large_obsticle(), sw.duration]
        self.inputs = inputs


    def calculate_fitness(self, genome):
        if self.window is None:
            self.window = pyautogui.getWindowsWithTitle('BlueStacks App Player')[0]

        for train in dtt.find_every_train():
            if train[1] != 0:

                if train[1] >= (self.window.height / 2) - 200:
                    print("train is close")
                    live_stopwatch.start()
                    break
        for obsticle in obsticles.find_all_obsticles():
            print(obsticle)
            if obsticle[1] != 0:
                print("obsticle is close")
                obsticle_stopwatch.start()
                break

        if live_stopwatch.duration >= 5 or obsticle_stopwatch.duration >= 5:
            if not coll.is_game_over():
                self.fitness += 100
                print("avoided death")
            live_stopwatch.reset()
            obsticle_stopwatch.reset()

        if sw.duration > self.counter:
            self.fitness += 80
            self.counter += 5

        # self.fitness -= dtc.find_coins()
        # self.fitness -= rails.are_free_rails()
        genome.fitness = self.fitness
