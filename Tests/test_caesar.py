from MyCiphers.caesar import Caesar
from Tests.test_cipher import CipherTest

def CaesarTest(CipherTest):

	def encrypt_test():
		plaintext = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		encryptions= {
			0:"abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz",
			1:"bcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyza",
			5:"fghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcde",
			12:"mnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijkl",
			25:"zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxy"
		}
		for k, v in encryptions.items():
			encrypt = Caesar(k).encrypt(v)
			assert(encrypt.upper() == v.upper())

	def decrypt_test():
		pass


	def punct_test():
		pass
