import random
import math

# TODO Create Documentation


class DNA:
    """A Object that will contain a string of accepted letters."""

    def __init__(self, target_length, accepted, target):
        """
        Init for DNA instance.
        Also creates ``genes`` which is a string of random accepted characters.

        :param int target_length: The length of the target.
        :param str accepted: The accepted characters that can be used when generating a new DNA instance.
        :param str target: The target that teh simulation is trying to met.
        """

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
        """Looks at each index of the DNA's gene and determines how many characters match the target.

        :return float: The fitness of the DNA instance.
        """

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
        """Splices the current DNA instance and the partner DNA instance at a random point
        creating a new child DNA instance

        :param DNA Object partner: The DNA object that you would like to splice with.
        :return: DNA object that has genes from both the original and the partner DNA object.
        :rtype: DNA Object
        """

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
        """Gives DNA object ability to introduce mutation into its genes.

        :param int mutation_rate: The probability out of 100 that mutation will occur.
        """

        index = 0
        # print("Mutating")
        while index < len(self.genes):
            if random.randint(0, 100) < mutation_rate:
                self.genes[index] = random.choice(self.Accepted)
            index = index + 1
        # print(self.genes)
