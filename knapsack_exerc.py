import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

def write_solution(data):
    #FUNCTION TO OUTPUT DATA TO A TXT
    """
    this function write data to file
    :param data:
    :return:
    """
    data = str(data)
    file_name = "solutions.txt"
    with open(file_name, 'a') as state_file:
        state_file.write(data+"\n")


def pause():
    #A PAUSE FUNCTION FOR DEBUGGING
    raw_input("Continue")

def list2dict(inList):
    # dictionary = dict(zip(list(range(len(inList))),inList))
    dictionary = dict([(k, list[k]) for k in range(len(inList))])
    return dictionary

#lists for problem istantiation
lista = [(10, 4), (4, 12), (4, 49), (2, 25), (3, 33), (4, 35), (3, 0), (10, 21), (9, 13), (6, 15), (1, 31), (7, 21), (3, 42), (3, 36),
(9, 14), (3, 24), (7, 41), (7, 37), (2, 15), (1, 15), (2, 29), (4, 1), (2, 16), (1, 45), (5, 11), (9, 42), (8, 12), (10, 40), (9, 12),
(4, 8), (5, 30), (6, 12), (5, 11), (9, 46), (8, 25), (5, 16), (4, 42), (10, 14), (8, 40), (3, 13), (5, 33), (1, 49), (3, 13), (1, 36), (2, 28),
(10, 2), (8, 6), (3, 49), (6, 23), (6, 38)]



#=============%%%%==================#
# a) INPUT THE PROBLEM'S PARAMETERS HERE
#problem parameters
IND_INIT_SIZE = 5               # Individual Initial Size
MAX_ITEM = "x"                  # Max number of items in bag
MAX_WEIGHT = "x"                # Max weight of the bag
NBR_ITEMS = len(lista)          # Total number of items for choosing
NGEN = "x"                      # Number of generations
CXPB = "x"                      # Probability of CrossOver operations
MUTPB = "x"                     # Probability of Mutation operation
POPSIZE = "x"                   # Size of population
#####

#algorithm parameters
LAMBDA = 100



#=============%%%%==================#
# b) REPLACE "?????" FOR THE DATA STRUCTURE THAT YOU WANT. "???" is a valid Python data structure
creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))        # Minimizing first objective(weight), maximizing second (value)
creator.create("Individual", "?????", fitness=creator.Fitness)      # Define the data type of the Individual


# Create the item dictionary(key,value): key is an integer, and value is
# a (weight, item_value) 2-uple. Transforms list to dict
items = list2dict(lista)
toolbox = base.Toolbox()

#Create the attr_item attribute, that will be a random number between 0 and NBR_ITEMS.
toolbox.register("attr_item", random.randrange, NBR_ITEMS)

#=============%%%%==================#
# c) An individual will contain a set of desired items. Its size is variable, but has an initial definition.
# The constructur will create an individual with "????" random (attr_item attribute) items, a parameter defined above.
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_item, "????")

#The population is a fixed-length list of individuals, but its size will be user-defined in the main() function (pop variable)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


#=============%%%%==================#
# d) Define the FITNESS FUNCTION. THIS INCLUDES THE RESTRICTION ON KNAPSACK WEIGHT AND ITEMS
def evalKnapsack(individual):
    weight = 0.0
    value = 0.0

    #HINT: SEE WHAT YOU RECEIVE IN THIS FUNCTION
    #print "individual:" individual
    #pause()    #REMEMBER TO COMMENT THIS WHEN EXECUTING "FOR REAL"
    for ...
        "????"

    if ...

        return 10000, 0     #Makes sure overweighted bags are dominated

    return weight, value

def cxSet(ind1, ind2):
    """Apply a crossover operation on input sets. The first child is the
    intersection of the two sets, the second child is the difference of the
    two sets.
    """


    temp = set(ind1)                # Used in order to keep type
    ind1 &= ind2                    # Intersection (inplace)
    ind2 ^= temp                    # Symmetric Difference (inplace)

    return ind1, ind2

def mutSet(individual):
    """Mutation that pops or add an element."""
    if random.random() < 0.5:
        if len(individual) > 0:     # We cannot pop from an empty set
            individual.remove(random.choice(sorted(tuple(individual))))
    else:
        individual.add(random.randrange(NBR_ITEMS))
    return individual,


#=============%%%%==================#
# e) Insert the operations into the toolbox. These are the operations defined above.
toolbox.register("evaluate",    "????")
toolbox.register("mate",        "????")
toolbox.register("mutate",      "????")
toolbox.register("select", tools.selNSGA2)

def main():

    pop = toolbox.population(n=POPSIZE)
    hof = tools.ParetoFront()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    #Just throw it into the algorithm and see what comes out of it
    algorithms.eaMuPlusLambda(pop, toolbox, POPSIZE, LAMBDA, CXPB, MUTPB, NGEN, stats,
                              halloffame=hof)


    # print hof
    print("Best individual is %s, %s" % (hof[len(hof)-1], hof[len(hof)-1].fitness.values))
    write_solution([hof[len(hof)-1], hof[len(hof)-1].fitness.values])
    return pop, stats, hof


if __name__ == "__main__":
    main()
