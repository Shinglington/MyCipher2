from MyCiphers.cipher import Cipher

class Baconian(Cipher):
	def __init__(self, A = "A", B = "B"):
		self.A = A
		self.B = B
		Cipher.__init__(self)

	def encrypt(self, plaintext):
		text = self.remove_punct(plaintext)
		ciphertext = ""
		for c in text:
			binary = bin(self.char_to_int(c))
			ciphertext += str(binary).replace("0b", "").zfill(5).replace("0", self.A).replace("1", self.B)
		return ciphertext

	def decrypt(self, ciphertext):
		text = self.remove_punct(ciphertext, keep = self.A + self.B)
		plaintext = ""
		for i in range(0, len(text), 5):
			binary = text[i:i+5].replace(self.A, "0").replace(self.B, "1")
			plaintext += self.int_to_char(int("0b" + binary, base = 0))
		return plaintext