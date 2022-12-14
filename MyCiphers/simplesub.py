from MyCiphers.cipher import Cipher


class SimpleSub(Cipher):

	def __init__(self, key):
		Cipher.__init__(self)
		cipher_alphabet = ""
		for c in key.upper():
			if c not in cipher_alphabet:
				cipher_alphabet += c
		for c in self.alphabet_upper:
			if c not in cipher_alphabet:
				cipher_alphabet += c
		self.key = cipher_alphabet

	def encrypt(self, plaintext, keep_punct=False):
		text = self.remove_punct(plaintext)
		ciphertext = ""
		for c in text:
			ciphertext += self.key[self.char_to_int(c)]
		if keep_punct:
			ciphertext = self.restore_punct(ciphertext, plaintext)
		return ciphertext

	def decrypt(self, ciphertext, keep_punct=False):
		text = self.remove_punct(ciphertext)
		plaintext = ""
		for c in text:
			plaintext += self.int_to_char(self.key.index(c))
		if keep_punct:
			plaintext = self.restore_punct(plaintext, ciphertext)
		return plaintext
