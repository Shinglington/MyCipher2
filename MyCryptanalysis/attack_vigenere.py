from MyCiphers import Vigenere
from MyCiphers import Caesar
from MyCryptanalysis.ngram_score import calc_score
from MyCryptanalysis.nbest import nbest
import MyCryptanalysis.util as util

def Attack_Vigenere(ciphertext, keyLength = None):
	if keyLength == None:
		keyLength = guess_key_length(ciphertext)
	columns = split_to_columns(ciphertext, keyLength)
	column_keys = []
	for i in range(keyLength):
		col = columns[i]
		column_keys.append(guess_column_key(col))
	print(column_keys)
	keywords = guess_likely_keywords(column_keys)

	best_keys = nbest(3)
	for key in keywords:
		best_keys.add(key, calc_score(Vigenere(key).decrypt(ciphertext)))

	for i in range(len(best_keys)):
		pair = best_keys[i]
		print(str(i+1) + ". Key = " + str(pair[0]) + ", score = " + str(pair[1]))
		print(Vigenere(pair[0]).decrypt(ciphertext))
		print("\n\n\n")
	
def guess_likely_keywords(column_keys):
	keywords = ["" * len(column_keys)]
	for i in range(len(column_keys)):
			key_letters = column_keys[i]
			new_keywords = []
			for j in range(len(keywords)):
				for k in key_letters:
					new_keywords.append(keywords[j] + k)
			keywords = new_keywords
	return keywords

def guess_column_key(column):
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	col_keys = nbest(5, reverse = False)
	for i in range(26):
		decrypt_col = Caesar(i).decrypt(column)
		score = util.Calc_Chi_Squared(decrypt_col)
		col_keys.add(alphabet[i], score)
	likely_keys = []
	for i in range(len(col_keys)):
		pair = col_keys[i]
		if pair[1] < (2 * col_keys[0][1]):
			likely_keys.append(pair[0])

	return likely_keys
	


def guess_key_length(ciphertext, max = 30):
	text = ciphertext.replace(" ","").upper()
	bestKeyLengths = nbest(max)
	for i in range(1, max + 1):
		columns = split_to_columns(text, i)
		total_ioc = 0
		for col in columns:	
			total_ioc += util.Calc_Ioc(col)
		avg_ioc = total_ioc / i
		bestKeyLengths.add(i, avg_ioc)

		# Show ioc for column
		print(str(i) + " : " + str(avg_ioc))

	bestPair = bestKeyLengths[0]
	for i in range(1, 4):
		pair = bestKeyLengths[i]
		if bestPair[0] % pair[0] == 0:
			bestPair = pair
	print("guessed key length to be " + str(bestPair[0]))
	return bestPair[0]
	
def split_to_columns(ciphertext, columnCount):
	columns = [""] * columnCount
	for i in range(len(ciphertext)):
		columns[i%columnCount] = columns[i%columnCount] + ciphertext[i]
	return columns