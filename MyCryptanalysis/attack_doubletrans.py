import random
from MyCiphers.rowtrans import RowTrans
from MyCiphers.coltrans import ColTrans
from MyCryptanalysis.ngram_score import calc_score

def Attack_DoubleColTrans(ciphertext, keylen1, keylen2):
	def alg(ciphertext, key1, key2):
		return ColTrans(key1).decrypt(ColTrans(key2).decrypt(ciphertext))
	Hill_Climb(ciphertext, keylen1, keylen2, alg)

def Attack_DoubleRowTrans(ciphertext, keylen1, keylen2):
	def alg(ciphertext, key1, key2):
		return RowTrans(key1).decrypt(RowTrans(key2).decrypt(ciphertext))
	Hill_Climb(ciphertext, keylen1, keylen2, alg)


def Attack_RowColTrans(ciphertext, rowkeylen, colkeylen):
	def alg(ciphertext, key1, key2):
		return RowTrans(key1).decrypt(ColTrans(key2).decrypt(ciphertext))
	Hill_Climb(ciphertext, rowkeylen, colkeylen, alg)

def Attack_ColRowTrans(ciphertext, colkeylen, rowkeylen):
	def alg(ciphertext, key1, key2):
		return ColTrans(key1).decrypt(RowTrans(key2).decrypt(ciphertext))
	Hill_Climb(ciphertext, colkeylen, rowkeylen,  alg)

def Hill_Climb(ciphertext, keylen1, keylen2, decryptalg):
	best_key = []
	best_score = -99e9
	key_streak = 0
	while (key_streak < 10):
		current_key = [GetRandomKey(keylen1), GetRandomKey(keylen2)]
		current_score = calc_score(decryptalg(ciphertext, current_key[0], current_key[1]))
		iterations = 0
		while (iterations < 1000):
			new_key = current_key
			if random.randint(0,1) ==  1:
				new_key = [AlterKey(current_key[0]), current_key[1]]
			else:
				new_key = [current_key[0], AlterKey(current_key[1])]
			score = calc_score(decryptalg(ciphertext, new_key[0], new_key[1]))
			if score > current_score:
				current_key = new_key
				current_score = score
				iterations = 0
			iterations += 1

		if current_score > best_score:
			best_score = current_score
			best_key = current_key
			print("Score is currently {0}".format(best_score))
			print(decryptalg(ciphertext, best_key[0], best_key[1]))
			print("Key = {0}".format(best_key))
			print("\n\n\n")
			key_streak = 0
		else:
			print("Keystreak is now " + str(key_streak+1))
			key_streak += 1

	print("\n\n\n")
	print("Key ={0}, score = {1}".format(best_key, best_score))
	print(decryptalg(ciphertext, best_key[0], best_key[1]))


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
	
	
	