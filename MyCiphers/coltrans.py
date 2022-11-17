from MyCiphers.cipher import Cipher

class ColTrans(Cipher):
	def __init__(self, key):
		self.key = key.upper()
		
		self.num_key= self.get_numerated_key()
		print(self.num_key)

	def encrypt(self, plaintext, keep_punct = False):
		text = self.remove_punct(plaintext)
		cipher_rows = []
		# Pad text
		while (len(text) % len(self.key) != 0):
			text += "X"
			plaintext += "X"
		for i in range(0, len(text), len(self.key)):
			original_row = text[i:i+len(self.key)]
			new_row = [None] * len(self.key)
			for j in range(len(self.key)):
				new_row[j] = original_row[self.num_key[j]]
			print(new_row)
			cipher_rows.append(new_row)
		ciphertext = ""
		for col in range(len(self.key)):
			for row in cipher_rows:
				ciphertext += row[col]
		if keep_punct:
			ciphertext = self.restore_punct(ciphertext, plaintext)
		return ciphertext

		
	def decrypt(self, ciphertext, keep_punct = False):	
		text = self.remove_punct(ciphertext)
		plaintext = ""
		row_count = int(len(text) / len(self.key))
		for i in range(row_count):
			row = [None] * len(self.key)
			for j in range(len(self.key)):
				row[self.num_key[j]] = text[i + (j * row_count)]
			plaintext += ''.join(row)
		if keep_punct:
			plaintext = self.restore_punct(plaintext, ciphertext)
		return plaintext


	def get_numerated_key(self):
		index_to_key = {}
		for i in range(len(self.key)):
			index_to_key.update({i:self.key[i]})
		return list(dict(sorted(index_to_key.items(), key = lambda item: item[1])).keys())

		
		