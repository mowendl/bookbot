# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["num"]

def count_words(string): 
    words = string.split()  # Split the string into words 
    return len(words)       # Return the number of words 

def count_chars(string):
    d = {}
    for x in string:
        x = x.lower()
        d[x] = d.get(x, 0) + 1
    return d

def main():
    path_to_file = "books/frankenstein.txt"

    with open(path_to_file) as f:
        file_contents = f.read()
    
    #print(file_contents)
    
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{count_words(file_contents)} word(s) found in the document\n")
    
    dict_count_chars = count_chars(file_contents)
    list_count_char  = []

    for key, value in dict_count_chars.items():
        if key.isalpha():
            dict = {
                "char": key,
                "num": value
            }
            list_count_char.append(dict)

    list_count_char.sort(reverse=True, key=sort_on)

    for i in list_count_char:
        print(f"The character '{i['char']}' was found {i['num']} time(s)")
    print("--- End report ---")

main()