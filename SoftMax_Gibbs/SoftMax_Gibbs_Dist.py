import pandas as pd
import numpy as np
import random as rd
import matplotlib.pyplot as plt
#def gibbsDist(temperature):

#def e_greedy(greedyList):

def evalNBandit(epsChance):
    #action List: max action = 10, min = 1 [1-10]
    randArr = [[rd.randint(1,10) for i in range(10)] for j in range(2000)]
    #rand array is now setup
    #for i in range(0,len(randArr)):
        #for j in range(0,len(randArr[i])):
            #print("hi")
    s = np.random.normal() #mean , variance, size
def main():
    # myData = pd.DataFrame([1,2,3,4,56,7])
    # myData2 = pd.DataFrame([12,345,5,3,2,3,4])
    # myData3 = pd.DataFrame([12,34,5,34,5,34,3,63])
    # ax = myData.plot()
    # myData2.plot(ax=ax)
    # myData3.plot(ax=ax)
    # plt.show()
    evalNBandit(1)
    #eval bandit is to test ML n-bandit problem - Check Sutton's book
if __name__ == "__main__":
    main()
