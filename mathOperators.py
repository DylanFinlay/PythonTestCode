#Addition, subtraction, modulus, floor division, decimal division, and multiplication

def add(x, y):
    return x + y 

def subtract(x, y):
    return x - y

def mod(x, y):
    return x%y 

def floordiv(x, y):
    return x//y

def divide(x, y):
    return x/y

def mult(x, y):
    return x * y

def main():
    num1 = int(input("Enter an integer for num1: "))
    num2 = int(input("Enter an integer for num2: "))

    print("num1 plus num2:", add(num1, num2))
    print("num1 minus num2:", subtract(num1, num2))
    print("num1 mod num2:", mod(num1, num2))
    print("num1 floordiv num2:", floordiv(num1, num2))
    print("num1 divided by num2:", divide(num1, num2))
    print("num1 times num2:", mult(num1, num2))





