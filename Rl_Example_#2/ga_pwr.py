import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
from reward import Reward as rwd
import random
import ga
from RL4Ass import RL_4ass

ass_dim=4
ass_type_dim = 6
reward_options={'type': 'sum_new_linear',
'number_limit_criteria': 3,
'number_maximum_criteria': 1,
'L1': (2,1),
'L2': (2,1),
'L3': (2,1),
'M1': (6,10)}
s0 = np.random.randint(1,ass_type_dim+1, size=ass_dim)
fuel_types = list(range(1,ass_type_dim+1))
options={"fuel_types": fuel_types,
         "initial_state": s0,
         "reward_options": reward_options}
rl1 = RL_4ass(options)

sol_per_pop = 10
num_parents_mating = 6

# Defining the population size.
pop_size = (sol_per_pop,ass_dim) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
#Creating the initial population.
new_population = np.random.randint(1,ass_type_dim, size=pop_size)
print(new_population)

num_generations = 20

for generation in range(num_generations):
    print("Generation : ", generation)
    # Measing the fitness of each chromosome in the population.
    fitness = ga.cal_pop_fitness(rl1, new_population)

    # Selecting the best parents in the population for mating.
    parents = ga.select_mating_pool(new_population, fitness,
                                      num_parents_mating)

    # Generating next generation using crossover.
    offspring_crossover = ga.crossover(parents,
                                       offspring_size=(pop_size[0]-parents.shape[0], ass_dim))

    # Adding some variations to the offsrping using mutation.
    offspring_mutation = ga.mutation(offspring_crossover,ass_type_dim,ass_dim)

    # Creating the new population based on the parents and offspring.
    new_population[0:parents.shape[0], :] = parents
    new_population[parents.shape[0]:, :] = offspring_mutation

    # The best result in the current iteration.
#    print("Best result : ", np.max(np.sum(new_population*equation_inputs, axis=1)))

# Getting the best solution after iterating finishing all generations.
#At first, the fitness is calculated for each solution in the final generation.
fitness = ga.cal_pop_fitness(rl1, new_population)
# Then return the index of that solution corresponding to the best fitness.
best_match_idx = np.where(fitness == np.max(fitness))

print("Best solution : ", new_population[best_match_idx, :])
print("Best solution fitness : ", fitness[best_match_idx])
