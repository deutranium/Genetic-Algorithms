import client as C
from ga import *
import numpy as np

#### CONSTANTS ####
OVERFIT_ERR = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
    1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]
NUM_GENES = 11

KEY = '81WmrH1dHrlpZ3Qj2RF4HRr9Qv8gRke6SmF2zNLjHJ3v6wzIYE'

NUM_CHROMOSOMES = 20
POPULATION_SIZE = (NUM_CHROMOSOMES, NUM_GENES)
MATING_POOL_SIZE = 8

# generate the population
INITIAL_POPULATION = np.random.uniform(low = -0.00000000005, high = 0.00000000005, size = POPULATION_SIZE)

# INITIAL_POPULATION = np.array([
#  [ 1.01815264e-12,  3.15526534e-13,  4.60344715e-13, -2.05011803e-12,
#    2.09333439e-12, -1.55942142e-15, -3.19563759e-14,  2.39169383e-14,
#    2.78373525e-14,  2.85011219e-14,  5.35831613e-14],
#  [ 1.10023797e-12,  3.40964864e-13,  4.97458552e-13, -2.21540231e-12,
#    2.26210286e-12, -1.60552495e-15, -3.29011505e-14,  2.46240309e-14,
#    2.86603502e-14,  2.93437436e-14,  5.51673211e-14],
#  [ 8.36780117e-13,  2.59319007e-13,  3.78339446e-13, -1.68491240e-12,
#    1.72043025e-12, -1.60192657e-15, -3.28274108e-14,  2.45688422e-14,
#    2.85961151e-14,  2.92779769e-14,  5.50436773e-14],
#  [ 1.23217784e-12,  3.81853161e-13,  5.57113477e-13, -2.48107200e-12,
#    2.53337285e-12, -2.16288442e-15, -4.43228153e-14,  3.31722860e-14,
#    3.86098173e-14,  3.95304513e-14,  7.43187077e-14],
#  [ 1.19297458e-12,  3.69704032e-13,  5.39388224e-13, -2.40213363e-12,
#    2.45277046e-12, -1.66416492e-15, -3.41028275e-14,  2.55233955e-14,
#    2.97071368e-14,  3.04154903e-14,  5.71822446e-14],
#  [ 8.74756210e-13,  2.71087837e-13,  3.95509852e-13, -1.76137979e-12,
#    1.79850957e-12, -1.71885232e-15, -3.52235068e-14,  2.63621395e-14,
#    3.06833659e-14,  3.14149972e-14,  5.90613544e-14],
#  [ 1.04590442e-12,  3.24126840e-13,  4.72892329e-13, -2.10599809e-12,
#    2.15039240e-12, -1.64423119e-15, -3.36943365e-14,  2.52176708e-14,
#    2.93512984e-14,  3.00511671e-14,  5.64973035e-14],
#  [ 9.89461078e-13,  3.06634992e-13,  4.47372193e-13, -1.99234567e-12,
#    2.03434419e-12, -1.85983563e-15,-3.81126012e-14 , 2.85244088e-14,
#    3.32000699e-14,  3.39917109e-14,  6.39056712e-14],
#  [ 9.47363376e-13,  2.93588871e-13,  4.28338255e-13, -1.90757915e-12,
#    1.94779080e-12, -1.49389736e-15, -3.06136270e-14,  2.29119920e-14,
#    2.66676775e-14,  2.73035565e-14,  5.13316940e-14],
#  [ 1.27875288e-12,  3.96286815e-13,  5.78171789e-13, -2.57485395e-12,
#    2.62913172e-12, -1.86184104e-15, -3.81536969e-14,  2.85551659e-14,
#    3.32358686e-14,  3.40283632e-14,  6.39745789e-14]]
# )

# INITIAL_POPULATION = [OVERFIT_ERR]*NUM_CHROMOSOMES

NUM_GENERATIONS= 20

population= INITIAL_POPULATION

print(population.shape)

i= 0
while(input() != "NO"):
# for gen in range(NUM_GENERATIONS):
    print("Generation: " + str(i))

    fitness= get_fitness(population)

    print("Fitness: ", fitness)

    parents= mating_pool(population, fitness)

    offsprings_crossover= crossover(parents, offspring_size = (NUM_CHROMOSOMES - MATING_POOL_SIZE, NUM_GENES))

    offsprings= mutate_vector(offsprings_crossover)

    population[0: MATING_POOL_SIZE, : ] = parents[: , : 11]
    population[MATING_POOL_SIZE:, : ] = offsprings

    print("This: ")
    for i in population:
        print("[", end="")
        for j in i:
            print(j, end=", ")
        print("],")
    print("dim: ", population.shape)
    i += 1

print(population)
