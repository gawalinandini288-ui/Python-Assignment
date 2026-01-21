def Count(No):
    count = 0
    No = str(No)
    print("Number of digits:",len(No))
def main():
    No = int(input("Enter the number :"))
    Count(No)
if __name__ == "__main__":
    main()