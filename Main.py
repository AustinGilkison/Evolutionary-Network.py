
import Population, string, time, Lib

target = "cat in the hat"
mutationRate = 1
popmax = 2000
Accepted = string.ascii_letters + " "


population_ = Population.population(target, mutationRate, popmax, Accepted)

index = 1
highest = 0
while highest < 100:
    #print(index)
    #print("Starting main fitnesscal")
    population_.calcFitness()
    #print("Finished main fitnesscal")

    #print("Starting natural section")
    population_.naturalSelection()
    #print("Finishing natural section")

    #print("Generating next Population")
    population_.generate()
    #print("Finished generating next Population")

    #print("Evaluating population")
    loop = int(population_.evaluate()*100)

    MostFit = population_.fitestElement()

    print("Fitest from population " + str(index) + ' is "' + str(MostFit) + '" with a fitness of ' + str(loop))
    if loop > highest:
        highest = loop
    print("Evaluation "+ str(highest)) 
    #print(" ")
    index = index + 1


class sim:

    def __init__(self, target, mutationRate, popmax):

        self.target = target
        self.mutationRate = mutationRate
        self.popmax = popmax
        self.Accepted = string.ascii_letters + " "
        #print("starting pop")
        self.population_ = Population.population(self.target, self.mutationRate, self.popmax, self.Accepted)
        #print("pop finished")
    #@Lib.time_it
    def Simulate(self):
        index = 1
        highest = 0
        while highest < 100:
            #print(index)
            #print("Starting main fitnesscal")
            self.population_.calcFitness()
            #print("Finished main fitnesscal")

            #print("Starting natural section")
            self.population_.naturalSelection()
            #print("Finishing natural section")

            #print("Generating next Population")
            self.population_.generate()
            #print("Finished generating next Population")

            #print("Evaluating population")
            loop = int(self.population_.evaluate()*100)

            MostFit = self.population_.fitestElement()

            #print("Fitest from population " + str(index) + ' is "' + str(MostFit) + '" with a fitness of ' + str(loop))
            if loop > highest:
                highest = loop
            #print("Evaluation "+ str(highest)) 
            #print(" ")
            index = index + 1
        
        '''
        def test():
            dna = population_.population[0]
            pop = dna.genes
            for j in population_.population:
                print(" ")
                for i in pop:
                    print(i)
                    '''
def time_it(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            result = func(*args, **kwargs)
            end = time.time()
            print(func.__name__ + "took" + (start - end))