from MyCiphers.cipher import Cipher

class ColTrans(Cipher):
	def __init__(self, key):
		self.key = key.upper()
		
		self.enc_index = self.get_indexed_key()
		self.dec_index = self.get_inverse_index()

	def encrypt(self, plaintext, keep_punct = False):

		text = self.remove_punct(plaintext)
		ciphertext = ""

		# Pad text
		while (len(text) % len(self.key) != 0):
			text += "X"

		row_count = len(text) / len(self.key)
		for i in range(0, row_count):
			row = ""
			for j in range(len(self.key)):
				row += text[i+(j*row_count)]
			for k in range(len(self.key)):
				ciphertext += original[self.enc_index[k]]

		if keep_punct:
			ciphertext = self.restore_punct(plaintext, ciphertext)
		return ciphertext

		
	def decrypt(self, ciphertext, keep_punct = False):		
		text = self.remove_punct(ciphertext)
		plaintext = ""

		row_count = len(text) / len(self.key)
		for i in range(0, row_count):
			row = ""
			for j in range(len(self.key)):
				row += text[i+(j*row_count)]
			for k in range(len(self.key)):
				plaintext += original[self.dec_index[k]]

		if keep_punct:
			plaintext = self.restore_punct(ciphertext, plaintext)
		return plaintext


	def get_indexed_key(self):
		index_to_key = {}
		for i in len(self.key):
			index_to_key.update({i:self.key[i]})
		return dict(sorted(index_to_key.items(), key = lambda item: item[1])).keys()

	def get_inverse_index(self):
		inverse_index = []
		for i in len(self.key):
			inverse_index[i] = self.enc_index[i]
		return inverse_index
		
		