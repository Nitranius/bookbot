def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    lowered_string = get_words(text)
    print(f"{num_words} words found in the document")
    


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


    

main()