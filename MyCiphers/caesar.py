from MyCiphers.cipher import Cipher


class Caesar(Cipher):

	def __init__(self, key):
		self.key = key % 26
		Cipher.__init__(self)

	def encrypt(self, plaintext, keep_punct=False):
		text = self.remove_punct(plaintext)
		ciphertext = ""
		for c in text:
			ciphertext += self.int_to_char(self.char_to_int(c) + self.key)
		if keep_punct:
			ciphertext = self.restore_punct(plaintext, ciphertext)
		return ciphertext

	def decrypt(self, ciphertext, keep_punct=False):
		text = self.remove_punct(ciphertext)
		plaintext = ""
		for c in text:
			plaintext += self.int_to_char(self.char_to_int(c) - self.key)

		if keep_punct:
			plaintext = self.restore_punct(ciphertext, plaintext)
		return plaintext
