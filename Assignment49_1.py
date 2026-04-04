import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def main():
    
    
    Border = "=" * 70
    print(Border)

    df = pd.read_csv("diabetes.csv")
    print(df.head())

    print(Border)

    print("\nColumn info :")
    print(df.info())

    print(Border)

    print("\nMissing values in each column :")
    print(df.isnull().sum())

    print(Border)

    print(df.describe())

    
    sns.countplot(x= "Outcome",data= df)
    plt.title("Distribution of diabetes")
    plt.show()

    sns.boxplot(x= "Outcome" , y = "Glucose",data=df)
    plt.show()

if __name__ == "__main__":
    main()
    


