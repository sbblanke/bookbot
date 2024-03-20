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
    sorted_chars = sort_dict(chars_count)
    
    print(f" --- Begin Report of {book_path} --- ")
    print(f"{get_num_words(text)} words found in the document")
    print()
    for char_dict in sorted_chars:
        print(f"The {char_dict['letter']} character was found {char_dict['num']} times")
    print()
    print("--- End Report ---")

def count_letters(text):
    count_of_letters = defaultdict(int)
    lower_case_string = text.lower()
    for i in lower_case_string:
        if i.isalpha():
            count_of_letters[i] +=1
    return count_of_letters
            
def sort_dict(count_of_letters):
    list_of_dictionaries = []
    for key, value in count_of_letters.items():
        new_dict = {"letter": key, "num": value}
        list_of_dictionaries.append(new_dict)
    list_of_dictionaries.sort(reverse=True, key=extract_num)
    return list_of_dictionaries

def extract_num(dictionary):
    return dictionary["num"]

main()