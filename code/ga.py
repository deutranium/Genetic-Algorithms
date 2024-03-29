import numpy as np
from constants import *
import client as C
import random

# calculate fitness with train factor
def calculate_fitness(population):
    rows, cols = population.shape
    fitness = np.empty((rows, 3))


    for i in range(rows):
        error = C.get_errors(SECRET_KEY, list(population[i]))

        # calculate fitness from errors
        this_fit = 0.7*error[0] + error[1] # 0: train, 1: val
        fitness[i] = [error[0], error[1], this_fit]

    # append each vector's fitness to its genes
    fit_pop = np.column_stack((population, fitness))

    # pop sorted by fitness in increasing order
    fit_pop = fit_pop[np.argsort(fit_pop[:, -1])]

    # shape of fit_pop: (NUM_POPULATION, NUM_GENES + 3)
    # The extra 3 per element = err_valid, err_train, fitness

    return fit_pop


# get the best vectors for the mating pool
def select_mating_pool(fit_pop):
    # gets the best MATING_POOL_SIZE number of elements for the mating pool
    mating_pool = fit_pop[:MATING_POOL_SIZE]

    return mating_pool


# use simulated binary crossover
def crossover(parent_1, parent_2):
    child1 = np.empty(11)
    child2 = np.empty(11)

    u = random.random()
    n_c = 2

    # refer https://engineering.purdue.edu/~sudhoff/ee630/Lecture04.pdf

    if(u < 0.5):
        beta = (2*u)**(1/(n_c + 1))
    else:
        beta = (1/(2*(1-u)))**(1/(n_c + 1))

    child1 = 0.5*((1+beta)*parent_1 + (1-beta)*parent_2)
    child2 = 0.5*((1-beta)*parent_1 + (1+beta)*parent_2)

    return child1, child2


# add mutations
def mutate_child(child):
    for idx, val in enumerate(child):
        prob = random.uniform(0, 1)


        if(prob <= 0.6):
            if val == 0:
                val += random.uniform(-1e-20, 1e-20)
            else:
                val += random.uniform(-0.7, 0.7)*val
        
        
        child[idx] = val
    return child



# create offsprings with crossover and mutation
def create_offsprings(mating_pool):
    # removes valid, train, fit from the elements
    pool = mating_pool[:, :-3]
    children = []


    # calculate total error of all the vectors
    total_error = 0.0 

    for i in mating_pool[:MATING_POOL_SIZE]:
        total_error += i[-1]

    probs = []
    parents_selected = []
    crossover_elem = []
    mutate_elem = []

    for i in mating_pool[:MATING_POOL_SIZE]:
        probs.append((total_error - i[-1]) /
                     (total_error*(MATING_POOL_SIZE-1)))


    for i in range(4):

        # select parents based on their probabilities
        [parent_1,parent_2] = pool[np.random.choice(
            np.arange(0, MATING_POOL_SIZE), 2, replace=False, p=probs)]

        parents_selected.append([parent_1, parent_2])

        # crossover to create children
        child1, child2 = crossover(parent_1, parent_2)

        # mutate children
        child1 = mutate_child(child1)
        child2 = mutate_child(child2)

        crossover_elem.append(child1)
        crossover_elem.append(child2)

        mutate_elem.append(child1)
        mutate_elem.append(child2)

        children.append(child1)
        children.append(child2)



    print("\nParents selected: \n")
    for i in parents_selected:
        print(i)

    print("\nAfter Crossover: \n")

    for i in crossover_elem:
        print(i)

    print("\nAfter Mutation: \n")

    for i in mutate_elem:
        print(i)

    return children


def create_gen(offsprings, fitness):

    # get the best 2 vectors from parent population
    fitness = fitness[:2]

    # get fitness for offsprings
    child_fitness = calculate_fitness(offsprings)

    new_pop = np.concatenate((fitness, child_fitness))

    np.random.shuffle(new_pop)

    # sort and get first NUM_POPULATION elements
    new_pop = new_pop[np.argsort(new_pop[:,-1])][:NUM_POPULATION]

    return new_pop



