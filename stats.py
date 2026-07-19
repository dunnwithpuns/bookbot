def get_word_count(text): 
    words = text.split()
    count = len(words)
    return count

def get_labeled_chars(chars_dict):
    labeled_chars = []
    for char in chars_dict:
        if char.isalpha() == True:
            label_dict = {}
            label_dict["char"] = char 
            label_dict["num"] = chars_dict[char] 
            labeled_chars.append(label_dict)
    return labeled_chars

