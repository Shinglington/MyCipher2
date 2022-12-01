from MyCiphers import Vigenere
from MyCryptanalysis.ngram_score import calc_score
from MyCryptanalysis.nbest import nbest
import MyCryptanalysis.util as util

def Attack_Vigenere(ciphertext, keyLength = None):
	if keyLength == None:
		keyLength = GuessKeyLength(ciphertext)

def GuessKeyLength(ciphertext):
	pass
	
	