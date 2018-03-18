
import Population, string, time, Lib


class engine:

    def __init__(self, target, mutationRate, popmax):
        self.target = target
        self.mutationRate = mutationRate
        self.popmax = popmax
        self.accepted = string.ascii_letters + " "

    def runSimulation(self):
    
        population = Population.population(self.target, self.mutationRate, self.popmax, self.accepted)

        index = 1
        highest = 0
        while highest < 100:
            #print(index)
            #print("Starting main fitnesscal")
            population.calcFitness()
            #print("Finished main fitnesscal")

            #print("Starting natural section")
            population.naturalSelection()
            #print("Finishing natural section")

            #print("Generating next Population")
            population.generate()
            #print("Finished generating next Population")

            #print("Evaluating population")
            loop = int(population.evaluate()*100)

            MostFit = population.fitestElement()

            print("Fitest from population " + str(index) + ' is "' + str(MostFit) + '" with a fitness of ' + str(loop) + "%")
            if loop > highest:
                highest = loop
            #print("Evaluation "+ str(highest)) 
            #print(" ")
            index = index + 1
