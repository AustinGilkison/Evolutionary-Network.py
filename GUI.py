# Added functions for checking properties when creating sim instance and running sim and also checking if they are the
# the correct type.

# Checking GUI properties against sim instance properties

# GUI will only start if GUI.py is __main__

# TODO refactor code so that GUI pulls directly from Core.py instead of using intermediate Class Simulation.

from tkinter import *
import Core
import logging
import exceptions
import LogConfig


LOG_FORMAT = "%(filename)s %(levelname)s %(asctime)s - %(message)s"
logging.basicConfig(filename=LogConfig.DEBUG_LOG,
                    level=logging.DEBUG,
                    format=LOG_FORMAT,
                    filemode='w')
logger = logging.getLogger()

simulation = None
logger.info("GUI instance started")


class Simulation:
    """Class for a simulation object that will hold all of the values that may be needed
    for the Core Engine to run properly."""

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
        """ Will set teh properties for the Simulation instance.

        :param str target: The target that the algorithm will be trying the find.
        :param int mutation: The amount of mutation that will be introduced into the gene pool.
        :param int pop: The Amount of DNA instances that will be created for each evolution.
        :return: None
        """

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
        """Creates a new instance of ``Core.Engine`` and pushes the needed values such as
        `target`, `mutation`, and `pop`. The new ``Core.Engine`` instance is saved as simulation.
        """

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
        """Updates Simulation's `numberOfGenerations` value with `simulations.currentGen` value."""

        logger.debug("Updating the Simulation instance generation number to the "
                     "generation number of Core.Engine instance, Current value: {old}, New value: {new}".format(
                        new=self.simulation.currentGen,
                        old=self.numberOfGenerations
                        ))
        self.numberOfGenerations = self.simulation.currentGen

    def update_status(self, status):
        """Updates the status of the status text in the GUI.

        :param str status: The new status of the program.
        :return: None
        """

        logger.debug("Updating GUI status, Current status: {old}, New status: {new}".format(
                        old=self.status,
                        new=status
                        ))
        self.status = status
        statusRs.config(text=self.status)
        root.update()

    def update_fitness(self):
        """Updates Simulation's `populationFitness` value with `simulation.fittest_yet` value."""

        logger.debug("Updating fitness, Current fitness: {old}, New fitness: {new}".format(
                        old=self.populationFitness,
                        new=self.simulation.fittest_yet
                        ))
        self.populationFitness = self.simulation.fittest_yet


def incorrect_property_types():
    """Will update GUI's status to 'Property types incorrect!'."""

    sim.update_status("Property types incorrect!")


def set_properties():
    """Function to be called by GUI to set properties."""

    if property_type_check():
        sim.set_properties(targetIn.get(), int(mutationIn.get()), int(popIn.get()))
    else:
        incorrect_property_types()


def property_type_check():
    """Checks the variable types of `mutationIn`, `popIn`, and `targetIn` in ensure they are the correct types.

    :raises ValueError: Either `mutationIn` or `popIn` can not be converted into an int and/or
    `targetIn` can not be converted into str.
    """
    try:
        int(mutationIn.get())
        int(popIn.get())
        str(targetIn.get())
    except ValueError as exc:
        mess = "Unable to convert mutationIn ({value}) to int: {error}".format(
            value=mutationIn.get(),
            error=exc
        )
        print(mess)
        logger.error(mess)
    else:
        return True


def property_sync_check():
    """Checks if the values in teh GUI are the same values being ran though the ``Core.Engine`` instance,
    if they are not then the ``Core.Engine`` instance will be recreated with the correct values.

    :raises: exceptions.PropertiesOutOfSync: Values in GUI and ``Core.Engine`` instance are out of sync,
    this will recreate the ``Core.Engine`` instance with the correct values.
    :return: True if property types are correct.
    """
    if property_type_check():
        gui_properties = [targetIn.get(), int(mutationIn.get()), int(popIn.get())]
        sim_properties = [sim.target, sim.mutation, sim.pop]

        # TODO add function to auto correct PropertiesOutOFSync,
        # by giving option to auto recreate instance with new Properties

        for i in range(0, 3):
            try:
                if gui_properties[i] != sim_properties[i]:
                    raise exceptions.PropertiesOutOfSync("Values (GUI) {} and (SIM) {} are out of sync".format(
                        gui_properties,
                        sim_properties
                    ))
            except exceptions.PropertiesOutOfSync as exc:
                print("PropertiesOutOfSync: " + str(exc))
                logger.warning("PropertiesOutOfSync: " + str(exc))
                # TODO create function in Dev window to set weather you want PropertiesOutOfSync to auto correct

                set_properties()
                init_sim()
                mess = "Properties Synced, Checking again..."
                print(mess)
                logger.debug(mess)
                property_sync_check()
        return True

    else:
        incorrect_property_types()
        return False


def run_sim_x_times(times=1, infinity=False):
    """Run a evolution cycle for the ``Core.Engine``, The amount of times is determined by the `times` and infinity`
    parameters.

    :param int times: The amount of evolutions the simulation will go though, Will stop if the target is met.
    :param bool infinity: If true simulation will keep running evolution till that target is met.
    """

    if property_sync_check():

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


# TODO create a function to stop any evolution cycle.
def run_sim_once():
    """Function to be called by GUI that will run the
    :func: ``run_sim_x_times`` once using the default `times` value of 1."""

    run_sim_x_times()


def run_sim_10_times():
    """Function to be called by GUI that will run the :func: ``run_sim_x_times`` 10 times."""

    run_sim_x_times(times=10)


def run_sim_100_times():
    """Function to be called by GUI that will run the :func: ``run_sim_x_times`` 100 times."""

    run_sim_x_times(times=100)


# TODO make run till solved a toggle
def run_sim_till_solved():
    """Function to be called by GUI that will run the :func: ``run_sim_x_times`` till target is met."""

    run_sim_x_times(infinity=True)


def init_sim():
    """Function to be called by the GUI to create a new instance of the ``Core.Engine``."""

    print("Creating population")
    property_sync_check()
    sim.init_sim()


def dev_open():
    # TODO Make function to open a Dev window.
    pass
# TODO Create function in Dev window to disable warning messages. Ex. PropertiesOutOfSync Warning.

# TODO Make function to set random properties either in GUI.py or Core.py


if __name__ == "__main__":
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

    devBt = Button(root, text='Dev Mode', command=dev_open)

    root.mainloop()
