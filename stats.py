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