def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    chars_dict = get_chars_dict(text) 
    labeled_chars = get_labeled_chars(chars_dict)
    labeled_chars.sort(reverse=True, key=sort_on)
    get_report(book_path, word_count, labeled_chars)
  
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

def get_labeled_chars(chars_dict):
    labeled_chars = []
    for char in chars_dict:
        if char.isalpha() == True:
            label_dict = {}
            label_dict["char"] = char 
            label_dict["num"] = chars_dict[char] 
            labeled_chars.append(label_dict)
    return labeled_chars

def get_report(book_path, word_count, labeled_chars):
    print(f"--- Begin report of {book_path} ---")
    print(f"{word_count} words found in the document\n")
    for char in labeled_chars:
        print(f"The '{char['char']}' character was found {char['num']} times")
    print("--- End report ---")
 
def sort_on(dict):
    return dict["num"]

def get_book_text(book_path):
    with open(book_path) as f:
        return f.read()

if __name__ == "__main__":
    main()