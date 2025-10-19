def get_num_words(text):
    words = text.split()
    num_words = len(words)
    return f"Found {num_words} total words"

def get_char_count(text):
    char_list = {}
    text_to_lower = text.lower()
    for i in range(0, len(text_to_lower)):
        if text_to_lower[i] in char_list:
            char_list[text_to_lower[i]] += 1
        else:
            char_list[text_to_lower[i]] = 1
    return char_list

def sort_char_count(char_count):
    char_list = []
    for char in char_count:
        char_list.append((char, char_count[char]))
    char_list.sort(key=sort_on, reverse=True)
    return char_list

def sort_on(items):
    return items[1]