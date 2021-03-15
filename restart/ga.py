import numpy as np
from constants import *
import client as C
import random

def calculate_fitness(population):
    rows, cols = population.shape
    fitness = np.empty((rows, 3))

    for i in range(rows):
        # error = C.get_errors(SECRET_KEY, list(population[i]))
        error = [2662475751412.1533, 2386431631920.067]

        this_fit = error[0] + 0.7 * error[1] # 0: train, 1: val
        fitness[i] = [error[0], error[1], this_fit]
        # fitness[i] = np.random.randint(10)

    print(population.shape)
    print(fitness.shape)
    fit_pop = np.column_stack((population, fitness))

    # pop sorted by fitness in increasing order
    fit_pop = fit_pop[np.argsort(fit_pop[:, -1])]

    # shape of fit_pop: (NUM_POPULATION, NUM_GENES + 3)
    # The extra 3 per element = err_valid, err_train, fitness

    return fit_pop



def select_mating_pool(fit_pop):
    # gets the best MATING_POOL_SIZE number of elements for the mating pool
    mating_pool = fit_pop[:MATING_POOL_SIZE]

    return mating_pool



def crossover(parent_1, parent_2):
    child1 = np.empty(11)
    child2 = np.empty(11)

    u = random.random()
    n_c = 3

    # refer https://engineering.purdue.edu/~sudhoff/ee630/Lecture04.pdf

    if(u < 0.5):
        beta = (2*u)**(1/(n_c + 1))
    else:
        beta = (1/(2*(1-u)))**(1/(n_c + 1))

    child1 = 0.5*((1+beta)*parent_1 + (1-beta)*parent_2)
    child2 = 0.5*((1-beta)*parent_1 + (1+beta)*parent_2)

    return child1, child2



def mutate_child(child):
    for idx, val in enumerate(child):
        prob = random.uniform(0, 1)

        if(prob <= 0.6):
            if(val == 0):
                val += random.uniform(-1e-10, 1e-10)
            else:
                val += random.uniform(-0.5, 0.5)*val
        
        child[idx] = val
    return child




def create_offsprings(mating_pool):
    # removes valid, train, fit from the elements
    pool = mating_pool[:, :-3]
    children = []

    total_error = 0.0 

    for i in mating_pool[:MATING_POOL_SIZE]:
        total_error += i[-1]

    probs = []

    for i in mating_pool[:MATING_POOL_SIZE]:
        probs.append((total_error - i[-1]) /
                     (total_error*(MATING_POOL_SIZE-1)))

    crossover_elem = []
    mutate_elem = []

    for i in range(7):
        [parent_1,parent_2] = pool[np.random.choice(
            np.arange(0, MATING_POOL_SIZE), 2, replace=False, p=probs)]
        # parent_2 = pool[np.random.randint(MATING_POOL_SIZE)]

        crossover_elem.append(parent_1)
        crossover_elem.append(parent_2)

        child1, child2 = crossover(parent_1, parent_2)


        child1 = mutate_child(child1)
        child2 = mutate_child(child2)

        mutate_elem.append(child1)
        mutate_elem.append(child2)

        children.append(child1)
        children.append(child2)


    f.write("\nAfter Crossover: \n")

    for i in crossover_elem:
        write_file(i)


    f.write("\nAfter Mutation: \n")

    for i in mutate_elem:
        write_file(i)

    # print("\n Children:\n", children)
    return children


def create_gen(offsprings, fitness):

    fitness = fitness[:4]

    child_fitness = calculate_fitness(offsprings)

    new_pop = np.concatenate((fitness, child_fitness))

    # sort and get first NUM_POPULATION elements
    new_pop = new_pop[np.argsort(new_pop[:,-1])][:NUM_POPULATION]

    return new_pop



