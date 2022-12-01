from MyCiphers import Affine
from MyCryptanalysis.nbest import nbest
from MyCryptanalysis.ngram_score import calc_score

def Attack_Affine(ciphertext):
	attempts = nbest(3)
	for a in [1,3,5,7,9,11,15,17,19,21,23,25]:
		for b in range(0, 26):
			attempts.add((a, b), calc_score(Affine(a, b).decrypt(ciphertext)))

	for i in range(3):
		pair = attempts[i]
		print(str(i+1) + ". Key = " + str(pair[0]) + ", score = " + str(pair[1]))
		print(Affine(pair[0][0], pair[0][1]).decrypt(ciphertext))
		print("\n\n\n")
		