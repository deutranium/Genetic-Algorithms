import client as C

import numpy as np

#### CONSTANTS ####
OVERFIT_ERR = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]
NUM_GENES = 11

KEY = '81WmrH1dHrlpZ3Qj2RF4HRr9Qv8gRke6SmF2zNLjHJ3v6wzIYE'

NUM_CHROMOSOMES = 20
POPULATION_SIZE = (NUM_CHROMOSOMES, NUM_GENES)
MATING_POOL_SIZE = 8



def get_fitness(population):
    fitness_arr = np.zeros((NUM_CHROMOSOMES, 1))
    for i in range(NUM_CHROMOSOMES):
        # print(population[i])

        print(population[i, :])

        # err = C.get_errors(KEY, list(population[i, :]))
        err = [2662475751412.1533, 2386431631920.067]
        print("err: ", err)

        fitness_arr[i] = 0.7*err[0] + err[1]
    return fitness_arr

def mating_pool(population, fitness):
    arr = np.concatenate((population, fitness), axis = 1)
    arr = arr[np.argsort(arr[:, NUM_GENES])]
    # print("!!!!!!!!!", population.shape)
    # print("!!!!!!!!!", fitness.shape)
    # print("!!!!!!!!!", arr.shape)
    # print("!!!!!!!!!", arr)

    prob = np.arange(1.0, NUM_CHROMOSOMES + 1, 1.0)

    prob = np.reciprocal(prob)
    prob = prob/np.sum(prob)

    pool = arr[np.random.choice(
        NUM_CHROMOSOMES, size=MATING_POOL_SIZE, replace=False, p = prob
    )]

    # print("Pool: ", pool)
    return(pool)


# single point crossover
def crossover(parents, offspring_size):
    offsprings = np.empty(offspring_size)

    crossover_point = np.uint8(offspring_size[1]/2)
    # print("blah: ", crossover_point)
    # print("abcd ", offspring_size)
    # print("fml: ", parents.shape)

    for i in range(offspring_size[0]):
        parent_1 = i % parents.shape[0]
        parent_2 = (i+1) % parents.shape[0]
        # print("1: ", parent_1)
        # print("2: ", parent_2)

        # print("parents: ", parents.shape)
        # print("offspring: ", offsprings.shape)

        offsprings[i, 0:crossover_point] = parents[parent_1, 0:crossover_point]
        # print("11: ", parents[parent_1, 0:crossover_point].shape)
        # print("21: ", parents[parent_2, crossover_point:].shape)
        # print("o: ", offsprings)
        offsprings[i, crossover_point:] = parents[parent_2, crossover_point: -1]

    return offsprings

def mutate_vector(arr):

    # random_arr = np.random.uniform(-1.0, 1.0, arr.shape)
    # arr += random_arr
    for i in arr:
        i += np.random.uniform(-0.25, 0.25)*i
    return arr
