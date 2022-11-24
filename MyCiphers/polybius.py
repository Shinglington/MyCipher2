from MyCiphers.cipher import Cipher

class PolybiusSquare(Cipher):
	def __init__(self, square = "ABCDEFGHIKLMNOPQRSTUVWXYZ", size = 5, chars = None):
		Cipher.__init__(self)
		self.square = square
		self.size = size
		self.chars = chars or "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[:size]
		assert len(self.square) == size ** 2
		assert len(self.chars) == size


	def encrypt_char(self, char):
		row = int(self.square.index(char) / self.size)
		col = (self.square.index(char) % self.size)
		return self.chars[row] + self.chars[col]

	def decrypt_pair(self, pair):
		row = self.chars.index(pair[0])
		col = self.chars.index(pair[1])
		return self.square[row*self.size + col]
	
	def encrypt(self, plaintext):
		text = self.remove_punct(plaintext).replace("J", "I")
		ciphertext = ""
		for i in range(len(text),):
			ciphertext += self.encrypt_char(text[i])
		return ciphertext
		
	def decrypt(self, ciphertext):
		text = self.remove_punct(ciphertext)
		plaintext = ""
		for i in range(0, len(text), 2):
			pair = text[i:i+2]
			plaintext += self.decrypt_pair(pair)
		return plaintext
		