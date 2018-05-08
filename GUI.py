from tkinter import *
import Core

simulation = None


def setproperties():
    target = targetIn.get()
    mutation = int(mutationIn.get())
    pop = int(popIn.get())

    global simulation
    simulation = Core.Engine(target, mutation, pop)

    print("props set")


def runsim():
    simulation.runsimulation()
    generationsRs.message = simulation.gentillcomplete


def getresults():
    return simulation.gentillcomplete


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

setProp = Button(root, text="Set Properties", command=setproperties)
run = Button(root, text="RUN", command=runsim)
setProp.grid(row=3, columnspan=2)
run.grid(row=4, columnspan=2)

resultsLb = Label(root, text="Test results")
resultsLb.grid(row=1, column=2, columnspan=2, sticky=N)

generationsLb = Label(root, text="Generations count: ")
generationsRs = Label(root, text="Please run a Test")
generationsLb.grid(row=2, column=2, sticky=E)
generationsRs.grid(row=2, column=3)

root.mainloop()