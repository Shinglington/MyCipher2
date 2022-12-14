from MyCiphers import Railfence
from MyCryptanalysis.nbest import nbest
from MyCryptanalysis.ngram_score import calc_score

def Attack_Railfence(ciphertext):
	attempts = nbest(3)
	for key in range(2, 11):
		attempts.add(key, calc_score(Railfence(key).decrypt(ciphertext)))

	for i in range(3):
		pair = attempts[i]
		print(str(i+1) + ". Key = " + str(pair[0]) + ", score = " + str(pair[1]))
		print(Railfence(pair[0]).decrypt(ciphertext))
		print("\n\n\n")
		