def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(f"--- Begin report of {book_path} ---")
    word_count = get_word_count(text)
    print(f"{word_count} words found in the document\n")
    char_dict = count_chars_appearance(text)
    pretty_print_char_dict(char_dict)
    print("--- End report ---")


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    return len(words)

def count_chars_appearance(text):
    lowercased_text = text.lower()
    char_count = len(text)

    char_dict = {}

    for i in range(0, char_count):
        char = lowercased_text[i]

        if (char_dict.get(char) == None):
            char_dict[char] = 1
        else: 
            char_dict[char] += 1
    
    return char_dict

def pretty_print_char_dict(dict):
    for char, count in dict.items():
        print(f"The {char} character was found {count}")
        

main()