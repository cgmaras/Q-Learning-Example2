import numpy as np
#import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
from getcriteria import Reward as rwd
import copy
from test_import import RL_4ass
import copy
import time
import ga
#import pandas as pd
dim=6
reward_options={'type': 'sum_new_linear',
'number_limit_criteria': 2,
'number_maximum_criteria': 1,
'L1': (1.48,1),
'L2': (2.1,1),
'M1': (1,1)}
fuel_types = list(range(2,dim+1))
s0 = np.random.randint(2,dim+1,4)
#s0 = np.array([2,4,4,2])                                 " best design"
options={"fuel_types": fuel_types,
         "initial_state": s0,
         "reward_options": reward_options}

#rl1 = RL_4ass(options)                                    " initial test only"


epochs=5
num_iterations = 5
epsilon = 1.0
EPS_DECAY = 0.9999

# rl1 = RL_4ass(options)
counter2 = 0
def rl_iter(rl,num_iterations, epsilon, RAND=False):
    best_reward = -np.inf
    best_state = None
    counter1 = 0
 #   np.random.seed(int(time.time()))
    #s0 = np.random.randint(2,dim+1,4)
    # print('Initial State')
    # print(s0)
    rl.impose_state(s0)
    for j in range(num_iterations):
        if(RAND):
            np.random.seed(int(time.time()))
            rl.impose_state(np.random.randint(2,dim+1,4))
        else:
            if(np.random.rand()> epsilon):
                rl.update_state(lr,dc)
            else:
                rl.update_state(lr,dc, True)

        print("New state: {} , New Reward: {}".format(rl1.get_state(), rl1.current_reward))
#        rewards.append(rl.current_reward)
        if rl.current_reward > best_reward :
            best_reward = rl.current_reward
            best_state = rl.get_state()
        counter1 += 1
        print(counter1)
        # print('Best State')
        # print(best_state)
        # print()
        # print('LP')
        # rl.simulate_submit(best_state)
    return((best_reward,best_state))

def ga_pwr(ass_dim,pop,pmat,ngen):
    sol_per_pop = pop
    num_parents_mating = pmat

    # Defining the population size.
    pop_size = (sol_per_pop,ass_dim) # The population will have sol_per_pop chromosome where each chromosome has num_weights genes.
    #Creating the initial population.
    new_population = np.random.randint(1,dim, size=pop_size)
#    print(new_population)

    num_generations = ngen

    for generation in range(num_generations):
   #    print("Generation : ", generation)
        # Measing the fitness of each chromosome in the population.
        fitness = ga.cal_pop_fitness(rl1, new_population);

        # Selecting the best parents in the population for mating.
        parents = ga.select_mating_pool(new_population, fitness,
                                          num_parents_mating);

        # Generating next generation using crossover.
        offspring_crossover = ga.crossover(parents,
                                           offspring_size=(pop_size[0]-parents.shape[0], ass_dim));

        # Adding some variations to the offsrping using mutation.
        offspring_mutation = ga.mutation(offspring_crossover,dim,ass_dim);

        # Creating the new population based on the parents and offspring.
        new_population[0:parents.shape[0], :] = parents  ;
        new_population[parents.shape[0]:, :] = offspring_mutation ;

        # The best result in the current iteration.
    #    print("Best result : ", np.max(np.sum(new_population*equation_inputs, axis=1)))

    # Getting the best solution after iterating finishing all generations.
    #At first, the fitness is calculated for each solution in the final generation.
    fitness = ga.cal_pop_fitness(rl1, new_population);
    # Then return the index of that solution corresponding to the best fitness.
    best_match_idx = np.where(fitness == np.max(fitness));
    res=np.max(fitness);
    return(res)

lr = 0.1
dc = 0.99
TEST=True
# rl1 = RL_4ass(options)
# rl = rl1
#rlt1 = RL_4ass(options)
#rlt2 = RL_4ass(options)
#rand_qtable1=copy.deepcopy(rlt1.qtable)
#rand_qtable2=copy.deepcopy(rlt2.qtable)
#rl2 = RL_4ass(options)

