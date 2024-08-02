def main():

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    count_words(file_contents)

def count_words(file_contents):
    words = len(file_contents.split())
    
        
    print (f"{words}")


main()
