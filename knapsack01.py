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


def pause():
    raw_input("Continue")

#specific list
# lista = [(6,10),(3,4),(5,8),(6,12),(3,3),(2,1),(2,2),(1,1),(4,3),(1,1),(2,6)]
lista = [(10, 4), (4, 12), (4, 49), (2, 25), (3, 33), (4, 35), (3, 0), (10, 21), (9, 13), (6, 15), (1, 31), (7, 21), (3, 42), (3, 36),
(9, 14), (3, 24), (7, 41), (7, 37), (2, 15), (1, 15), (2, 29), (4, 1), (2, 16), (1, 45), (5, 11), (9, 42), (8, 12), (10, 40), (9, 12),
(4, 8), (5, 30), (6, 12), (5, 11), (9, 46), (8, 25), (5, 16), (4, 42), (10, 14), (8, 40), (3, 13), (5, 33), (1, 49), (3, 13), (1, 36), (2, 28),
(10, 2), (8, 6), (3, 49), (6, 23), (6, 38)]

#problem parameters
# IND_INIT_SIZE = 5
MAX_ITEM = 15
MAX_WEIGHT = 100
# MAX_WEIGHT = 6
NBR_ITEMS = len(lista)
NGEN = 50
CXPB = 0.75
MUTPB = 0.25


#algorithm parameters
MU = 50
LAMBDA = 100

creator.create("Fitness", base.Fitness, weights=(-1.0, 1.0))
creator.create("Individual", list, fitness=creator.Fitness)

# Create the item dictionary: item name is an integer, and value is
# a (weight, value) 2-uple.




items = {}
# Create random items and store them in the items' dictionary.
for i in range(NBR_ITEMS):
    # items[i] = (random.randint(1, 10), random.randint(0, 100))
    items[i] = lista[i]



toolbox = base.Toolbox()
toolbox.register("attr_item_bool", random.randint, 0, 1)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_item_bool, NBR_ITEMS)

toolbox.register("population", tools.initRepeat, list, toolbox.individual)

def evalKnapsack(individual):
    weight = 0.0
    value = 0.0
    # print individual
    for i in range(len(individual)):
        include = individual[i]
        # print include
        weight += include*items[i][0]
        value  += include*items[i][1]
    # print weight
    # print value
    # pause()
    if len(individual) > MAX_ITEM or weight > MAX_WEIGHT:
        return 10000, 0     #Makes sure overweighted bags are dominated
    return weight, value
    

toolbox.register("evaluate", evalKnapsack)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selNSGA2)

def main():


    pop = toolbox.population(n=MU)
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
