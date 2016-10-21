import random

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools

def write_solution(data):
    """
    this function write data to file
    :param data:
    :return:
    """
    data = str(data)
    file_name = "solutions.txt"
    with open(file_name, 'a') as state_file:
        state_file.write(data+"\n")


def list2dict(inList):
    # dictionary = dict(zip(list(range(len(inList))),inList))
    dictionary = dict([(k, inList[k]) for k in range(len(inList))])
    return dictionary

def pause():
    raw_input("Continue")

#problem parameters
IND_INIT_SIZE = 5
MAX_ITEM = 15
MAX_WEIGHT = 100
NBR_ITEMS = 50
# NGEN = 100
CXPB = 0.6
MUTPB = (1-CXPB)
# POPSIZE = 50

NGEN = 10000
POPSIZE = 150

#algorithm parameters
MU = int(0.1*POPSIZE)
LAMBDA = int(1.3*POPSIZE)

creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
creator.create("Individual", set, fitness=creator.Fitness)

# Create the item dictionary: item name is an integer, and value is
# a (weight, value) 2-uple.

lista = [(10, 4), (4, 12), (4, 49), (2, 25), (3, 33), (4, 35), (3, 0), (10, 21), (9, 13), (6, 15), (1, 31), (7, 21), (3, 42), (3, 36),
 (9, 14), (3, 24), (7, 41), (7, 37), (2, 15), (1, 15), (2, 29), (4, 1), (2, 16), (1, 45), (5, 11), (9, 42), (8, 12), (10, 40), (9, 12),
  (4, 8), (5, 30), (6, 12), (5, 11), (9, 46), (8, 25), (5, 16), (4, 42), (10, 14), (8, 40), (3, 13), (5, 33), (1, 49), (3, 13), (1, 36), (2, 28),
   (10, 2), (8, 6), (3, 49), (6, 23), (6, 38)]

items = list2dict(lista)

toolbox = base.Toolbox()
toolbox.register("attr_item", random.randrange, NBR_ITEMS)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_item, IND_INIT_SIZE)
print toolbox.individual()

toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalKnapsack(individual):
    weight = 0.0
    value = 0.0
    # print individual
    # pause()
    for item in individual:
        weight += items[item][0]
        value += items[item][1]
    if len(individual) > MAX_ITEM or weight > MAX_WEIGHT:
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

toolbox.register("evaluate", evalKnapsack)
toolbox.register("mate", cxSet)
toolbox.register("mutate", mutSet)
toolbox.register("select", tools.selNSGA2)

def main():


    pop = toolbox.population(n=POPSIZE)
    hof = tools.ParetoFront()
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", numpy.mean, axis=0)
    stats.register("std", numpy.std, axis=0)
    stats.register("min", numpy.min, axis=0)
    stats.register("max", numpy.max, axis=0)

    algorithms.eaMuPlusLambda(pop, toolbox, MU, LAMBDA, CXPB, MUTPB, NGEN, stats,
                              halloffame=hof)


    # print hof
    print("Best individual is %s, %s" % (hof[len(hof)-1], hof[len(hof)-1].fitness.values))
    write_solution([hof[len(hof)-1], hof[len(hof)-1].fitness.values])
    return pop, stats, hof


if __name__ == "__main__":
    main()
