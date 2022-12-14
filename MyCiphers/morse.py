from MyCiphers.cipher import Cipher

class Morse(Cipher):
	
	CHAR_TO_CODE = {'A': '.-',     'B': '-...',   'C': '-.-.', 
						        'D': '-..',    'E': '.',      'F': '..-.',
						        'G': '--.',    'H': '....',   'I': '..',
						        'J': '.---',   'K': '-.-',    'L': '.-..',
						        'M': '--',     'N': '-.',     'O': '---',
						        'P': '.--.',   'Q': '--.-',   'R': '.-.',
						        'S': '...',    'T': '-',      'U': '..-',
						        'V': '...-',   'W': '.--',    'X': '-..-',
						        'Y': '-.--',   'Z': '--..',
						
						        '0': '-----',  '1': '.----',  '2': '..---',
						        '3': '...--',  '4': '....-',  '5': '.....',
						        '6': '-....',  '7': '--...',  '8': '---..',
						        '9': '----.' 
						        }
	CODE_TO_CHAR = {value:key for key,value in CHAR_TO_CODE.items()}
	
	def __init__(self, dot = '.', dash = '-'):
		Cipher.__init__(self, "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789")
		self.dot = dot
		self.dash = dash

	def encrypt(self, plaintext):
		text = self.remove_punct(plaintext)
		ciphertext = ""
		for c in text:
			ciphertext += self.CHAR_TO_CODE[c.upper()]
			ciphertext += " "
		
		return ciphertext.strip(" ")

	def decrypt(self, ciphertext):
		text = ciphertext.replace(self.dot, '.').replace(self.dash, '-')
		plaintext = ""
		codes = text.split(' ')
		for morse in codes:
			plaintext += self.CODE_TO_CHAR[morse]
		return plaintext
		
		