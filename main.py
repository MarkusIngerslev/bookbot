from stats import get_num_words

def main():
    book_path = "./books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return get_num_words(file_contents)

main()