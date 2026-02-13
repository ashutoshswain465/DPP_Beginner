with open("number_file/numbers.txt", 'r') as file:
    numbers = [float(line.strip()) for line in file]
    print(f"The maximum number in the file is: {max(numbers)}")
