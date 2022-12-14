import random
import math
from MyCiphers.playfair import Playfair
from MyCryptanalysis.ngram_score import calc_score

def Attack_Playfair(ciphertext):
	print("attempting to crack playfair cipher")


	best_key = GetRandomKey()
	best_score = calc_score(Playfair(best_key).decrypt(ciphertext))
	iteration = 0
	keystreak = 0
	while (keystreak < 3):
		iteration += 1
		new_key = Simulated_Annealing(ciphertext, best_key)
		new_score = calc_score(Playfair(new_key).decrypt(ciphertext))
		if new_score > best_score:
			best_score = new_score
			best_key = new_key
			print("Updated key during iteration " + str(iteration))
			print("Best score so far is {0} on iteration {1}".format(best_score, iteration))
			keystreak = 0
		else:
			keystreak += 1
		print("Key = " + best_key)
		print(Playfair(best_key).decrypt(ciphertext))
		print("\n\n\n")

	print("\n\n\n")
	print("Final Best Key:")
	print("Key ={0}, score = {1}".format(best_key, best_score))
	print(Playfair(best_key).decrypt(ciphertext))
	

def Simulated_Annealing(ciphertext, best_key):
	## Simulated Annealing
	COUNT = 10000
	TEMP = 10
	STEP = 0.2
	
	best_score = calc_score(Playfair(best_key).decrypt(ciphertext))
	
	current_score = best_score
	current_key = best_key
	
	T = TEMP
	while T >= 0:
		print("TEMP currently at " + str(T))
		key = best_key
		score = best_score
		for i in range(COUNT):
			key = AlterKey(current_key)
			score = calc_score(Playfair(key).decrypt(ciphertext))
			fitness_dif = score - current_score
			if fitness_dif >= 0:
				current_key = key
				current_score = score
			elif T > 0:
				prob = math.exp(fitness_dif / T)
				if prob > random.random():
					current_key = key
					current_score = score
				
			if current_score > best_score:
				best_score = current_score
				best_key = current_key
		T -= STEP


	return best_key

def GetRandomKey():
	key = ""
	remaining_alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"
	for j in range(0,25):
		key_char = remaining_alphabet[random.randint(0, len(remaining_alphabet) - 1)]
		key += key_char
		remaining_alphabet = remaining_alphabet.replace(key_char, "")
	return key

def AlterKey(key):
	new_key = list(key)
	i = random.randint(0, 30000) % 50
	if i == 0:
		a = random.randint(0, 4)
		b = random.randint(0, 4)
		for j in range(5):
			new_key[a*5 + j] = key[b*5 + j]
			new_key[b*5 + j] = key[a*5 + j]
	elif i ==1:
		a = random.randint(0, 4)
		b = random.randint(0, 4)
		for j in range(5):
			temp = new_key[j*5 + a]
			new_key[j*5 + a] = new_key[j*5 + b]
			new_key[j*5 + b] = temp
	elif i == 2:
		new_key = key[::-1]
	elif i ==3:
		for j in range(5):
			for k in range(5):
				new_key[j*5 + k] = key[(4-j) * 5 + k]
	elif i == 4:
		for j in range(5):
			for k in range(5):
				new_key[j + k*5] = key[j + (4-k)*5]
	else:
		a = random.randint(0, 24)
		b = random.randint(0, 24)
		new_key[a] = key[b]
		new_key[b] = key[a]
	return "".join(new_key)
	
	