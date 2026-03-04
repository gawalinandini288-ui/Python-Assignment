import math
   
def EucDistance(P1 , P2):
    Ans = math.sqrt((P1['Study Hours'] - P2['Study Hours']) ** 2 + (P1['Attendance'] - P2['Attendance']) **2)
    return Ans 

def StudentKNeighborsClaasifier():
    
    Border = "-" * 40

    Data = [
             {'Study Hours' : 2, 'Attendance' : 60, 'Result' : 'Fail'},
             {'Study Hours' : 5, 'Attendance' : 80, 'Result' : 'Pass'},
             {'Study Hours' : 6, 'Attendance' : 85, 'Result' : 'Pass'},
             {'Study Hours' : 1, 'Attendance' : 50, 'Result' : 'Fail'}
           ]

    print(Border)
    print("Student Pass / Fail KNN")
    print(Border)

    print(Border)
    print("Testing the data")
    print(Border)

    for i in Data:
        print(i)

   

    Study_Hours = int(input("Enter the hours of study :"))
    Attendance = int(input("Enter the attendance of student :"))

    New_Data = {'Study Hours' : Study_Hours , 
                'Attendance' : Attendance}

    for d in Data:
        d['distance'] = EucDistance(d,New_Data)
    
    print(Border)
    print("Calculated distances are :")
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
        Result = neighbour['Result']
        Votes[Result] = Votes.get(Result , 0) + 1

    print(Border)
    print("Final Voting :")
    print(Border)

    for d in Votes:
        print('Name :' , d ,"Number of votes :" ,Votes[d])
    print(Border)

    predicted_output = max(Votes , key = Votes.get)

    print("Predicted output pass / fail :" , predicted_output)

def main():

    StudentKNeighborsClaasifier()

if __name__ == "__main__":
    main()   