def Odd(No):
    for i in range(1,No+1,2):
        print(i,end=" ")
def main():
    No = int(input("Enter thr number"))
    Odd(No)
if __name__ == "__main__":
    main()