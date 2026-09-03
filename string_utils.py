def count_vowels(text):
    count = 0
    for ch in text:
        if ch.lower() in "aeiou":
            count = count + 1
    return count


def reverse_string(text):
    return text[::-1]


def is_palindrome(text):
    return text == text[::-1]


def count_words(text):
    words = text.split()
    return len(words)


def remove_spaces(text):
    return text.replace(" ", "")