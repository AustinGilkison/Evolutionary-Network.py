import Core

instances = []
test_phrase = "This is a test"
mutation_rate = 1
population_number = 500


def createInstances(TotalinstanceNumber):
    try:
        for i in range(0, TotalinstanceNumber):
            instances.append(Core.engine(test_phrase, mutation_rate, population_number))
        print("Build finished")
    except Exception as ext:
        print("Build failed: " +  str(ext) )
        exit()

def testAttributes():
    if(
        instances[0].target == test_phrase and 
        instances[0].mutationRate == mutation_rate and
        instances[0].popmax == population_number
        ):
        print("testAttributes finished")
    else:
        print("testAttributes failed")
        exit()


createInstances(10)
testAttributes()