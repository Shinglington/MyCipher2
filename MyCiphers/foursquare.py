from MyCiphers.cipher import Cipher

class FourSquare(Cipher):
	def __init__(self, key1, key2, alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"):
		Cipher.__init__(self)
		# Generate square
		self.plainsquare = alphabet
		self.square1 = self.create_square(key1, alphabet)
		self.square2 = self.create_square(key2, alphabet)

	def create_square(self, key, alphabet):
		square = ""
		for c in key.upper():
			if c not in square:
				square += c
		for c in alphabet:
			if c not in square:
				square += c
		return square		

	def encrypt_pair(self, a, b):
		row_a = int(self.plainsquare.index(a) / 5)
		col_a = int(self.plainsquare.index(a) % 5)

		row_b = int(self.plainsquare.index(b) / 5)
		col_b = int(self.plainsquare.index(b) % 5)

		return self.square1[row_a * 5 + col_b] + self.square2[row_b * 5 + col_a]

		
		

	def decrypt_pair(self, a, b):
		row_a = int(self.square1.index(a) / 5)
		col_a = int(self.square1.index(a) % 5)

		row_b = int(self.square2.index(b) / 5)
		col_b = int(self.square2.index(b) % 5)

		return self.plainsquare[row_a * 5 + col_b] + self.plainsquare[row_b * 5 + col_a]

	def encrypt(self, plaintext, keep_punct = False):
		text = self.remove_punct(plaintext).replace("J", "I")
		ciphertext = ""
		if (len(text) % 2 != 0):
			text += "X"
			
		for i in range(0, len(text), 2):
			ciphertext += self.encrypt_pair(text[i], text[i+1])

		if keep_punct:
			ciphertext = self.restore_punct(ciphertext, plaintext)
		return ciphertext
			
		

	def decrypt(self, ciphertext, keep_punct = False):
		text = self.remove_punct(ciphertext)
		assert len(text) % 2 == 0, "Length of text must be even"
		plaintext = ""
		for i in range(0, len(text), 2):
			plaintext += self.decrypt_pair(text[i], text[i+1])
		
		if keep_punct:
			plaintext = self.restore_punct(plaintext, ciphertext)
		return plaintext

		