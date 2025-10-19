from stats import get_num_words, get_char_count, sort_char_count

def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    print(book_text)

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    word_count = get_num_words(file_contents)
    char_count = sort_char_count(get_char_count(file_contents))
    print_final_message(word_count, char_count, path)

def print_final_message(word_count, char_count, path):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char, count in char_count:
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

main()