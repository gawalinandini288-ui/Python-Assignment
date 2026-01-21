def Perfect(No):
    sum = 0
    for i in range(1,No):
        if No % i == 0:
            Sum = sum + i
    if Sum == No:
        print("It is perfect number")
    else:
        print("It is not perfect number")
def main():
    No = int(input("Enter thr number :"))
    Perfect(No)
if __name__ =="__main__":
    main()