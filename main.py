import sys
from stats import get_num_words, get_occurrence_dict

def get_book_text(filepath):
    with open(filepath) as f:
      return f.read()

def main():
  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
  filepath = sys.argv[1]
  text = get_book_text(filepath)
  num_words = get_num_words(text)
  occurrence_dict = get_occurrence_dict(text)
  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {filepath}")
  print("----------- Word Count ----------")
  print(f"Found {num_words} total words")
  print("--------- Character Count -------")
  sorted_occurrences = sorted(occurrence_dict.items(), key=lambda item: item[1], reverse=True)
  for char, count in sorted_occurrences:
      print(f"{char}: {count}")
  print("============= END ===============")

main()
