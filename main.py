from collections import defaultdict

def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_num_words(text): 
    words = text.split()
    return len(words)

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_count = count_letters(text)
    print(chars_count)

def count_letters(text):
    count_of_letters = defaultdict(int)
    lower_case_string = text.lower()
    for i in lower_case_string:
        if i.isalpha():
            count_of_letters[i] +=1
    return count_of_letters
            

main()