import random
from MyCryptanalysis.ngram_score import calc_score

def Attack_UnknownTrans(ciphertext):
	## Hill climbing
	length = len(ciphertext)
	best_key = []
	best_score = -99e9
	key_streak = 0
	while (key_streak < 10):
		current_key = GetRandomKey(length)
		current_score = calc_score(DecryptUnknown(ciphertext, current_key))
		iterations = 0
		while (iterations < 1000):
			new_key = AlterKey(current_key)
			score = calc_score((DecryptUnknown(ciphertext, new_key)))
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
			print((DecryptUnknown(ciphertext, new_key)))
			print("Key = {0}".format(best_key))
			print("\n\n\n")
			key_streak = 0
		else:
			key_streak += 1

	print("\n\n\n")
	print("Key ={0}, score = {1}".format(best_key, best_score))
	print((DecryptUnknown(ciphertext, new_key)))
	



def GetRandomKey(length):
	key = []
	remaining = list(range(length))
	for j in range(length):
		key_char = remaining[random.randint(0, len(remaining) - 1)]
		key.append(key_char)
		remaining.remove(key_char)
	return key

def AlterKey(key):
	new_key = []
	a = random.randint(0, len(key) - 1)
	b = random.randint(0, len(key) - 1)
	for j in range(len(key)):
		if j == a:
			new_key.append(key[b])
		elif j == b:
			new_key.append(key[a])
		else:
			new_key.append(key[j])
	return new_key


def DecryptUnknown(text, key):
	assert len(text) == len(key)
	decryption = [None] * len(text)
	for i in range(len(text)):
		decryption[i] = text[key[i]]
	return ''.join(decryption)