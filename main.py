def main():
    filepath = "books/frankenstein.txt"
    print(f"---------- Begin Report on {filepath} ----------")

    text = get_text(filepath)
    total_count = count_all(text)
    print(f"There are a total of {total_count} words")
    print("\n")
    char_count = get_char_count(text)
    char_list = dict_to_list(char_count)
    char_list.sort(reverse=True, key=getCount)
    
    for dict in char_list:
        print(f"The letter {dict["letter"]} was found {getCount(dict)} times")
    
    print("---------- End Report ----------")


def getCount(dict):
    return dict["count"]   

def dict_to_list(dict):
    lst = []
    for key in dict:
        if key.isalpha():
            lst.append({"letter": key, "count": dict[key]})
    return lst 

def get_char_count(text):
    count = {}
    for ch in text:
        lowered = ch.lower()
        if lowered not in count:
            count[lowered] = 0
        count[lowered] += 1
    return count


def get_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def count_all(text):
    words = text.split()
    return len(words)

main()
