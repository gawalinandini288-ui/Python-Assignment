def ChkGreater(No1,No2):
    if(No1 > No2):
        print(No1)
    else:
        print(No2)

def main():
    No1 = int(input("Enter First Number :"))
    No2 = int(input("Enter Second Number :"))

    ChkGreater(No1,No2)

if __name__ == "__main__":
    main()