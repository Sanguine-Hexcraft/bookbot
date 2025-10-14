# We pass the book text from main().
# then we split the long string (whole book) so each word is its own string.
# Then return the length of that list as an integer or count.
def get_num_words(text):
    return len(text.split())


# Again we pass book_words from main() into this function's parameter
def get_num_characters(text):
    # Make an empty dictionary
    char_dic = {}
    # We then lowercase all the strings we passed from main()
    text = text.lower()
    # Loop through each character(char)     
    for char in text:
        if char not in char_dic:
            char_dic[char] = 0
        char_dic[char] = char_dic[char] + 1

    return char_dic

def sorterator(items):
    return items["num"]

def sort_the_dic(text):
    sorted_dic_list = []
    test_dic = {}

    for k, c in text.items():
        if k.isalpha():
            sorted_dic_list.append({"char": k, "num": c})
        # print(f"test test test {sorted_dic_list}")
    
    sorted_dic_list.sort(reverse=True, key=sorterator)
    
    return sorted_dic_list

    # print(f"test test test: {sorted_dic_list}")

