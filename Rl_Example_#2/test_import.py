import numpy as np
import pickle
from matplotlib import style
import time
from getcriteria import Reward as rwd
import copy
import os
import shutil

class RL_4ass(object):
    """
    Object for reinforcement learning
    """
    def __init__(self,options):
        self.ftypes = options["fuel_types"]
        self.state = (0,0,0,0)
        self.reward = 0
        self.fsize = len(self.ftypes)
        self.criteria = [0, 0, 0]
        self.rwd = rwd(options["reward_options"])
        self.impose_state(options["initial_state"])
        self.qtable = self.init_qtable()


    def reward_calc(self):
        """
        Converts the state values to the qtable indices
            - state is an array of fuel types configuration
            - the state is returned as a tuple
        """
        #ith open("C:/Users/Cameron/Documents/Python tests/RLsim_Code/Output_Search.py", "r") as output_file:
        qoi = self.rwd.get_criteria()
        print(qoi)
        return(qoi)

    def init_qtable(self):
        """
        Initialization of the qtable to random initial values
        """
        qt={}
        for i in range(self.fsize):
            for ii in range(self.fsize):
                for iii in range(self.fsize):
                        for iiii in range(self.fsize):
                            qt[(i,ii,iii,iiii)] = np.reshape([np.random.uniform(-1,0 ) for j in range(self.fsize*4)], (self.fsize,4))
                            qt[(i,ii,iii,iiii)][i,0] = -np.inf
                            qt[(i,ii,iii,iiii)][ii,1] = -np.inf
                            qt[(i,ii,iii,iiii)][iii,2] = -np.inf
                            qt[(i,ii,iii,iiii)][iiii,3] = -np.inf
        return(qt)

    def get_state(self):
        """
        Returns the state of the class
            - the state is returned as a tuple
        """
        state=np.array(self.state)
        return(tuple(state+2))

    def get_simState(self):
        """
        Gets state from last SIMULATE run

        """
        from user_input import State4
        object = State4()
        state   = object.State4
        #self.state = self.state_converter(state)
        return(state)

    def state_converter(self, state):
        """
        Converts the state values to the qtable indices
            - state is an array of fuel types configuration
            - the state is returned as a tuple
        """
        return(tuple(state -2))

    def impose_state(self,state):
        """
        Imposes a desired state and updates the current reward
            - state is an array of fuel types configuration
        """
        try:
            shutil.rmtree('/home/cgmaras/Python/CameronRL/Queue')
        except OSError as e:
            print ("Error: didnt delete queue")
        try:
            shutil.rmtree('/home/cgmaras/Python/CameronRL/SimRuns')
        except OSError as e:
            print ("Error: didnt delete SimRuns")

        self.state = self.state_converter(state)
        self.simulate_submit(state)
        self.criteria = self.rwd.get_criteria()
        os.chdir('/home/cgmaras/Python/CameronRL/')
        self.current_reward= self.rwd.evaluate(self.criteria)

    def action(self,state):
        """
        Finds the indices for the maximum of the qtable indicating the action
            - state is a tuple of indices
            - the action is return as a list of two indices: act[0] is the
            fuel type to be used and act[1] the location
        """
        Qsel=self.qtable[state]
        act = list(np.unravel_index(np.argmax(Qsel),Qsel.shape))
        return(act)


    def get_qvalue(self,s,a):
        """
        Returns the qvalue for a specific state and action
            - s is the state as a tuple
            - a is the action as a list of size 2
        """
        return(self.qtable[s][a[0],a[1]])

    def load_qtable(self,qt):
        """
        Loads a saved qtable
            - s is the state as a tuple
            - a is the action as a list of size 2
        """
        self.qtable = copy.deepcopy(qt)

    def simulate_submit(self,state):
        """
        Takes current action and performs SIMULATE run
            - current_action action found for current state
        First, it updates user_input with new LP current_action

        Second, it runs main2.py to submit SIMULATE job to cluster
        """
        import user_input
        from user_input import LoadingPattern

        LoadingPattern[0][0] = state[0]
        LoadingPattern[0][1] = state[1]
        LoadingPattern[1][0] = state[2]
        LoadingPattern[1][1] = state[3]
        print("Current working directory is:", os.getcwd())
        with open("user_input.py","r") as f:
            lines = f.readlines()

        with open("user_input.py","w") as f:
            for i in range(len(lines)):
                if i <= 42:
                    lines[i] = lines[i].rstrip()
                    if lines[i].startswith('LoadingPattern'):
                        #f.write(('LoadingPattern = '+ l.split(',') for l in ','.join(test).split(', [')))
                        f.write('LoadingPattern = [' + str(LoadingPattern[0]) + ', \n')
                        length = len(LoadingPattern)-1
                        counter = 0
                        for item in LoadingPattern[1:]:
                            counter += 1
                            if counter == length:
                                f.write('                  ' + str(item) + '] \n')
                            else:
                                f.write('                  ' + str(item) + ', \n')

                            #     f.write('LoadingPattern = '+"%s\n" % item)
                            #     f.write("%s\n" % item)

                    else:
                        f.writelines(lines[i] + '\n')

            for i in range(51, len(lines), 1):
                f.writelines(lines[i])

        import main2
        from main2 import submit2
        submit2()

    def update_state(self,lr,dc,RAND=False):
        """
        It performs the RL policy by updating the state based on an action
            - lr is the LEARNING_RATE
            - dc is the DISCOUNT
            - RAND True if a random update is to be performed

        First, the action is selected by taking the maximum of the qtable
        for the current state.

        Second, the state is updated and the reward is calculated

        Third, the current qvalue before the action and the maximum future
        qvalue after the action are computed and combined with the reward to
        calculate the new qvalue for the initial state and action.
        """

        current_state = copy.deepcopy(self.state)
        if RAND:
            current_q = -np.inf
            while current_q==-np.inf:
                current_act = [np.random.randint(0,self.fsize),np.random.randint(0,4)]
                current_q = self.get_qvalue(current_state,current_act)

        else:
            current_act = self.action(current_state)
        current_q = self.get_qvalue(current_state,current_act)


        new_state = list(self.state)
        new_state[current_act[1]] = current_act[0]
        self.impose_state(np.array(new_state)+2)

        new_act = self.action(self.state)
        max_future_q = self.get_qvalue(self.state,new_act)
        qvalue_update = (1 - lr) * current_q + lr * (self.current_reward + dc * max_future_q)
        self.update_qtable(current_state,current_act,qvalue_update)


    def get_qstate(self):
        """
        Returns the q values for the current state
        """
        return(self.qtable[self.state])

    def update_qtable(self,state,action,value):
        """
        Updates the qvalue for a specific state and action
            - state the tuple of state indices
            - action the list of the selected action
            - value the new value of the qvalue
        """
        self.qtable[state][action[0],action[1]]=value

# ob = RL_4ass()
# x = ob.get_simState()
# print(x)
