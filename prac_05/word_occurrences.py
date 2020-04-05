"""
CP1404 Practical
a program to count the occurrences of words in a string.
The program should ask the user for a string,
then print the counts of how many of each word are in the file.
"""

word_to_count = {}
text = input("Text: ").upper()
words = text.split()

for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1

words = list(word_to_count.keys())
words.sort()

max_length = max((len(word) for word in words))
for word in words:
    print("{:{}} : {}".format(word, max_length, word_to_count[word]))

