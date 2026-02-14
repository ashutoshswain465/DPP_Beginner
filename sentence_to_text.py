line1 = input("Enter sentence 1: ")
line2 = input("Enter sentence 2: ")
line3 = input("Enter sentence 3: ")

lines = [line1, line2, line3]

filepath = 'user_sentence/user_sentences.txt'

with open(filepath, 'w') as file:
    print(*lines, sep="\n___________\n", file=file)

print(f"Sentences have been saved to {filepath}.")
