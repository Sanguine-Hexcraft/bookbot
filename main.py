import sys
from stats import get_num_words, get_num_characters, sort_the_dic

# Function that opens the file path to the books and returns it to main().
def get_book_text(filepath):
    with open(filepath) as f:
        book_contents = f.read()
        return book_contents


def main():
    # Set the path to our book(s).
    if len(sys.argv) < 2:
        sys.exit(1)
    books_path = sys.argv[1]
    # Create a new variable by calling the function get_book_text with the path to book.
    book_words = get_book_text(books_path)
    # Create a new variable by returning a value from the function in stats.py to count the number of words in the book.
    count_of_words = get_num_words(book_words)

    # This is where our funky munky print statment is going:
    print("============ BOOKBOT ============")
    # Prints the path of books
    print(f"Analyzing book found at {books_path}...")
    print("----------- Word Count ----------")
    # Prints the number of words in the document to the console.
    print(f"Found {count_of_words} total words")
    print("--------- Character Count -------")
    # Create a new variable to store the key(character) and value(number the character is used) in a dictionary.
    sorted_characters = get_num_characters(book_words)
    # -------
    # Create a variable to store a list of sorted (high to low) 
    # of small dictionaries using the key/value pair of "char": char and "num": count.
    # So we can print them in a nice format in the console
    printable_char_list = sort_the_dic(sorted_characters)
    # loop through or new sorted list of small dics and just create a 
    # string with the string of char and int of num
    for k in printable_char_list:
        ch = k["char"]
        nm = k["num"]
        print(f"{ch}: {nm}")
    # print(printable_char_list)

    print("============= END ===============")

main()

