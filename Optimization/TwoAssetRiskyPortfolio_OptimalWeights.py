# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
### Optimal portfolio 2 risky assets
def optimal_weights(ret1,ret2,rf,sd1,sd2,corr):
    cov_12 = sd1*sd2*corr
    excess_r1 = ret1 - rf
    excess_r2 = ret2 - rf
    num = (sd2**2)*excess_r1 - cov_12*excess_r2
    denom = (sd2**2)*excess_r1 + (sd1**2)*excess_r2 - cov_12*(excess_r1+excess_r2)
    w1 = num/denom
    sigma_p = ((w1**2)*(sd1**2) + ((1-w1)**2)*(sd2**2) + 2*cov_12*w1*(1-w1))**0.5
    sr = (excess_r1*w1 + excess_r2*(1-w1))/sigma_p
    return w1,1-w1,sr
def sharpe_ratio(ret1,ret2,rf,sd1,sd2,corr,w1):
    cov_12 = sd1*sd2*corr
    excess_r1 = ret1 - rf
    excess_r2 = ret2 - rf
    sigma_p = ((w1**2)*(sd1**2) + ((1-w1)**2)*(sd2**2) + 2*cov_12*w1*(1-w1))**0.5
    sr = (excess_r1*w1 + excess_r2*(1-w1))/sigma_p
    return sr
def plot(w_array,sr_array,w1):
    plt.plot(w_array, sr_array,w1)
    plt.xlabel("Weights")
    plt.ylabel("Sharpe Ratio")
    plt.title("Sharpe Ratio vs W1")
    plt.axvline(w1, linestyle='dashed', color='r')
    plt.show()
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    ### Find optimal weights of 2 asset risky portfolio
    ret1 = 0.03
    ret2 = 0.0
    rf = 0.0
    sd1 = 0.1
    sd2 = 0.1
    corr = -0.5
    w1,w2,sr = optimal_weights(ret1, ret2, rf, sd1, sd2, corr)
    ### Plot optimal weights vs Sharpe Ratio
    w_array = np.linspace(0, 1, 100)
    sr_array = []
    for w in w_array:
        sr_array.append(sharpe_ratio(ret1, ret2, rf, sd1, sd2, corr, w))
    plot(w_array, sr_array,w1)
