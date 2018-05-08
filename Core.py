
import Population
import string


class Engine:

    def __init__(self, target, mutation_rate, pop_max):
        self.target = target
        self.mutationRate = mutation_rate
        self.pop_max = pop_max
        self.accepted = string.ascii_letters + " " + string.digits
        self.gen_till_complete = None

    def run_simulation(self):
    
        population = Population.Population(self.target, self.mutationRate, self.pop_max, self.accepted)

        index = 1
        highest = 0
        while highest < 100:
            # print(index)
            # print("Starting main fitness_cal")
            population.calc_fitness()
            # print("Finished main fitness_cal")

            # print("Starting natural section")
            population.natural_selection()
            # print("Finishing natural section")

            # print("Generating next Population")
            population.generate()
            # print("Finished generating next Population")

            # print("Evaluating population")
            loop = int(population.evaluate()*100)

            most_fit = population.fittest_element()

            print("Fittest from population " +
                  str(index) + ' is "' + str(most_fit) +
                  '" with a fitness of ' + str(loop) + "%")

            if loop > highest:
                highest = loop
            # print("Evaluation "+ str(highest))
            # print(" ")
            index = index + 1

            self.gen_till_complete = index
