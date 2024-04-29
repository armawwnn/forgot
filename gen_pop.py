from nqueen import NQueensState
from roulett_wheel import roulette_wheel_selection
import random
from test import *
from test2 import *
from collections import Counter
population =[]
fitnesses =[]


for i in range(20):
    state = NQueensState.random_state(N=8)
    
    population.append(state)
    fitnesses.append(state.conflicts())


# forgot 10 node totlay
def forgot():
    if 0 in fitnesses:
        return True
    good_fitnes =[]
    good_population =[]

    bad_fitnes =[]
    bad_population =[]

#number of population
    for i in range(10):
        selected_individual = roulette_wheel_selection(population, fitnesses)
        index_to_remove = population.index(selected_individual)
        bad_node  = population.pop(index_to_remove)
        bad_fit = fitnesses.pop(index_to_remove)
        bad_population.append(bad_node)
        bad_fitnes.append(bad_fit)
        good_population = population  
        good_fitnes = fitnesses

    for i in range(0,10,2):
        good_child_queens = merge_arrays_replace_half(good_population[i].get_queens(),good_population[i+1].get_queens())
        good_child = NQueensState(good_child_queens)
        good_child_fitnes = good_child.conflicts()
        population.append(good_child)
        fitnesses.append(good_child_fitnes)


        bad_child_queens = merge_arrays_replace_half(bad_population[i].get_queens(),bad_population[i+1].get_queens())
        bad_child = NQueensState(bad_child_queens)
        bad_child_fitnes = bad_child.conflicts()
        population.append(bad_child)
        fitnesses.append(bad_child_fitnes)

    random_index = random.randint(0, len(population) - 1)
    population.pop(random_index)
    fitnesses.pop(random_index)
    state1 = NQueensState.random_state(N=8)
    population.append(state1)
    fitnesses.append(state1.conflicts())


    random_index = random.randint(0, len(population) - 1)
    population.pop(random_index)
    fitnesses.pop(random_index)
    state1 = NQueensState.random_state(N=8)
    population.append(state1)
    fitnesses.append(state1.conflicts())



    random_index = random.randint(0, len(population) - 1)
    population.pop(random_index)
    fitnesses.pop(random_index)
    state1 = NQueensState.random_state(N=8)
    population.append(state1)
    fitnesses.append(state1.conflicts())




for i in range(20):
    print(fitnesses)

    boo = bool()
    boo = forgot()
    if boo == True:
        print('win')
        break










