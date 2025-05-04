import sys
from stats import get_num_words
from stats import sort_letters

def main():
    if len(sys.argv) > 1:
        book_path = sys.argv[1]
        letters, word_count = get_num_words(book_path)
        sorted_letters = sort_letters(letters)
        sorted_letters.sort(reverse=True, key=lambda dict: dict["num"])
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for line in sorted_letters:
            print(f"{line['letter']}: {line['num']}")
        print("============= END ===============")
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
main()
