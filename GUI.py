from tkinter import *
import Core
# TODO Create Documentation

simulation = None


class Simulation():
    def __init__(self):
        self.simulation = None
        self.numberOfGenerations = "Please run a Test"
        self.target = None
        self.mutation = None
        self.pop = None
        self.status = "Awaiting Test"
        self.populationFitness = 0

    def set_properties(self, target, mutation, pop):
        self.target = target
        self.mutation = mutation
        self.pop = pop
        self.update_status("Properties set, population creation ready")

    def init_sim(self):
        self.simulation = Core.Engine(self.target, self.mutation, self.pop)
        self.simulation.gen_population()
        self.update_status("Population created")

    def update_gen(self):
        self.numberOfGenerations = self.simulation.currentGen

    def update_status(self, status):
        self.status = status
        statusRs.config(text=self.status)
        root.update()

    def update_fitness(self):
        self.populationFitness = self.simulation.fittest_yet


def set_properties():
    sim.set_properties(targetIn.get(), int(mutationIn.get()), int(popIn.get()))
    print("Properties set")


def run_sim_x_times(times=1):
    index = 0
    while index < times:
        print("Starting simulation")
        sim.update_status("Running Evolution!")
        sim.simulation.run_once()
        sim.update_gen()
        generationsRs.config(text=sim.numberOfGenerations)
        sim.update_fitness()
        if sim.populationFitness == 100:
            sim.update_status("Solution found")
            break
        else:
            sim.update_status("Evolution finished")
        index += 1


def run_sim_once():
    run_sim_x_times()


def run_sim_10_times():
    run_sim_x_times(times=10)


def run_sim_100_times():
    run_sim_x_times(times=100)


def init_sim():
    print("Creating population")
    sim.init_sim()




# TODO Make function to set random properties either in GUI.py or Core.py

root = Tk()

targetLb = Label(root, text="Target:")
mutationLb = Label(root, text="Mutation Rate:")
popLb = Label(root, text="Population:")

# TODO Make function to test if correct input types are being used by the user

targetIn = Entry(root)
mutationIn = Entry(root)
popIn = Entry(root)

targetLb.grid(row=0, sticky=E)
targetIn.grid(row=0, column=1)
mutationLb.grid(row=1, sticky=E)
mutationIn.grid(row=1, column=1)
popLb.grid(row=2, sticky=E)
popIn.grid(row=2, column=1)

setProp = Button(root, text="Set Properties", command=set_properties)
sim = Simulation()
create = Button(root, text="Create  population", command=init_sim)
run = Button(root, text="RUN", command=run_sim_once)
run_10_times = Button(root, text="RUN 10 times", command=run_sim_10_times)
run_100_times = Button(root, text="RUN 100 times", command=run_sim_100_times)
setProp.grid(row=3, columnspan=3)
create.grid(row=4, columnspan=3)
run.grid(row=5, column=0, sticky=E)
run_10_times.grid(row=5, column=1,)
run_100_times.grid(row=5, column=2, sticky=W)

resultsLb = Label(root, text="Test results")
resultsLb.grid(row=1, column=2, columnspan=2, sticky=N)

generationsLb = Label(root, text="Generations count: ")
generationsRs = Label(root, text=sim.numberOfGenerations)
generationsLb.grid(row=2, column=3, sticky=E)
generationsRs.grid(row=2, column=4, sticky=W)

statusLb = Label(root, text="Status: ")
statusRs = Label(root, text=sim.status)
statusLb.grid(row=3, column=3, sticky=E)
statusRs.grid(row=3, column=4, sticky=W)

root.mainloop()
