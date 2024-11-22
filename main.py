def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    #calls main book open/read func

    total_words_int = get_total_words(text)
    #calls count of all words from text file

    total_chars_int = get_character_count(text)
    #calls count of all characters in text_file
    
    sorted_chars_int = sort_character_count(total_chars_int)
    # takes total chars func and sorts by int
    print(f"\n{text}")
    print(f"\n{total_words_int} words found in document")
    print(f"\n{total_chars_int}")
    print


def get_total_words(txt_file):
    seperate = txt_file.split()
    count = len(seperate)
    return count




main()