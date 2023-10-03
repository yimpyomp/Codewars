# https://www.codewars.com/kata/51e056fe544cf36c410000fb/train/python


def top_three_words(text):
    if not text:
        return []
    words = text.split(' ')
    occurences = {}
    for word in words:
        if not word.isalpha():
            continue
        if word.lower() not in occurences.keys():
            occurences[word.lower()] = 1
        else:
            occurences[word.lower()] += 1
    max_vals = [str(i)]