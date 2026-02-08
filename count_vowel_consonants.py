text = input(f"Text: ")
lower_text = text.lower().split()
input_text = "".join(lower_text)

vowel_count = 0
consonant_count = 0

for text in input_text:
    if text.isalpha():
        if text in ['a', 'e', 'i', 'o', 'u']:
            vowel_count += 1
        else:
            consonant_count += 1

print(f"The number of vowels in the string is: {vowel_count}")
print(f"The number of consonants in the string is: {consonant_count}")
