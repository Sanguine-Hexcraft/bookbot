def get_num_words(text):
    return len(text.split()) 


def get_num_characters(text):
    char_dic = {}
    text = text.lower()
        
    for char in text:
        if char not in char_dic:
            char_dic[char] = 0
        char_dic[char] = char_dic[char] + 1

    return char_dic
    
