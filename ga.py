import client as C

import numpy as np

import random

#### CONSTANTS ####
OVERFIT_ERR = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -
    1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]
NUM_GENES = 11

KEY = 'PRz8goBaZsoe41TSChLpab9dgyEXThblG2pE44gE2Ia5nqMJGv'

NUM_CHROMOSOMES = 10
POPULATION_SIZE = (NUM_CHROMOSOMES, NUM_GENES)
MATING_POOL_SIZE = 8


def get_fitness(population):
    fitness_arr = np.zeros(NUM_CHROMOSOMES)
    for i in range(NUM_CHROMOSOMES):
        # print(population[i])

        # print(population[i, :])

        err = C.get_errors(KEY, list(population[i, :]))
        # err = [2662475751412.1533, 2386431631920.067]
        # err = [np.random.randint(10), np.random.randint(10)]
        print("err: ", err)

        fitness_arr[i] = 0.7*err[0] + err[1]
    return fitness_arr

# def mating_pool(population, fitness):
#     arr = np.concatenate((population, fitness), axis = 1)
#     arr = arr[np.argsort(arr[:, NUM_GENES])]

#     print("arr:")
#     print(arr)

#     prob = np.arange(1.0, NUM_CHROMOSOMES + 1, 1.0)

#     prob = np.reciprocal(prob)
#     prob = prob/np.sum(prob)

#     print("prob: ")
#     print(prob)

#     pool = arr[np.random.choice(
#         NUM_CHROMOSOMES, size=MATING_POOL_SIZE, replace=False, p = prob
#     )]

#     print("pool: ")
#     print(pool)

#     # print("Pool: ", pool)
#     return(pool)


def mating_pool(population, fitness):
    parents = np.empty((NUM_CHROMOSOMES, population.shape[1]))

    # print("BAD: ")
    # print(population)

    for i in range(NUM_CHROMOSOMES):
        max_fitness_idx = np.where(fitness == np.max(fitness))

        max_fitness_idx = max_fitness_idx[0][0]
        parents[i, :] = population[max_fitness_idx, :]

        fitness[max_fitness_idx] = -999999999

    # print("GOOD")
    # print(parents)
    return parents

# single point crossover


def crossover(parents, offspring_size):
    offsprings = np.empty(offspring_size)

    crossover_point = np.uint8(offspring_size[1]/2)

    for i in range(offspring_size[0]):
        parent_1 = i % parents.shape[0]
        parent_2 = (i+1) % parents.shape[0]

        offsprings[i, 0:crossover_point] = parents[parent_1, 0:crossover_point]
        print(offsprings[i, crossover_point:])
        print(parents[parent_2, crossover_point:])
        offsprings[i, crossover_point:] = parents[parent_2, crossover_point:]
        # offsprings[i, 0: ] = np.divide((np.multiply(parents[parent_1,0: ],parent_2+1)  +  np.multiply(parents[parent_1, 0:],parent_1+1)),parent_1+parent_2+2)[0:11]

    return offsprings


def mutate_vector(arr):
    arr2 = arr.copy()
    # print(arr.shape)
    # print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    # print(arr)
    # print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA')
    for i,val in enumerate(arr):
        # print(i)
        for j,val2 in enumerate(val):
            # print('NNADSIOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO')
            # print(j)
            # print('asiduhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh')
            # j += random.uniform(-0.25, 0.25)*j
            arr2[i][j] = random.uniform(-0.25, 0.25)*val2 + val2
            if val2 == 0:
                arr2[i][j] = random.uniform(-0.0000000001, 0.0000000001)
            # print(j)
        # print(arr2[i])
    # print(arr2)
    return arr2