from constants import *
from ga import *

population = np.array([np.copy(OVERFIT_ERR) for i in range(NUM_POPULATION)])

# add variation to overfit vector
for idx in range(NUM_POPULATION):
    prob = random.random()
    if(prob <= 0.63): # 7/11
        gene_id = np.random.randint(NUM_GENES)
        population[idx][gene_id] = 0

    population[idx] = mutate_child(population[idx])


fitness = calculate_fitness(population)
# [......., val, train, fitness]


count = 1

print("INITIAL POPULATION")

for i in fitness:
    print("[ ", end="")
    for j in i[:-3]:
        print(j, end=", ")
    print("]")
print()

while(input() != "NO"):

    print("\n\n------------------------------\n")
    print("Generation " + str(count) + "\n")
    print("\nFitness: \n")
    
    for i in fitness:
        print(i[-3:])
    
    # select the mating pool
    mating_pool = select_mating_pool(fitness)

    print("\nAfter Selection: \n")
    for i in mating_pool:
        print(i[:-3])

    # Create offsprings with crossover and mutation
    offsprings = create_offsprings(mating_pool)

    # create generation
    new_gen = create_gen(np.array(offsprings), fitness)

    # update population and fitness with the new generation
    fitness = new_gen
    population = new_gen[:,:-3]

    print("\n New Generation:\n")

    for i in new_gen:
        print("[ ", end="")
        for j in i[:-3]:
            print(j, end=", ")
        print("]")
    print()

    print()
    count += 1

f.close()
