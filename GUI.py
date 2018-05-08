from tkinter import *
import Core

simulation = None


class Simulation():
    def __init__(self):
        self.simulation = None
        self.numberOfGenerations = "Please run a Test"
        self.target = None
        self.mutation = None
        self.pop = None

    def set_properties(self, target, mutation, pop):
        self.target = target
        self.mutation = mutation
        self.pop = pop

    def init_sim(self):
        self.simulation = Core.Engine(self.target, self.mutation, self.pop)

    def update_gen(self):
        self.numberOfGenerations = self.simulation.gen_till_complete


def set_properties():
    sim.set_properties(targetIn.get(), int(mutationIn.get()), int(popIn.get()))
    print("props set")


def run_sim():
    sim.init_sim()
    sim.simulation.run_simulation()
    sim.update_gen()
    generationsRs.config(text=sim.numberOfGenerations)


root = Tk()

targetLb = Label(root, text="Target:")
mutationLb = Label(root, text="Mutation Rate:")
popLb = Label(root, text="Population:")

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
run = Button(root, text="RUN", command=run_sim)
setProp.grid(row=3, columnspan=2)
run.grid(row=4, columnspan=2)

resultsLb = Label(root, text="Test results")
resultsLb.grid(row=1, column=2, columnspan=2, sticky=N)

sim = Simulation()

generationsLb = Label(root, text="Generations count: ")
generationsRs = Label(root, text=sim.numberOfGenerations)
generationsLb.grid(row=2, column=2, sticky=E)
generationsRs.grid(row=2, column=3)

root.mainloop()