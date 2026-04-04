import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler

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

    # There is no such a missing value in any column therefore no need to check the columns

    # Standard Scaling

    print(Border)

    X = df.drop("Outcome" , axis=1)
    Y = df["Outcome"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    print("Data gets scaled successfully")
    print(Border)

if __name__ == "__main__":
    main()
    


