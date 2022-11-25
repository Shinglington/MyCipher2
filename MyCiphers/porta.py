from MyCiphers.cipher import Cipher
from MyCiphers.cipher import Caesar
class Porta(Cipher):
	def __init__(self, key):
		Cipher.__init__(self)
		self.key = key.upper()
		self.tableau = self.generate_tableau

	def generate_tableau(self):
		pass
	

	def encrypt(self, plaintext, keep_punct = False):
		text = self.remove_punct(plaintext)
		ciphertext = ""
		for i in range(len(text)):
			key_char = self.key[i%len(self.key)]
			cipher_row = int(self.char_to_int(key_char) / 2)
			cipher_alphabet = Caesar(cipher_row + 13)
			ciphertext += self.char_to_int(key_char) % 13

		if keep_punct:
			ciphertext = self.restore_punct(ciphertext, plaintext)

	def decrypt(self, ciphertext, keep_punct = False):
		text = self.remove_punct(ciphertext)
		plaintext = ""
  		for i in range(len(text):
			plaintext += text[i]

		if keep_punct:
			plaintext = self.restore_punct(plaintext, ciphertext)
		return plaintext