sentence = input("text = ")
words = sentence.split()
no_space_text = "".join(words)

upper_count = 0
lower_count = 0

for letter in no_space_text:
    if letter.isalpha():
        if letter.isupper():
            upper_count += 1
        else:
            lower_count += 1

print(f"The number of uppercase letters is: {upper_count}")
print(f"The number of lowercase letters is: {lower_count}")
