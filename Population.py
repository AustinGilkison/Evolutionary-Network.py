
import DNA
import Lib
import random


class Population:
    def __init__(self, target, mutationrate, popmax, accepted):
        self.Accepted = accepted
        self.target = target
        self.mutationRate = mutationrate
        self.popmax = popmax
        self.population = []
        self.targetLength = len(self.target)
        index = 0
        while index < popmax:
            # print("DNA Unit " + str(index+1))
            self.population.append(DNA.dna(self.targetLength, accepted, target))
            index = index + 1
        # self.matingPool = []
        self.MostFit = []
        self.fitness = 0
        self.maxFitness = 0

    def naturalselection(self):
        # maxfitness = 0
        index = 0 
        while index < len(self.population):
            if self.population[index].fitness > self.maxFitness:
                self.maxFitness = self.population[index].fitness
                self.MostFit = self.population[index].genes
            index = index + 1
        # print("Max Fitness " + str(self.maxFitness))
        index = 0
        while index < len(self.population):
            # Old Mating pool method of selection
            # fitness =  Lib.map(self.population[index].fitness, 0, maxfitness, 0, 100)
            # n = (math.floor(fitness*100)**2)
            # i = 0
            # while i < n:
            #     self.matingPool.append(self.population[index])
            #     i = i  + 1

            index = index + 1
        # print("size of MatingPool " + str(len(self.matingPool)))

    def generate(self):
        index = 0
        newpopulation = []
        while index < len(self.population):
            # print("Generating unit " + str(index))
            partner1 = self.acceptreject()
            partner2 = self.acceptreject()

            # a = int(math.floor(random.randrange(len(self.matingPool))))
            # b = int(math.floor(random.randrange(len(self.matingPool))))
            # partnerA = self.matingPool[a]
            # partnerB = self.matingPool[b]

            child = partner1.crossover(partner2)
            child.mutate(self.mutationRate)
            newpopulation.append(child)
            index = index + 1
        self.population = newpopulation
        # self.matingPool = []
    
    def acceptreject(self, ):
        besafe = 0
        while True:
            index = random.randint(0, len(self.population)-1)
            r = random.randint(0, int(self.maxFitness*100))
            partner = self.population[index]
            if r < partner.fitness*100:
                return partner
            besafe = besafe + 1
            if besafe > 10000:
                return None

    def calcfitness(self):
        # print("population mass fitnesscal started")
        index = 0
        while index < len(self.population):
            # print("Population fitnesscal stated " + str(index))
            self.population[index].calcFitness()
            index = index + 1
            # print("Population fitnesscal fished")
        # print("Population mass fitnesscal finished")

    def evaluate(self):
        index = 0
        while index < len(self.population):
            if self.population[index].fitness > self.maxFitness:
                self.maxFitness = self.population[index].fitness
            index = index + 1
        return self.maxFitness
        
    def makenew(self):
        index = 0
        self.population = []
        while index < self.popmax:
            self.population.append(DNA.dna(self.targetLength, self.Accepted, self.target))
            index = index + 1

    def fitestelement(self):
        index = 0
        result = ""
        while index < len(self.MostFit):
            result += self.MostFit[index]
            index += 1
        return result



