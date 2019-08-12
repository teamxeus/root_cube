#program to calculate the square root and cube root
#the program uses newtons method to approximate the values
from math import fabs
def menu():
    print("This is a program to calculate the square root and cube root of a real number")
    choice = eval(input("Enter:\n1: for square root\n2: for cube root\n"))
    return choice
def squareRoot(value):
    root = 1.0
    diff = root * root - value
    while diff > 0.0001 or diff < -0.0001:
        root = (root + value / root) / 2.0
        diff = root * root - value
    return root
def cubeRoot(value):
    error = 0.00000001
    start = 0
    end = value
    while True:
        mid = (start + end) / 2
        if fabs((value - mid * mid * mid)) < error:
            return mid
        elif (mid * mid * mid) > value:
            end = mid
        if (mid * mid * mid) < value:
            start = mid

    remainder = value
def main():
    choice = menu()
    value = eval(input("Enter value:"))
    if choice != 1 and choice != 2:
        print("ERROR: input not recognised\nprogram will exit now.")
    elif choice == 1:
        square_root = squareRoot(value)
        print("The square root of ",value," is ",square_root)
    else:
        cube_root = cubeRoot(value)
        print("The cube root of ",value," is ",cube_root)
    delay = input("Press enter to exit")
main()