from stats import get_num_words, get_num_characters


def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
        return book_contents


def main():
    book_words = get_book_text("books/frankenstein.txt")
    count_of_words = get_num_words(book_words)  
    print(f"Found {count_of_words} total words") 
    print("testicals:", get_num_characters(book_words))
main()

