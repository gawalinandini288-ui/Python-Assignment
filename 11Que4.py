def Reverse(No):
    Result = 0
    for digit in str(No):
        Result = int(digit) + Result * 10
    print("Revesred Number :",Result)
def main():
    No = int(input("Enter the Number :"))
    Reverse(No)
if __name__ == "__main__":
    main()