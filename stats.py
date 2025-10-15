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
    # Loop through each character(char), if the character not in dictionary,
    # add the key("character") and value("0"), else increment the value by 1 of the character
    for char in text:
        if char not in char_dic:
            char_dic[char] = 0
        char_dic[char] = char_dic[char] + 1
    # Return the dictionary to main()
    return char_dic

# A function to had a key to sort a list of tuples or dicts by the value of the key num
def sorterator(items):
    return items["num"]

# A function to sort the keys by value in a list of dicts with key=character and value=number
# sored_dic parameter comes from the call in main() ~sorted_characters~ 
def sort_the_dic(sorted_dic):
    # Create the list for storing our tuples
    sorted_dic_list = []

    # Loop through the key(k) and count(c) in the items in the dictionary
    for k, c in sorted_dic.items():
        # Conditionally check if the string is an alpha (e.g a,b,c, not a symbol or space) 
        # and if it is, append it to the new empty list sorted_dic_list,
        # with a new tuple of keys of char and num, with the values of the "char": (single character) and "num": integer
        if k.isalpha():
            sorted_dic_list.append({"char": k, "num": c})
        
    # Sort the new list of dictionarys in reverse order(Highest to Lowest)
    # Also call the sorterator function so it sorts by the key of "num"
    sorted_dic_list.sort(reverse=True, key=sorterator)
    
    # Return tne new sorted list to main()
    return sorted_dic_list

