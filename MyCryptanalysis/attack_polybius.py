from MyCryptanalysis.attack_simplesub import Attack_SimpleSub

def Attack_Polybius(ciphertext):
	print("Attempting to attack polybius cipher by converting it to simple substitution")
	text = ciphertext.replace(" ","").upper()
	assert len(text) % 2 == 0, "Polybius ciphertext must be even"
	alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	pairs_to_singles = {}
	new_text = ""

	for i in range(0, len(text), 2):
		pair = text[i:i+2]
		if pair not in pairs_to_singles.keys():
			pairs_to_singles.update({pair:alphabet[len(list(pairs_to_singles.keys()))]})
		new_text += pairs_to_singles[pair]

	Attack_SimpleSub(new_text)
	
	