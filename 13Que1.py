def Area(Length,Width):
    Area = 0
    Area = Length * Width
    print("Area of Rectangle :", Area)
def main():
    Length = int(input("Enter the length :"))
    Width = int(input("Enter the Width :"))
    Area(Length,Width)
if __name__ == "__main__":
    main()