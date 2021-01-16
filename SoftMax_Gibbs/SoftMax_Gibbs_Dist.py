import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
import numpy as np
#def gibbsDist(temperature):

#def e_greedy(greedyList):

def evalNBandit(epsChance):
    #action List: max action = 10, min = 1 [1-10]
    total_turns = 5000;
    num_slots = 10;

    ##for each slot how many wins does it incur? how many LOSSES does it incur? ->
    num_wins = np.zeros(num_slots);
    num_lost = np.zeros(num_slots);
    total_reward = np.zeros(total_turns);

    np.random.normal(0,1,20);

    conversions = np.random.uniform(0.01, .3, num_slots);
    convTable = np.zeros((total_turns, num_slots));
    for turn_index in range(0, total_turns):
        for slot_index in range(num_slots):
            if(np.random.rand() <= conversions[slot_index]):
                convTable[turn_index][slot_index] = 1;

    #print(convTable[0:15, 0:10]);
    #Begin Simulation of e-greedy methods // on each play we must add reward to our array, then just return array
    #The array we return is
    incuredRewards = 0
    for turn_pos in range(turn_index):
        machine_index_played = -1
        max_reward = -1
        if (np.random.random() < 1 - epsChance):
            for slot_machine in range(num_slots):
                a = num_wins[slot_machine]+1
                b = num_lost[slot_machine]+1

                random_reward = np.random.beta(a, b)
                if(random_reward > max_reward):
                    max_reward = random_reward
                    machine_index_played = slot_machine

            #now we play the slot machine IF its within epsilon, otherwise we play a random one
                if (convTable[turn_pos][machine_index_played] == 1):
                    incuredRewards+=1;
                    num_wins[machine_index_played]+=1;
                else:
                    num_lost[machine_index_played]+=1;
        else: #play a random machine
            random_machine_played = np.random.randint(0,10)
            if (convTable[turn_pos][random_machine_played] == 1):
                num_wins[random_machine_played]+=1;
                incuredRewards+=1
            else:
                num_lost[random_machine_played]+=1;
        ##turn End : gather points
        total_reward[turn_pos] = incuredRewards/(turn_pos+1);
    return total_reward


def main():
    # myData = pd.DataFrame([1,2,3,4,56,7])
    # myData2 = pd.DataFrame([12,345,5,3,2,3,4])
    # myData3 = pd.DataFrame([12,34,5,34,5,34,3,63])
    # ax = myData.plot()
    # myData2.plot(ax=ax)
    # myData3.plot(ax=ax)
    # plt.show()
    #eval bandit is to test ML n-bandit problem - Check Sutton's book A-
    noExplore = evalNBandit(0.0)
    tenPercentExplore = evalNBandit(.001)  # episilon of 1%
    displayNAB = pd.DataFrame({'e = 1%' : tenPercentExplore, 'e = 0 (greedy)' : noExplore})
    ax = displayNAB.plot()
    plt.show()
if __name__ == "__main__":
    main()
