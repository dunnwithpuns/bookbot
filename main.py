import sys
from stats import get_word_count, get_labeled_chars

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        return  sys.exit(1)

    book_path = f"{sys.argv[1]}"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars_dict = get_chars_dict(text) 
    labeled_chars = get_labeled_chars(chars_dict)
    labeled_chars.sort(reverse=True, key=sort_on)
    print_report(book_path, word_count, labeled_chars)
    return sys.exit(0)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def print_report(book_path, word_count, labeled_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"Found {word_count} total words\n")
    for char in labeled_chars:
        print(f"'{char['char']}: {char['num']}'")
    print("--- End report ---")
 
def sort_on(dict):
    return dict["num"]

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

if __name__ == "__main__":
    main()
