# Simple Python Calculator
# There are a few small bugs in this file.
# Fix them and submit a pull request!

def add(a, b):
    return a + b  


def subtract(a, b):
    return a - b   


def multiply(a, b):
    return a * b   


def divide(a, b):
    if(b == 0):
        return "b can't be 0"
    return a / b  


def main():
    print("Simple Calculator")
    print("Operations: +  -  *  /")

    operation = input("Enter operation: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == "+":
        result = add(num1, num2)
        print("Result:", result)

    elif operation == "-":
        result = subtract(num1, num2)
        print("Result:", result)

    elif operation == "*":
        result = multiply(num1, num2)
        print("Result:", result)

    elif operation == "/":
        result = divide(num1, num2)
        print("Result:", result)

    else:
        print("Invalid operation. Use +, -, *, or /.")


if __name__ == "__main__":
    main()
