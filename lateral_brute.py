regular_alphabet = [
	letter.encode('UTF8') for letter in open('res/regular_alphabet.txt').read()
]
inverse_alphabet = [
	letter.encode('UTF8') for letter in open('res/inverse_alphabet.txt').readlines()
]
regular_words = []
inverse_words = []

print regular_alphabet
print inverse_alphabet

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