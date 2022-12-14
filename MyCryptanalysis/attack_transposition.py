import random
from itertools import permutations
from MyCiphers.rowtrans import RowTrans
from MyCiphers.coltrans import ColTrans
from MyCryptanalysis.nbest import nbest
from MyCryptanalysis.ngram_score import calc_score

def Attack_ColTrans(ciphertext, keylen = None):
	print("Attempting the attack column transposition cipher")
	def alg(ciphertext, key):
		return ColTrans(key).decrypt(ciphertext)

	attack_trans(ciphertext, keylen, alg)


def Attack_RowTrans(ciphertext, keylen = None):
	print("Attempting the attack row transposition cipher")
	def alg(ciphertext, key):
		return RowTrans(key).decrypt(ciphertext)
		
	attack_trans(ciphertext, keylen, alg)



def attack_trans(ciphertext, keylen, decryptalg):
	best_keys = nbest(5)
	if keylen == None:
		for i in range(2, 21):
			print("\n\n\n\n\n\n")
			print("Trying key length " + str(i))
			temp_keys = get_best_keys(ciphertext, i, decryptalg)
			for i in range(len(best_keys)):
				pair = best_keys[i]
				print(str(i+1) + ". Key = " + str(pair[0]) + ", score = " + str(pair[1]))
				print(decryptalg(ciphertext, pair[0]))
				print("\n\n\n")
				
			for j in range(len(temp_keys)):
				pair = temp_keys[j]
				best_keys.add(pair[0],pair[1])
			
	else:
		best_keys = get_best_keys(ciphertext, keylen, decryptalg)

	for i in range(len(best_keys)):
		pair = best_keys[i]
		print(str(i+1) + ". Key = " + str(pair[0]) + ", score = " + str(pair[1]))
		print(decryptalg(ciphertext, pair[0]))
		print("\n\n\n")

def get_best_keys(ciphertext, keylen, decryptalg):
	best_keys = nbest(5)
	if keylen < 9:
		for perm in permutations(list(range(keylen))):
			key = list(perm)
			best_keys.add(key, decryptalg(ciphertext, key))
	else:
		best_keys = Hill_Climb(ciphertext, keylen, decryptalg)
	return best_keys


def Hill_Climb(ciphertext, keylen, decryptalg):
	best_keys = nbest(5)
	best_keys.add("",-99e9)
	key_streak = 0
	while (key_streak < 10):
		current_key = GetRandomKey(keylen)
		current_score = calc_score(decryptalg(ciphertext, current_key))
		iterations = 0
		while (iterations < 1000):
			new_key = AlterKey(current_key)
			score = calc_score(decryptalg(ciphertext, new_key))
			if score > current_score:
				current_key = new_key
				current_score = score
				iterations = 0
			iterations += 1
		if current_score > best_keys[0][1]:
			print("Score is currently {0}".format(current_score))
			print(decryptalg(ciphertext, current_key))
			print("Key = {0}".format(current_key))
			print("\n\n\n")
			key_streak = 0
		else:
			print("Keystreak is now " + str(key_streak+1))
			key_streak += 1
		best_keys.add(current_key, current_score)



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