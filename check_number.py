number = float(input("Enter a number: "))

match number:
    case n if n < 0:
        print("The number is negative.")
    case n if n > 0:
        print("The number is positive.")
    case _:
        print("The number is zero.")
