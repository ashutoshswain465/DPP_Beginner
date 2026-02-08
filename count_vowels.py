text = input(f"text: ")
text_split = text.lower().split()
single_text = "".join(text_split)

vowel_count = 0

for letter in single_text:
    if letter.isalpha():
        if letter in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1

print(f"The number of vowels in the string is: {vowel_count}")
