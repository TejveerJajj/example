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

def sin(x):
    return math.sin(math.radians(x))

def cos(x):
    return math.cos(math.radians(x))

def tan(x):
    return math.tan(math.radians(x))

def main():
    history = []
    print("Select operation:")
    print("1.Add")
    print("2.Subtract")
    print("3.Multiply")
    print("4.Divide")
    print("5.Exponent")
    print("6.Square Root")
    print("7.History")
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
                result = add(num1, num2)
                history.append(f"{num1} + {num2} = {result}")
                print(num1, "+", num2, "=", result)

            elif choice == '2':
                result = subtract(num1, num2)
                history.append(f"{num1} - {num2} = {result}")
                print(num1, "-", num2, "=", result)

            elif choice == '3':
                result = multiply(num1, num2)
                history.append(f"{num1} * {num2} = {result}")
                print(num1, "*", num2, "=", result)

            elif choice == '4':
                result = divide(num1, num2)
                history.append(f"{num1} / {num2} = {result}")
                print(num1, "/", num2, "=", result)

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
              break

        elif choice == '5':
            try:
                num1 = float(input("Enter a number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            result = exponent(num1)
            history.append(f"{num1} ^ 2 = {result}")
            print(num1, "^", 2, "=", result)

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
              break

        elif choice == '6':
            try:
                num1 = float(input("Enter a number: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue
            result = square_root(num1)
            history.append(f"sqrt({num1}) = {result}")
            print("sqrt(", num1, ") =", result)

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
              break

        elif choice == '7':
            print("Calculation history:")
            for calculation in history:
                print(calculation)

        elif choice in ('8', '9', '10'):
            try:
                num1 = float(input("Enter an angle in degrees: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                continue

            if choice == '8':
                result = sin(num1)
                history.append(f"sin({num1}) = {result}")
                print(f"sin({num1}) = {result}")
            elif choice == '9':
                result = cos(num1)
                history.append(f"cos({num1}) = {result}")
                print(f"cos({num1}) = {result}")
            elif choice == '10':
                result = tan(num1)
                history.append(f"tan({num1}) = {result}")
                print(f"tan({num1}) = {result}")

            next_calculation = input("Let's do next calculation? (yes/no): ")
            if next_calculation == "no":
                break
        else:
            print("Invalid Input")

if __name__ == "__main__":
    main()
