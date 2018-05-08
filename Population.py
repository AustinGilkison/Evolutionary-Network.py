
import DNA
import random


class Population:
    def __init__(self, target, mutation_rate, pop_max, accepted):
        self.Accepted = accepted
        self.target = target
        self.mutationRate = mutation_rate
        self.pop_max = pop_max
        self.population = []
        self.targetLength = len(self.target)
        index = 0
        while index < pop_max:
            # print("DNA Unit " + str(index+1))
            self.population.append(DNA.DNA(self.targetLength, accepted, target))
            index = index + 1
        # self.matingPool = []
        self.MostFit = []
        self.fitness = 0
        self.maxFitness = 0

    def natural_selection(self):
        # max_fitness = 0
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
            # fitness =  Lib.map(self.population[index].fitness, 0, max_fitness, 0, 100)
            # n = (math.floor(fitness*100)**2)
            # i = 0
            # while i < n:
            #     self.matingPool.append(self.population[index])
            #     i = i  + 1

            index = index + 1
        # print("size of MatingPool " + str(len(self.matingPool)))

    def generate(self):
        index = 0
        new_population = []
        while index < len(self.population):
            # print("Generating unit " + str(index))
            partner1 = self.accept_reject()
            partner2 = self.accept_reject()

            # a = int(math.floor(random.randrange(len(self.matingPool))))
            # b = int(math.floor(random.randrange(len(self.matingPool))))
            # partnerA = self.matingPool[a]
            # partnerB = self.matingPool[b]

            child = partner1.crossover(partner2)
            child.mutate(self.mutationRate)
            new_population.append(child)
            index = index + 1
        self.population = new_population
        # self.matingPool = []
    
    def accept_reject(self, ):
        be_safe = 0
        while True:
            index = random.randint(0, len(self.population)-1)
            r = random.randint(0, int(self.maxFitness*100))
            partner = self.population[index]
            if r < partner.fitness*100:
                return partner
            be_safe = be_safe + 1
            if be_safe > 10000:
                return None

    def calc_fitness(self):
        # print("population mass fitness_cal started")
        index = 0
        while index < len(self.population):
            # print("Population fitness_cal stated " + str(index))
            self.population[index].calc_fitness()
            index = index + 1
            # print("Population fitness_cal fished")
        # print("Population mass fitness_cal finished")

    def evaluate(self):
        index = 0
        while index < len(self.population):
            if self.population[index].fitness > self.maxFitness:
                self.maxFitness = self.population[index].fitness
            index = index + 1
        return self.maxFitness
        
    def make_new(self):
        index = 0
        self.population = []
        while index < self.popmax:
            self.population.append(DNA.dna(self.targetLength, self.Accepted, self.target))
            index = index + 1

    def fittest_element(self):
        index = 0
        result = ""
        while index < len(self.MostFit):
            result += self.MostFit[index]
            index += 1
        return result



