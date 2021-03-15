from constants import *
from ga import *

population = INITIAL_POPULATION

fitness = calculate_fitness(population)

# [......., val, train, fitness]

# (20,14)

count = 0

while(input() != "NO"):

    print("Generation: ", count)
    
    print("\nThis:")

    for i in fitness:
        print("[", end = " ")
        for j in i[:-3]:
            print(j, end=", ")
        print("],")

    print("\nFitness: ")
    
    for i in fitness:
        print("[", end = " ")
        for j in i[-3:]:
            print(j, end=", ")
        print("],")
    
    # print(population.shape)
    # print(fitness.shape)
    
    mating_pool = select_mating_pool(fitness)
    # print("Mating Pool: ")
    # print(mating_pool)

    offsprings = create_offsprings(mating_pool)
    # print("Offsprings: ", offsprings)

    new_gen = create_gen(offsprings, fitness)

    fitness = new_gen
    population = new_gen[:,:-3]

    print()
    count += 1
    # print(population.shape)

