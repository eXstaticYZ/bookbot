import sys
from stats import get_char_counts, get_num_words

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    file_path = sys.argv[1]
    book = get_book_text(file_path)
    word_count = get_num_words(book)
    chars = get_char_counts(book)

    print("============ BOOKBOT ============")
    print("Analyzing book found at %s..." % file_path)
    print("----------- Word Count ----------")
    print("Found %s total words" % word_count)
    print("--------- Character Count -------")
    for char in chars:
        print(f"{char}: {chars[char]}")
    print("============= END ===============")

def get_book_text(file_path):
    file = open(file_path, "r")
    contents = file.read()
    file.close()
    return contents

main()
