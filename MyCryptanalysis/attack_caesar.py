import MyCryptanalysis
from MyCiphers import Caesar

def Attack_Caesar(ciphertext):
	attempts = nbest(3)
	for key in range(0, 26):
		attempts.add(key, calc_score( Caesar(key).decrypt(ciphertext)))

	for i in range(3):
		pair = attempts[i]
		print(i + ". Key = " + pair[0] + ", score = " + pair[1])
		print(Caesar(pair[0]).decrypt(ciphertext))
		print("\n\n\n")
		