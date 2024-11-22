def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    total = total_words(text)
    print(text)
    print(total)


def get_book_text(path):
    with open(path) as f:
        return f.read()


def total_words(txt_file):
    seperate = txt_file.split()
    count = len(seperate)
    return count
    



main()