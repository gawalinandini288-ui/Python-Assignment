import math

def Area(Radius):
    Area = 0
    Pi = 3.14
    Area = Pi * (Radius**2)
    print("Area of circle :",Area)
def main():
    Radius = int(input("Enter the radius ;"))
    Area(Radius)
if __name__ == "__main__":
    main()