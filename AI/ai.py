import time

import neat
import pyautogui

import Controls.movement
import Game.collision
import Game.detect_collectibles
import Game.detect_trains
import Game.rails
import Game.play
import Game.detect_obsticles
from stopwatch import Stopwatch

dtt = Game.detect_trains.StaticTrains()
dtc = Game.detect_collectibles.Collectibles()
coll = Game.collision.Collision()
rails = Game.rails.Rails()
play = Game.play.Play()
obsticles = Game.detect_obsticles.Obsticles()

move = Controls.movement.Movement()
sw = Stopwatch()


class AI:
    def __init__(self):
        self.counter = 5
        self.fitness = 0

    def run(self):
        config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,
                             neat.DefaultSpeciesSet, neat.DefaultStagnation,
                             "config.txt")
        p = neat.Population(config)
        p.add_reporter(neat.StdOutReporter(True))
        stats = neat.StatisticsReporter()
        p.add_reporter(stats)
        p.add_reporter(neat.Checkpointer(1))
        best = p.run(self.evaluation, 50)

    def evaluation(self, genomes, config):
        for index, (genome_id, genome) in enumerate(genomes):
            sw.start()
            print(f"Evaluating genome {index}")
            genome.fitness = 0 if genome.fitness is None else genome.fitness

            while not coll.is_game_over():
                self.play(genome, config, self.get_inputs())
                self.calculate_fitness(genome)
                self.counter = 5


            self.fitness = 0

            pyautogui.press("esc")
            time.sleep(10)

            # if genome.fitness is not None:
            #     genome.fitness -= 100

            print(genome.fitness)

            play.click_play()

            sw.reset()

    def play(self, genome, config, inputs):
        net = neat.nn.FeedForwardNetwork.create(genome, config)
        output = net.activate(inputs)
        decision = output.index(max(output))
        move.move(decision)

    def get_inputs(self):
        return [dtt.find_modern_trains() * -1, dtt.find_old_trains() * -1, dtt.find_cargo_trains() * -1,
                dtt.find_ramp_trains() * -1,
                dtc.find_coins() * -1, obsticles.find_general_obsticle() * -1, sw.duration]

    def calculate_fitness(self, genome):
        # self.fitness += dtt.find_modern_trains()
        # self.fitness += dtt.find_old_trains()
        # self.fitness += dtt.find_cargo_trains()
        # self.fitness -= dtt.find_ramp_trains()
        self.fitness += obsticles.find_general_obsticle()
        if sw.duration > self.counter:
            self.fitness += 150
            self.counter += 5

        # self.fitness -= dtc.find_coins()
        # self.fitness -= rails.are_free_rails()
        genome.fitness = self.fitness
