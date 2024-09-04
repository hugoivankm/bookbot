def count_words(content):
    return len(content.split())


def get_book_content(filepath):
    with open(filepath) as f:
        return f.read()


def count_characters(content):
    char_dict = {}
    for ch in content:
        if (char := ch.lower()) in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def print_report(book_file_path):
    content = get_book_content(book_file_path)
    chars_counted = count_characters(content)
    
    def to_dict_list(dict):
        dict_list = []
        for key, value in dict.items():
            dict_list.append({"character": key, "count": value})
        return dict_list
    
    def sort_on(dict):
        return dict["count"]

    print(f"--- Begin report of {book_file_path} ---")
    print(f"{count_words(content)} words found in the document")
    print("\n")

    counted_chars_dict_list = (to_dict_list(chars_counted))
    counted_chars_dict_list.sort(reverse=True, key=sort_on)
    for entry in counted_chars_dict_list:
        if entry["character"].isalpha():
            print(f"The {entry["character"]} character was found {entry["count"]} time{('s' if entry["count"] > 1 else "")}")
   
    print("--- End report ---")


def main():
    print_report("books/frankenstein.txt")


main()
