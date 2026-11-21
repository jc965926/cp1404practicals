"""
Word Occurrences
Estimate: 25 minutes
Actual:   18 minutes
"""
word_to_occurrences = {}

string = input("Please type a sentence: ")
for word in string.split():
    if word not in word_to_occurrences:
        word_to_occurrences[word] = 1
    else:
        word_to_occurrences[word] += 1

max_word_length = max([len(word) for word in word_to_occurrences.keys()])

# print(sorted(word_to_count.items()))
print(f"Text: {string}")
for word, count in sorted(word_to_occurrences.items()):
    print(f"{word:<{max_word_length}} : {count}")