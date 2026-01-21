def Numbers(No):
    for i in range(1,6,1):
        No = No + 1
        print(i)
def main():
    No = int(input("Enter the number :"))
    Numbers(No)
if __name__ == "__main__":
    main()

