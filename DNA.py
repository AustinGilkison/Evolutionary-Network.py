
import random, math

class dna:

    def __init__(self, targetLength, Accepted, target):
        self.Accepted = Accepted
        self.targetLength = targetLength
        self.genes = []
        self.fitness = 0.00
        self.target = target
        index = 0
        while index < targetLength:
            self.genes.append(random.choice(Accepted))
            index = index + 1

    def calcFitness(self):
        score = 0
        index = 0
        while index < len(self.genes):
            #print("DNA fitnesscal stated " + str(index))
            if self.genes[index] == self.target[index]:
                score = score + 1
            #print(score)
            index = index + 1
            #print("DNA fitnesscal finished")
        self.fitness = float(score)/float(self.targetLength)
        #print(self.fitness)
        return self.fitness

    def crossover(self, partner):
        child = dna(self.targetLength, self.Accepted, self.target)
        midpoint = math.floor(random.randrange(len(self.genes)))
        index = 0

        while index < len(self.genes):
            if index > midpoint :
                child.genes[index] = self.genes[index]
            else:
                child.genes[index] = partner.genes[index]
            index = index + 1
        #print(child.genes)
        return child

    def mutate(self, mutationRate):
        index = 0
        #print("Mutating")
        while index < len(self.genes):
            if random.randint(0,100) < mutationRate:
                self.genes[index] = random.choice(self.Accepted)
            index = index + 1
        #print(self.genes)