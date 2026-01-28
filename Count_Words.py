sentence = input("Enter a sentence: ")
words = sentence.split()

print(f"The number of words in the sentence is; {len(words)}")
print(f"The longest word in the sentence is: {max(words, key=len)}")
