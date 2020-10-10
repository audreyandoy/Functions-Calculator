print("---Welcome to Calculator Program---")
print()
num1 = int(input("Provide a first number: "))
num2 = int(input("Provide a second number: "))
op = input("Provide an operator. Choose one: \n +, -, /, *  \n")

# create a function
def check_operator(op):
    global num1, num2
    if op == "+":
        # addition
        print(f"{num1} {op} {num2}")
        addition(num1, num2)
    elif op == "-":
        # subtraction
        print(f"{num1} {op} {num2}")
        subtract(num1, num2)
    elif op == "/":
        # division
        print(f"{num1} {op} {num2}")
        division(num1, num2)
    elif op == "*":
        # multiplication
        print(f"{num1} {op} {num2}")
        multiplication(num1, num2)
    else:
        print("hm.. that's not an operation.")

def addition(n1, n2):
    print(f" = {n1 + n2}")

def subtraction(n1, n2):
    print(f" = {n1 - n2}")

def division(n1, n2):
    print(f" = {n1 / n2}")

def multiplication(n1, n2):
    print(f" = {n1 * n2}")

check_operator(op)