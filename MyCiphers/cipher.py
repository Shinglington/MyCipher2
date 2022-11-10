
class Cipher():
	def __init__(self):
		self.alphabet_upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.alphabet_lower = "abcdefghijklmnopqrstuvwxyz"
	
	def encrypt(self, string):
		return string

	def decrypt(self, string):
		return string

	def char_to_int(self, char):
		char = char.upper()
		return self.alphabet_upper.index(char)

	def int_to_char(self, i):
		i = i%len(self.alphabet_upper)
		return self.alphabet_upper[i]

	def remove_punct(self, text, keep = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
		output = ""
		for c in text:
			if c in keep:
				output += c
		return output