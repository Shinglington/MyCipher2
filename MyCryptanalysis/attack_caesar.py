from MyCiphers import Caesar
from MyCryptanalysis.nbest import nbest
from MyCryptanalysis.ngram_score import calc_score

def Attack_Caesar(ciphertext):
	attempts = nbest(3)
	for key in range(0, 26):
		attempts.add(key, calc_score( Caesar(key).decrypt(ciphertext)))

	for i in range(3):
		pair = attempts[i]
		print(str(i+1) + ". Key = " + str(pair[0]) + ", score = " + str(pair[1]))
		print(Caesar(pair[0]).decrypt(ciphertext))
		print("\n\n\n")
		