num1 = float(input(f"Enter the first number: "))
num2 = float(input(f"Enter the second number: "))

operator = input(f"Enter operation (+, -, *, /): ")

if operator == '+':
    print(f"The result is: {num1 + num2}")
elif operator == '-':
    print(f"The result is: {num1 - num2}")
elif operator == '*':
    print(f"The result is: {num1 * num2}")
elif operator == '/':
    print(f"The result is: {num1 / num2}")
else:
    print(f"Invalid arithmetic operation")
