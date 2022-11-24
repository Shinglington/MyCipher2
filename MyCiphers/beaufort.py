from MyCiphers.cipher import Cipher
from MyCiphers.caesar import Caesar


class Beaufort(Cipher):
	def __init__(self, key):
		Cipher.__init__(self)
		self.key = key.upper()

	def encrypt(self, plaintext, keep_punct=False):
		text = self.remove_punct(plaintext)
		ciphertext = ""
		for i in range(len(text)):
			keychar = self.key[i % len(self.key)]
			column_number = self.char_to_int(text[i])
			ciphertext += self.int_to_char(Caesar(column_number).encrypt(self.alphabet_upper).index(keychar))

		if keep_punct:
			ciphertext = self.restore_punct(ciphertext, plaintext)
		return ciphertext

	def decrypt(self, ciphertext, keep_punct=False):
		return self.encrypt(ciphertext, keep_punct)

