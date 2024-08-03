def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_string = get_words(text)
    dict_character = character_count(lowered_string)

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
    print (f"{dict_character}")
        
        



main()