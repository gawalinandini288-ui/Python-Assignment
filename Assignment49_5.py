import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score , confusion_matrix , classification_report , ConfusionMatrixDisplay

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

    X_train , X_test , Y_train , Y_test = train_test_split(X_scaled , Y , test_size= 0.2 , random_state= 42)

    print("Data gets splited into the training and testing")

    print(Border)

    Model = LogisticRegression()

    Model.fit(X_train,Y_train)

    # Case study with KNN

    # Model = KNeighborsClassifier(n_neighbors=5)

    # Model.fit(X_train,Y_train)

    print("Model gets fit successfully")

    print(Border)

    Y_pred = Model.predict(X_test)

    print("Actaul Data is:\n",Y_test)
    print("Predicted Data :\n",Y_pred)

    print(Border)

    # Accuracy Score 

    Accuracy = accuracy_score(Y_pred,Y_test)
    print("Accuracy of model is :",Accuracy)

    Cm = confusion_matrix(Y_pred, Y_test)
    print("Confusion Matrix :\n",Cm)

    Cr = classification_report(Y_pred,Y_test)
    print("Classification Matrix :\n",Cr)

    print(Border)

    data = ConfusionMatrixDisplay(confusion_matrix=Cm,display_labels=Model.classes_)
    data.plot()
    plt.title("Confusion Matrix of diabetes dataset")
    plt.show()

if __name__ == "__main__":
    main()
    


