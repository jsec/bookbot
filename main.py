def main():
    path = "books/frankenstein.txt"
    word_count, char_count = get_book_stats(path)
    print_report(path, word_count, char_count)


def get_book_stats(path):
    book = get_book(path)
    return get_word_count(book), get_char_count(book)


def print_report(path, word_count, char_count):
    print(f"~~~ Begin report of {path} ~~~")
    print(f"{word_count} words found in the document")
    print()

    char_list = list(char_count.items())
    char_list.sort(key=lambda x: x[1], reverse=True)

    for char, count in char_list:
        if char.isalpha():
            print(f"The '{char}' character was found {count} times")

    print("~~~ End report ~~~")


def get_book(path):
    with open(path) as file:
        return file.read()


def get_word_count(text):
    return len(text.split())


def get_char_count(text):
    counts = {}

    for c in text:
        char = c.lower()
        if char not in counts:
            counts[char] = 0

        counts[char] += 1

    return counts


main()
