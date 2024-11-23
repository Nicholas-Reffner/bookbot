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
    output_message = output_message_function(sorted_chars_int)
    

    
    #print(f"\n{text}")
    ##print(f"\n{total_chars_int}")
    #prints sorted_char return
    #print(sorted_chars_int)



    print(f" --- Begin report of {book_path} --- ")
    print(f"{total_words_int} words found in the document")
    for char in output_message:
        print(char)
    #print(list(output_message))
    print(" --- End report --- ")






def get_total_words(txt_file):
    seperate = txt_file.split()
    count = len(seperate)
    return count

#takes full text from above function
#all characters made lowercase
#characters split into indiviual strings
#alphabet characters added to letters list
#iterate though all in letters and adds count to-
#- char_count_total dictionary
def get_character_count(text_file):
    char_count_total = {}
    letters = []
    text_file_lower = text_file.lower()
    characters = list(text_file_lower)
    for char in characters:
        if char.isalpha():
            letters.append(char) 
    for i in letters:
        if i not in char_count_total:
            char_count_total[i] = 1
        else:
            char_count_total[i] += 1
    return char_count_total



#takes results from above dictionary
#iterates though dict
#splits key-value tuples to items list
#appends individual single key-values lists to list_2d
#sorts list_2d by values in reverse order
def sort_character_count(total_chars_int):
    items = []
    list_2d = []
    #list(total_chars_int)
    for key, value in total_chars_int.items():
        items.append(key)
        items.append(value)
        list_2d.append(items[:2])
        items.clear()
    list_2d_sorted = sorted(list_2d, key=lambda x: x[1], reverse=True)
    
    return list_2d_sorted

        



def output_message_function(sorted_character_count):
    char_list = []
    for char in sorted_character_count:
        char_list.append(f"the '{char[0]}' character was found {char[1]} times")
    
    return char_list
        
        





    

def get_book_text(path):
    with open(path) as f:
        return f.read()


main()