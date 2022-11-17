from MyCiphers.cipher import Cipher

class Affine(Cipher):
	def __init__(self, a, b):
		self.a = a
		self.b = b
		self.inverse_a = -1
		for inv in range(1, 26, 2):
			if (self.a * inv) % 26 == 1:
				self.inverse_a = inv
				break

		Cipher.__init__(self)
		assert 0 <= self.inverse_a <= 25, "No inverse for key a = " + str(self.a)
		
	

	def encrypt(self, plaintext, keep_punct = False):
		text = self.remove_punct(plaintext)
		ciphertext = ""
		for c in text:
			ciphertext += self.int_to_char(self.a * self.char_to_int(c) + self.b)
		if keep_punct:
			ciphertext = self.restore_punct(ciphertext, plaintext)
		return ciphertext

	def decrypt(self, ciphertext, keep_punct = False):
		text = self.remove_punct(ciphertext)
		plaintext = ""
		for c in text:
			plaintext += self.int_to_char(self.inverse_a * (self.char_to_int(c) - self.b))
		if keep_punct:
			plaintext = self.restore_punct(plaintext, ciphertext)
		return plaintext