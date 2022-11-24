from MyCiphers.cipher import Cipher

class Railfence(Cipher):
	def __init__(self, key):
		Cipher.__init__(self)
		self.key = key


	def encrypt(self, plaintext, keep_punct = False):
		text = self.remove_punct(plaintext)
		ciphertext = ""
		fence = self.make_fence(text)
		for row in fence:
			ciphertext += ''.join(row)
		
		if keep_punct:
			ciphertext = self.restore_punct(ciphertext, plaintext)
		return ciphertext

	def decrypt(self, ciphertext, keep_punct = True):
		text = self.remove_punct(ciphertext)
		plaintext = [""] * len(text)
		fence = self.make_fence(range(len(text)))
		c_index = 0
		for row in fence:
			for item in row:
				if item != "":
					plaintext[item] = ciphertext[c_index]
					c_index += 1
		if keep_punct:
			plaintext = self.restore_punct(plaintext, ciphertext)
		return plaintext

	def make_fence(self, text):
		fence =[[""] * len(text) for row in range(self.key)]
		rail = 0
		descending = True
		for i in range(len(text)):
			fence[rail][i] = text[i]
			## check if descending state needs changing
			if rail + 1 >= self.key and descending:
				descending = False
			elif rail - 1 < 0 and not descending:
				descending = True
			## increment or decrement rail
			if descending:
				rail += 1	
			else:
				rail -= 1
				
		return fence