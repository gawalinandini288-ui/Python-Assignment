from functools import reduce

Minimum = lambda A,B : A if A < B else B


def main():
    Data = [10,50,55,87]
    print("Actual data is :",Data)

    rData = reduce(Minimum,Data)
    print("Data after reduce is :",rData)
if __name__ == "__main__":
    main()