def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars_dict = get_chars_dict(text) 
    print(chars_dict)
    
def get_word_count(text): 
    words = text.split()
    count = len(words)
    return count

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

main()
