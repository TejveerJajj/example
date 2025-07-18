def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

import math

def exponent(x):
    return x ** 2

def square_root(x):
    return math.sqrt(x)

def factorial(x):
    if x < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if x % 1 != 0:
        raise ValueError("Factorial only defined for integers")
    return math.factorial(int(x))

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def main():
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exponent")
    print("6.Square Root")
    print("7.Factorial")
    print("8.Sin")
    print("9.Cos")
    print("10.Tan")

    while True:
        choice = input("Enter choice(1/2/3/4/5/6/7/8/9/10): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '1':
                print(num1, "+", num2, "=", add(num1, num2))

            elif choice == '2':
                print(num1, "-", num2, "=", subtract(num1, num2))

            elif choice == '3':
                print(num1, "*", num2, "=", multiply(num1, num2))

            elif choice == '4':
                print(num1, "/", num2, "=", divide(num1, num2))

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
              break

        elif choice in ('5', '6', '7', '8', '9', '10'):
            try:
                num1 = float(input("Enter a number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            if choice == '5':
                print(num1, "^", 2, "=", exponent(num1))
            elif choice == '6':
                print("sqrt(", num1, ")", "=", square_root(num1))
            elif choice == '7':
                try:
                    print(num1, "!", "=", factorial(num1))
                except ValueError as e:
                    print(e)
            elif choice == '8':
                print("sin(", num1, ")", "=", sin(num1))
            elif choice == '9':
                print("cos(", num1, ")", "=", cos(num1))
            elif choice == '10':
                print("tan(", num1, ")", "=", tan(num1))


            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
              break

        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
