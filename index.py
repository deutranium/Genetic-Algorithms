import client as C

import numpy as np

#### CONSTANTS ####
original_vector = [0.0, -1.45799022e-12, -2.28980078e-13,  4.62010753e-11, -1.75214813e-10, -1.83669770e-15,  8.52944060e-16,  2.29423303e-05, -2.04721003e-06, -1.59792834e-08,  9.98214034e-10]
num_vectors = 10
vector_length = 11

population_size = 40

# generate the population
for i in range(population_size):
    temp = np.copy(original_vector)


def mutate(vector, index = -1, prob_mut = 0.1):

    # Changes to be made at the index position

    # Choose a random index if none provided
    if index == -1:
        index = np.random.randint(9, vector_length)

