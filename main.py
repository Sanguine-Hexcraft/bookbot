from stats import get_num_words, get_num_characters, sort_the_dic

# Function that opens the file path to the books and returns it to main()
def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
        return book_contents


def main():
    books_path = "books/frankenstein.txt"
    book_words = get_book_text(books_path)
    count_of_words = get_num_words(book_words)

    # This is where our funky munky print statment is going:

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {books_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_of_words} total words")
    print("--------- Character Count -------")
    sorted_characters = get_num_characters(book_words)
    # -------
    # Print sorted list magic go here.
    printable_char_list = sort_the_dic(sorted_characters)
    
    for k in printable_char_list:
        ch = k["char"]
        nm = k["num"]
        print(f"{ch}: {nm}")
    # print(printable_char_list)

    print("============= END ===============")

main()

