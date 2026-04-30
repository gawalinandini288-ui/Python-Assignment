import numpy as np
import math

def BCE(Actual_Y,Predicted_Y):

    n = len(Actual_Y)
    total_loss = 0

    for i in range(n):
        
        Y = Actual_Y[i]
        PR = Predicted_Y[i]

        p = max(min(PR,0.999),0.001)
        
        Loss = -(Y * math.log(p) + (1-Y) * math.log(1-p))
        total_loss += Loss 

    BCE = total_loss / n
    return BCE

def MSE(Actual_Y,Predicted_Y):

    n = len(Actual_Y)
    total_error = 0

    for i in range(n):
        Error = Actual_Y[i] - Predicted_Y[i]
        total_error += Error ** 2

    MSE = total_error / n
    return MSE


def main():

    Actual_Y = [10,20,30]
    Predicted_Y = [11,19,32]

    mse = MSE(Actual_Y,Predicted_Y)
    print("Mean Squared Error:",mse)

    bce = BCE(Actual_Y,Predicted_Y)
    print("Binary Class Entropy :",bce)

if __name__ == "__main__":
    main()