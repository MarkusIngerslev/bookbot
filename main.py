from stats import get_num_words, get_char_count

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    word_count = get_num_words(file_contents)
    char_count = get_char_count(file_contents)
    print(word_count)
    print(char_count)

main()