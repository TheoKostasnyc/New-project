
word_to_find = input("Enter a word to search for: ").lower()

file = open('story.txt', 'r')

word_count = 0

for line in file:
    word_count += line.lower().split().count(word_to_find)

file.close()

print(f"The word '{word_to_find}' appears {word_count} times in the file.")
