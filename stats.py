def get_num_words(text):
  words = text.split()
  return len(words)


def get_occurrence_dict(text):
  occurrence_dict = {}
  for char in text.lower():
    if char == " ":
      continue
    if char in occurrence_dict:
      occurrence_dict[char] += 1
    else:
      occurrence_dict[char] = 1
  return occurrence_dict
