# main.py

from texttools.cleaning import remove_punctuation, remove_extra_spaces
from texttools.tokenization import tokenize
from texttools.frequency import word_frequency

text = input("Enter a sentence: ")

# Remove punctuation
text = remove_punctuation(text)

# Remove extra spaces
text = remove_extra_spaces(text)

# Tokenize text
words = tokenize(text)

# Calculate word frequency
frequency = word_frequency(words)

print("\n----- TEXT ANALYSIS -----")
print("Cleaned Text:", text)
print("Tokens:", words)

print("\nWord Frequency:")
for word, count in frequency.items():
    print(word, ":", count)