def get_num_words(book):
    return len(book.split())

def get_char_counts(book):
    letters = {}
    for char in book:
        letter = char.lower()
        if not letter.isalpha():
            pass
        elif letter in letters:
            letters[letter] += 1
        else:
            letters[letter] = 1
    letters = {key: val for key, val in sorted(letters.items(), key = lambda ele: ele[1], reverse = True)}
    return letters
