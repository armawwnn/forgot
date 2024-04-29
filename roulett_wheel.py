import random

def roulette_wheel_selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    selected = None
    #selected = []
    #for _ in range(1):
    pick = random.uniform(0, total_fitness)
    current = 0
    for ind, fitness in zip(population, fitnesses):
        current += fitness
        if current > pick:
            selected = ind
            break
    if selected is None:
            random_index = random.randint(0, len(population) - 1)
            selected = population[random_index]


    return selected


