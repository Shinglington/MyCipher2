from MyCiphers.cipher import Cipher

class SimpleSub(Cipher):
	def __init__(self, key):
		Cipher.__init__()
		cipher_alphabet = ""
		for c in key.upper():
			if c not in cipher_alphabet:
				cipher_alphabet += c
		for c in self.alphabet_upper():
			if c not in cipher_alphabet:
				cipher_alphabet += c
		self.key = cipher_alphabet

	
	
	def encrypt(self, plaintext, keep_punct = False):
		text = self.remove_punct(plaintext)
		ciphertext = ""
		for c in text:
			ciphertext += self.int_to_char(self.key.index(c))
		
		return ciphertext

	def decrypt(self, ciphertext, keep_punct = False):
		text = self.remove_punct(ciphertext)
		plaintext = ""
		return plaintext
