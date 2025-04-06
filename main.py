from stats import get_num_words, get_num_letters, report
import sys

def main():
    if len(sys.argv) == 2:
        file = sys.argv[1]
        words = get_num_words(file)
        characters = get_num_letters(file)

        report(file, words, characters)
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

main()
