def name_upper(input_name):
    return input_name.upper()


def name_lower(input_name):
    return input_name.lower()


def name_len(input_name):
    name_text = input_name.split()
    no_space_name = "".join(name_text)
    return len(no_space_name)


def name_rev(input_name):
    rev_name = input_name[::-1]
    return rev_name


name = input("Please enter your full name: ")

print(f"Your name in uppercase: {name_upper(name)}")
print(f"Your name in lowercase: {name_lower(name)}")
print(f"Total number of characters (excluding spaces): {name_len(name)}")
print(f"Your name reversed: {name_rev(name)}")
