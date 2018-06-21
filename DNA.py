import random
import math

# TODO Create Documentation


class DNA:

    def __init__(self, target_length, accepted, target):
        self.Accepted = accepted
        self.targetLength = target_length
        self.genes = []
        self.fitness = 0.00
        self.target = target
        index = 0
        while index < target_length:
            self.genes.append(random.choice(accepted))
            index = index + 1

    def calc_fitness(self):
        score = 0
        index = 0
        while index < len(self.genes):
            # print("DNA fitness_cal stated " + str(index))
            if self.genes[index] == self.target[index]:
                score = score + 1
            # print(score)
            index = index + 1
            # print("DNA fitness_cal finished")
        self.fitness = float(score)/float(self.targetLength)
        # print(self.fitness)
        return self.fitness

    def crossover(self, partner):
        child = DNA(self.targetLength, self.Accepted, self.target)
        midpoint = math.floor(random.randrange(len(self.genes)))
        index = 0

        while index < len(self.genes):
            if index > midpoint :
                child.genes[index] = self.genes[index]
            else:
                child.genes[index] = partner.genes[index]
            index = index + 1
        # print(child.genes)
        return child

    def mutate(self, mutation_rate):
        index = 0
        # print("Mutating")
        while index < len(self.genes):
            if random.randint(0,100) < mutation_rate:
                self.genes[index] = random.choice(self.Accepted)
            index = index + 1
        # print(self.genes)
