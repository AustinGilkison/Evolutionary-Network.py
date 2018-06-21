# TODO Implement logger more!

from tkinter import *
import Core
import logging

# TODO Create Documentation

LOG_FORMAT = "%(filename)s %(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename="./DebugLog.Log",
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()


simulation = None
logger.info("GUI instance started")


class Simulation:
    def __init__(self):
        logger.debug("Init Simulation class")
        self.simulation = None
        self.numberOfGenerations = "Please run a Test"
        self.target = None
        self.mutation = None
        self.pop = None
        self.status = "Awaiting Test"
        self.populationFitness = 0

    def set_properties(self, target, mutation, pop):
        logger.debug("set_properties for Simulation with values "
                     "target: {target}, mutation: {mutation}, and pop: {pop}".format(
                        target=target,
                        mutation=mutation,
                        pop=pop
                        ))
        self.target = target
        self.mutation = mutation
        self.pop = pop
        self.update_status("Properties set, population creation ready")

    def init_sim(self):
        logger.debug("Creating instance of Core.Engine with Simulation values values "
                     "target: {target}, mutation: {mutation}, and pop: {pop}".format(
                        target=self.target,
                        mutation=self.mutation,
                        pop=self.pop
                        ))
        self.simulation = Core.Engine(self.target, self.mutation, self.pop)
        self.simulation.gen_population()
        generationsRs.config(text="0")
        self.update_status("Population created")

    def update_gen(self):
        logger.debug("Updating the Simulation instance generation number to the "
                     "generation number of Core.Engine instance, Current value: {old}, New value: {new}".format(
                        new=self.simulation.currentGen,
                        old=self.numberOfGenerations
                        ))
        self.numberOfGenerations = self.simulation.currentGen

    def update_status(self, status):
        logger.debug("Updating GUI status, Current status: {old}, New status: {new}".format(
                        old=self.status,
                        new=status
                        ))
        self.status = status
        statusRs.config(text=self.status)
        root.update()

    def update_fitness(self):
        logger.debug("Updating fitness, Current fitness: {old}, New fitness: {new}".format(
                        old=self.populationFitness,
                        new=self.simulation.fittest_yet
                        ))
        self.populationFitness = self.simulation.fittest_yet


# TODO create exceptions that will check the value of target mutation and pop are set to acceptable values
def set_properties():
    sim.set_properties(targetIn.get(), int(mutationIn.get()), int(popIn.get()))


def run_sim_x_times(times=1, infinity=False):
    logger.debug("Starting run_sim_x_times function with values times: {time}, and infinity: {infinity}".format(
        time=times,
        infinity=infinity
    ))
    index = 1
    while index <= times or infinity:
        logger.debug("run_sim_x_times round {index}/{time} INFINITY: {infinity}".format(
            index=index,
            time=times,
            infinity=infinity
        ))
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
        if not infinity:
            index += 1


def run_sim_once():
    run_sim_x_times()


def run_sim_10_times():
    run_sim_x_times(times=10)


def run_sim_100_times():
    run_sim_x_times(times=100)


def run_sim_till_solved():
    run_sim_x_times(infinity=True)


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
run_till_solved = Button(root, text="RUN till solved", command=run_sim_till_solved)
setProp.grid(row=3, columnspan=4)
create.grid(row=4, columnspan=4)
run.grid(row=5, column=0, sticky=E)
run_10_times.grid(row=5, column=1, sticky=W)
run_100_times.grid(row=6, column=0, sticky=E)
run_till_solved.grid(row=6, column=1, sticky=W)


resultsLb = Label(root, text="Test results")
resultsLb.grid(row=1, column=4, columnspan=2, sticky=N)

generationsLb = Label(root, text="Generations count: ")
generationsRs = Label(root, text=sim.numberOfGenerations)
generationsLb.grid(row=2, column=4, sticky=E)
generationsRs.grid(row=2, column=5, sticky=W)

statusLb = Label(root, text="Status: ")
statusRs = Label(root, text=sim.status)
statusLb.grid(row=3, column=4, sticky=E)
statusRs.grid(row=3, column=5, sticky=W)

root.mainloop()
