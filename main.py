def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_string = get_words(text)
    dict_character = character_count(lowered_string)
    key_value_alpha = print_character_number(dict_character)
    string_charcount_list = make_string_KV_pairs(key_value_alpha)
    individual_char_string = print_list_individual(string_charcount_list)
    print(individual_char_string)
    
    
def get_num_words(text):
    words = text.split()
    return len(words)

def get_words(words):
    words_string = "".join(words)
    lowered_string = words_string.lower()
    return lowered_string

def get_book_text(path):
    with open(path) as f:
        return f.read()

def character_count(lowered_string):
    dict_character = {}
    for character in lowered_string:
        if character not in dict_character:
            dict_character[character] = 1
        else: 
            dict_character[character] += 1
    return dict_character

def print_character_number(dict_character):
    key_value_alpha = []
    for key, value in dict_character.items():
        if key.isalpha():
            key_value_alpha.append({key: value})
    return key_value_alpha

def make_string_KV_pairs(key_value_alpha):
    string_charcount_list = []
    for dict in key_value_alpha:
        key, value = list(dict.items())[0]
        make_string_char_count = (f"the {key} character was found {value} times")
        string_charcount_list.append(make_string_char_count)
    return string_charcount_list

def print_list_individual(string_charcount_list):
    result = ""
    for individual in string_charcount_list:
        result += (f"{individual}\n")
    return result

main()