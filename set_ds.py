random_word = 'abracadabra'
unique_alph: set[str] = set(random_word)

print(unique_alph)

sentence = 'the big blue sky and the big blue ocean'

unique_alph = set(sentence)
print(unique_alph)

word_list = sentence.split()
print(word_list)

unique_words = set(word_list)
print(unique_words)

unique_words.update(['big', 'data'])
print(unique_words)

unique_words.remove('data')
print(unique_words)
