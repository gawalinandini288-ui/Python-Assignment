import numpy as np 
from sklearn.metrics import r2_score

def Prediction():

    X = [1, 2, 3, 4, 5]
    Y = [3, 4, 2, 4, 5]

    print("Values of Independent Variables X -",X)
    print("Values of Dependent Variables Y -",Y)

    mean_X = np.mean(X)
    mean_Y = np.mean(Y)

    print("Mean of X :",mean_X)
    print("Mean of Y :",mean_Y)

    n = len(X)

    Numerator = 0
    Denominator = 0

    for i in range(n):
        Numerator = Numerator + ((X[i] - mean_X) * (Y[i] - mean_Y))
        Denominator = Denominator + ((X[i] - mean_X) ** 2)

    m = Numerator / Denominator
    print("Slope of line is :",m)

    C = mean_Y - (m * mean_X)
    print("Intercept of line is :",C)

    x = np.linspace(1,6,n)
    y = C + m * x 
    
    Yp = m * x + C
    print("Predicted Y is :",Yp)

    r2 = r2_score(Y , Yp)
    print("R square is :",r2)

def main():

    Prediction()

if __name__ == "__main__":
    main()
