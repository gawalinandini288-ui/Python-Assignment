import numpy as pd
import matplotlib.pyplot as plt
import numpy as np

def Prediction():

    Experience = [1, 2, 3, 4, 5]
    Salary = [20000, 25000, 30000, 35000, 40000]
    
    print("Values of Independent Variables :",Experience)
    print("Values of Dependent Variables:",Salary)

    mean_Experience = np.mean(Experience)
    mean_Salary = np.mean(Salary)

    print("Mean of Experience :",mean_Experience)
    print("Mean of Salary :",mean_Salary)
    
    n = len(Experience)

    Numerator = 0
    Denominator = 0

    for i in range(n):
        Numerator = Numerator + ((Experience[i] - mean_Experience) * Salary[i] - mean_Salary)
        Denominator = Denominator + ((Experience[i] - mean_Experience) ** 2)

    m = Numerator / Denominator
    print("Slope of the line :",m)

    C = mean_Salary - (m * mean_Experience)
    print("Intercept of the line :",C)
    
    x = np.linspace(1,6,n)
    y = C + m*x

    Salary_Predicted =  m * x + C
    print("Predicted Salary :",Salary_Predicted)

    plt.plot(x,y , color = 'r' , label = 'Regression Line')
    plt.scatter(Experience,Salary , color = 'g' , label = "Scatter Plot")
    plt.scatter(Experience, Salary_Predicted , color = 'y' , label = "Predicted salary")

    plt.legend()
    plt.show()

def main():

    Prediction()

if __name__ == "__main__":
    main()
