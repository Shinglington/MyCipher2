import random
from MyCiphers import SimpleSub
from MyCryptanalysis.ngram_score import calc_score



def Attack_SimpleSub(ciphertext):
	print("attempting to crack substitution cipher")
	## Hill climbing
	best_key = ""
	best_score = -99e9
	key_streak = 0
	while (key_streak < 5):
		current_key = GetRandomKey()
		current_score = calc_score(SimpleSub(current_key).decrypt(ciphertext))
		iterations = 0
		while (iterations < 1000):
			new_key = AlterKey(current_key)
			score = calc_score(SimpleSub(new_key).decrypt(ciphertext))
			if score > current_score:
				print("Updated key to {0}".format(new_key))
				current_key = new_key
				current_score = score
				iterations = 0
			iterations += 1

		if current_score > best_score:
			best_score = current_score
			best_key = current_key
			print("Score is currently {0}".format(best_score))
			print(SimpleSub(best_key).decrypt(ciphertext))
			print("Key = {0}".format(best_key))
			print("\n\n\n")
			key_streak = 0
		else:
			key_streak += 1

	print("\n\n\n")
	print("Final Best Key:")
	print("Key ={0}, score = {1}".format(best_key, best_score))
	print(SimpleSub(best_key).decrypt(ciphertext))
	


def GetRandomKey():
	key = ""
	remaining_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	for j in range(0,26):
		key_char = remaining_alphabet[random.randint(0, len(remaining_alphabet) - 1)]
		key += key_char
		remaining_alphabet = remaining_alphabet.replace(key_char, "")
	return key

def AlterKey(key):
	new_key = ""
	a = random.randint(0, 25)
	b = random.randint(0, 25)
	for j in range(len(key)):
		if j == a:
			new_key += key[b]
		elif j == b:
			new_key += key[a]
		else:
			new_key += key[j]
	return new_key
	
	