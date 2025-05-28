from stats import get_book_text
from stats import get_num_words
from stats import get_num_characters
from stats import get_sorted
import sys 

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path = sys.argv[1]
    text = get_book_text(path)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
    print("--------- Character Count -------")

    counts = get_num_characters(text)
    sorted_chars = get_sorted(counts)

    for item in sorted_chars:
        print(f"{item['char']}: {item['num']}")

    print("============= END ===============")
    
    
if __name__ == "__main__":
    main()