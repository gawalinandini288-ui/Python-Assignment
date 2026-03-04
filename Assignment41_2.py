# [A , B, C, D]
# X[1, 2, 3, 6]
# Y[2, 3, 1, 5]
# [R, R, B, B]

import numpy as np
import math

def EucDistance(P1 , P2):
    Ans = math.sqrt((P1['X'] - P2['X']) ** 2 + (P1['Y'] - P2['Y']) ** 2)
    return Ans 

def AssignmentKNeighborsClassifier():

    Border = "-" * 40

    Data = [
             {'Point' : 'A', 'X' : 1, 'Y' : 2, 'label' : 'Red' },
             {'Point' : 'B', 'X' : 2, 'Y' : 3, 'label' : 'Red' },
             {'Point' : 'B', 'X' : 1, 'Y' : 1, 'label' : 'Blue' },
             {'Point' : 'B', 'X' : 6, 'Y' : 5, 'label' : 'Blue' }
    ]               

    print(Border)
    print("Assignment Userdefined KNN")
    print(Border)

    print(Border)
    print("Testing the data")
    print(Data)

    for i in Data:
        print(i)

    print(Border)
    
    New = {}
    New['X'] = int(input("Enter the new X coordinate :"))
    New['Y'] = int(input("Enter the new Y coordinate :"))    

    for d in Data:
        d['distance'] = EucDistance(d, New)

    print(Border)
    print("Calculated Distances are :")
    print(Border)

    for d in Data:
        print(d)

    Sorted_Data = sorted(Data , key = lambda item : item['distance'])
   
    print(Border)
    print("Sorted Data is :")
    print(Border)

    for d in Sorted_Data:
        print(d)

    k = int(input("Enter the Value of K"))
    nearest = Sorted_Data[:k]


    
    print(Border)
    print("Nearest three elements are :")
    print(Border)

    for d in nearest:
        print(d)

    Votes = {}

    for neighbour in nearest:
        label = neighbour['label']
        Votes[label] = Votes.get(label , 0) + 1

    print(Border)
    print("Final Voting :")
    print(Border)

    for d in Votes:
        print('Name :' , d ,"Number of votes :" ,Votes[d])
    print(Border)

    predicted_output = max(Votes , key = Votes.get)

    print("Predicted output of given coordinates :" , predicted_output)

def main():

   
    AssignmentKNeighborsClassifier()

if __name__ == "__main__":
        main()