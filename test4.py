from hill_climbing import *
from nqueen import NQueensState
from roulett_wheel import roulette_wheel_selection
from test import *
from test2 import *
from test3 import *






def forgot(population,fitnesses):
    good_fitnes =[]
    good_population =[]

    bad_fitnes =[]
    bad_population =[]

#number of population




    for i in range(4):
        selected_individual = roulette_wheel_selection(population, fitnesses)
        index_to_remove = population.index(selected_individual)
        bad_node  = population.pop(index_to_remove)
        bad_fit = fitnesses.pop(index_to_remove)
        bad_population.append(bad_node)
        bad_fitnes.append(bad_fit)
        good_population = population  
        good_fitnes = fitnesses

    for i in range(0,4,2):
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



        if random.random() < 1.0:

            random_index = random.randint(0, len(population) - 1)
            poped1 = population.pop(random_index)
            fitnesses.pop(random_index)

            ran = random.randint(0, len(bad_population) - 1)
            ran2 = random.randint(0, len(good_population) - 1)
            bad_good_child_queens = merge_arrays_replace_half(bad_population[ran].get_queens(),good_population[ran2].get_queens())
            bad_good_child = NQueensState(bad_good_child_queens)
            bad_good_child_fitness = bad_good_child.conflicts()
            population.append(bad_good_child)
            fitnesses.append(bad_good_child_fitness)




    random_index = random.randint(0, len(population) - 1)
    poped1 = population.pop(random_index)
    fitnesses.pop(random_index)
    state1_queens = shuffle_random_part(poped1.get_queens())
    state1 = NQueensState(state1_queens)
    population.append(state1)
    fitnesses.append(state1.conflicts())







    return population,fitnesses




population1 = []
fitnesses1 = []
for i in range(8):
    state = NQueensState.random_state(N=12)
    
    population1.append(state)
    fitnesses1.append(state.conflicts())







def append_if_not_exists(arr, element):
    if element not in arr:
        arr.append(element)


ans = []
count = 0
while True:
    count += 1
    print(len(ans))
    if len(ans) == 14200:
        print(ans)
        print('win')
        break




    for state in population1:
        i , y = hill_climbing_first_choice(state)
        if i.conflicts() == 0:
            append_if_not_exists(ans,i.get_queens())

    population1 , fitnesses1 = forgot(population1,fitnesses1)
    print(population1)




