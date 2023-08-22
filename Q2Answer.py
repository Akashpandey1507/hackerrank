def reverse_words_order_and_swap_cases(sentence):
  words = sentence.split(" ")
  words.reverse()
  reversed_words = []
  for word in words:
    new_word = ""
    for i in range(len(word)):
      if word[i].isupper():
        new_word += word[i].lower()
      else:
        new_word += word[i].upper()
    reversed_words.append(new_word)
  reversed_sentence = " ".join(reversed_words)
  return reversed_sentence



sentence = "Hello World!"
reversed_sentence = reverse_words_order_and_swap_cases(sentence)
print(reversed_sentence)
