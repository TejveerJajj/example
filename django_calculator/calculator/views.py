from django.shortcuts import render

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

def exponent(x):
    return x ** 2

def calculate(request):
    result = None
    if request.method == 'POST':
        try:
            num1 = float(request.POST.get('num1'))
            operation = request.POST.get('operation')

            if operation == 'exponent':
                result = exponent(num1)
            else:
                num2 = float(request.POST.get('num2'))
                if operation == 'add':
                    result = add(num1, num2)
                elif operation == 'subtract':
                    result = subtract(num1, num2)
                elif operation == 'multiply':
                    result = multiply(num1, num2)
                elif operation == 'divide':
                    result = divide(num1, num2)
        except (ValueError, TypeError):
            result = "Error! Invalid input."

    return render(request, 'index.html', {'result': result})
