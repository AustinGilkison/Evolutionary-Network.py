
import DNA, Lib, math, random

class population:
    def __init__(self, target, mutationRate, popmax, Accepted):
        self.Accepted = Accepted
        self.target = target
        self.mutationRate = mutationRate
        self.popmax = popmax
        self.population = []
        self.targetLength = len(self.target)
        index = 0
        while index < popmax:
            #print("DNA Unit " + str(index+1))
            self.population.append(DNA.dna(self.targetLength, Accepted, target))
            index = index + 1
        #self.matingPool = []
        self.MostFit = []
        self.fitness = 0
        self.maxFitness = 0

    def naturalSelection(self):
        maxFitness = 0
        index = 0 
        while index < len(self.population):
            if self.population[index].fitness > self.maxFitness:
                self.maxFitness = self.population[index].fitness
                self.MostFit = self.population[index].genes
            index = index + 1
        #print("Max Fitness " + str(self.maxFitness))
        index = 0
        while index < len(self.population):
            fitness =  Lib.map(self.population[index].fitness, 0, maxFitness, 0, 100)
            
            
            '''
            #Old Mating pool method of selection
            n = (math.floor(fitness*100)**2)
            i = 0
            while i < n:
                self.matingPool.append(self.population[index])
                i = i  + 1
            '''
            index = index + 1
        #print("size of MatingPool " + str(len(self.matingPool)))

    def generate(self):
        index = 0
        newPopulation = []
        while index < len(self.population):
            #print("Generating unit " + str(index))
            partnerA = self.acceptReject()
            partnerB = self.acceptReject()
            

            '''
            a = int(math.floor(random.randrange(len(self.matingPool))))
            b = int(math.floor(random.randrange(len(self.matingPool))))
            partnerA = self.matingPool[a]
            partnerB = self.matingPool[b]
            '''
            child = partnerA.crossover(partnerB)
            child.mutate(self.mutationRate)
            newPopulation.append(child)
            index = index + 1
        self.population = newPopulation
        self.matingPool = []
    
    def acceptReject(self, ):
        beSafe = 0
        first = False
        while True:
            index = random.randint(0, len(self.population)-1)
            r = random.randint(0, int(self.maxFitness*100))
            partner = self.population[index]
            if r < partner.fitness*100:
                return partner
            beSafe = beSafe + 1
            if beSafe > 10000:
                return None
               
        

    def calcFitness(self):
        #print("population mass fitnesscal started")
        index = 0
        while index < len(self.population):
            #print("Population fitnesscal stated " + str(index))
            self.population[index].calcFitness()
            index = index + 1
            #print("Population fitnesscal fished")
        #print("Population mass fitnesscal finished")

    def evaluate(self):
        index = 0
        while index < len(self.population):
            if self.population[index].fitness > self.maxFitness:
                self.maxFitness = self.population[index].fitness
            index = index + 1
        return self.maxFitness
        
    def makeNew(self):
        index = 0
        self.population = []
        while index < self.popmax:
            self.population.append(DNA.dna(self.targetLength, self.Accepted, self.target))
            index = index + 1

    def fitestElement(self):
        index = 0
        result = ""
        while index < len(self.MostFit):
            result += self.MostFit[index]
            index += 1
        return result



