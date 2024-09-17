def main():
  book_path = "books/frankenstein.txt"
  text = get_book_text(book_path)
  words_counter = count_words(text)
  characters_counter = count_characters(text)
  chars_sorted_list = sorted_chars_list(characters_counter)
  
  print(f"--- Begin report of {book_path} ---")
  print(f"{words_counter} words found in the document")
  print()

  for item in chars_sorted_list:
    if not item["char"].isalpha():
      continue
    print(f"The '{item['char']}' character was found {item['num']} times")

  print("--- End report ---")

def get_book_text(path):
  with open(path) as f:
    return f.read()
  
def count_words(book_text):
  words_array = book_text.split()
  counter = len(words_array)
  return counter

def count_characters(book_text):
  chars = {}
  for char in book_text:
    lowered = char.lower()
    if lowered in chars:
      chars[lowered] += 1
    else:
      chars[lowered] = 1
  return chars

def sort_on(dict):
  return dict["num"]

def sorted_chars_list(chars_counter_dictionary):
  sorted_list = []
  for char in chars_counter_dictionary:
    sorted_list.append({"char": char, "num": chars_counter_dictionary[char]})
  sorted_list.sort(reverse=True, key=sort_on)
  return sorted_list

main()