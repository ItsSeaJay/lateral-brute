from __future__ import print_function  # Only needed for Python 2
import codecs # Character encoding

regular_alphabet = codecs.open('res/regular_alphabet.txt', encoding = 'utf-8').read()
regular_alphabet = regular_alphabet.strip(' ').split()
inverse_alphabet = codecs.open('res/inverse_alphabet.txt', encoding = 'utf-8').read()
inverse_alphabet = inverse_alphabet.strip(' ').split()
# Create lists for all of the resulting words
regular_words = []
inverse_words = []

# Generate every possible word with three letters with both regular and
# upside-down characters
for first in regular_alphabet:
	for second in regular_alphabet:
		for third in regular_alphabet:
			word = first + second + third
			regular_words.append(word)

for first in inverse_alphabet:
	for second in inverse_alphabet:
		for third in inverse_alphabet:
			word = first + second + third
			inverse_words.append(word)

# Output all of the words to a file
with codecs.open('build/result.txt', encoding = 'utf-8', mode = 'w') as result:
	for word in range(0, len(regular_words)):
		comparision = regular_words[word] + ' ' + inverse_words[word]
		print(comparision, file = result)