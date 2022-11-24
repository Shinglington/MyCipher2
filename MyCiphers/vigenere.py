from MyCiphers.cipher import Cipher
from MyCiphers.caesar import Caesar


class Vigenere(Cipher):

	def __init__(self, key):
		Cipher.__init__(self)
		self.key = key.upper()

	def encrypt(self, plaintext, keep_punct=False):
		text = self.remove_punct(plaintext)
		ciphertext = ""
		for i in range(len(text)):
			keychar = self.key[i % len(self.key)]
			ciphertext += Caesar(self.char_to_int(keychar)).encrypt(text[i])

		if keep_punct:
			ciphertext = self.restore_punct(ciphertext, plaintext)
		return ciphertext

	def decrypt(self, ciphertext, keep_punct=False):
		text = self.remove_punct(ciphertext)
		plaintext = ""
		for i in range(len(text)):
			keychar = self.key[i % len(self.key)]
			plaintext += Caesar(self.char_to_int(keychar)).decrypt(text[i])

		if keep_punct:
			plaintext = self.restore_punct(plaintext, ciphertext)
		return plaintext
