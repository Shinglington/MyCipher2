from MyCiphers import Vigenere
from MyCryptanalysis.ngram_score import calc_score
from MyCryptanalysis.nbest import nbest
import MyCryptanalysis.util as util

def Attack_Vigenere(ciphertext, keyLength = None):
	if keyLength == None:
		keyLength = guess_key_length(ciphertext)

def guess_column_key(column)


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