def Grade(Marks):
    if Marks >= 75:
        print("Distinction")
    elif Marks >= 60:
        print("First Class")
    elif Marks >= 50:
        print("Second Class")
    elif Marks <= 50:
        print("Fail")
    else:
        print("None")
def main():
    Marks = int(input("Enter the Number :"))
    Grade(Marks)
if __name__ == "__main__":
    main()