if(TEST):
    best_rewards=[]
    best_states=[]
    best_rewards_rand=[]
    best_states_rand=[]
    best_rewards_ga=[]
    for it in range(1):
        np.random.seed(int(time.time()))
        s0 = np.random.randint(2,dim+1,4)
        options={"fuel_types": fuel_types,
         "initial_state": s0,
         "reward_options": reward_options}
        rl1 = RL_4ass(options)
        rl = rl1
        print('after first set up')
        # rl2 = RL_4ass(options)
        # print('after 2nd set up')
        best_reward_opt = -np.inf
        best_state_opt = None
        epsilon = 0.
        # RL Optimized
        for i in range(epochs):
 #           print("******** EPOCH: {}".format(i))
            best_reward_ep, best_state_ep = rl_iter(rl1,num_iterations,epsilon)
 #           print("New state: {} , New Reward: {}".format(best_state_ep, best_reward_ep))
            if best_reward_ep > best_reward_opt :
                    best_reward_opt = best_reward_ep
                    best_state_opt = best_state_ep

            epsilon *=EPS_DECAY
            counter2 += 1
            print(counter2)
            print('Best State')
            print(best_state_opt)
            print()
            # print('LP')
            # rl.simulate_submit(best_state_opt)

        best_rewards.append(best_reward_opt)
        best_states.append(best_state_opt)
        # # Random
        # best_reward_rand = -np.inf
        # best_state_rand = None
        # for i in range(epochs):
        # #    print("******** EPOCH: {}".format(i))
        #     best_reward_ep, best_state_ep = rl_iter(rl2,num_iterations,epsilon,True)
        #     if best_reward_ep > best_reward_rand :
        #             best_reward_rand = best_reward_ep
        #             best_state_rand = best_state_ep
        # best_rewards_rand.append(best_reward_rand)
        # best_states_rand.append(best_state_rand)
        #
        # ga_reward=ga_pwr(4,10,6,50)
        # best_rewards_ga.append(ga_reward)
        # # GA Optimized

    print("RL Optimized: \n Reward --> mean: {} , standard deviation: {}".format(np.mean(best_rewards),np.std(best_rewards)))
    # print("Random: \n Reward --> mean: {} , standard deviation: {}".format(np.mean(best_rewards_rand),np.std(best_rewards_rand)))
    # print("GA: \n Reward --> mean: {} , standard deviation: {}".format(np.mean(best_rewards_ga),np.std(best_rewards_ga)))
    # dts=np.array([best_rewards, best_rewards_rand, best_rewards_ga])
    # dts = np.transpose(dts)
    # dts=pd.DataFrame(dts)
   # plt.hist(dts,histtype='step', stacked=False, fill=False, label=["RL", "RD", "GA"])
    # kwargs = dict(alpha=0.5, bins=10, stacked=False)
    # plt.hist(dts[0], **kwargs, color='b', label='RL')
    # plt.hist(dts[1], **kwargs, color='r', label='RS')
    # plt.hist(dts[2], **kwargs, color='g', label='GA')
    # plt.hist(dts[2], **kwargs, color='g', label='GA')
    # plt.xlabel('Reward');
    # plt.legend();
else:
    best_reward = -np.inf
    best_state = None
    np.random.seed(int(time.time()))
    s0 = np.random.randint(2,dim+1,4)
    rewards=[]
    options={"fuel_types": fuel_types,
     "initial_state": s0,
     "reward_options": reward_options}
    rl1 = RL_4ass(options)
    for i in range(epochs):

        best_reward_ep, best_state_ep = rl_iter(rl1,num_iterations,epsilon)

#            print("******** EPOCH: {}".format(i))
#            print("Best state: {} , New Reward: {}".format(best_state_ep, best_reward_ep))
        if best_reward_ep > best_reward :
                    best_reward = best_reward_ep
                    best_state = best_state_ep
        epsilon *=EPS_DECAY

    print("Best state: {} , New Reward: {}".format(best_state, best_reward))


print("Best State is: {} with reward: {}".format(best_state, best_reward))
