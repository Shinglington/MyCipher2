import MyCiphers as Ciph

keyword = "GERMAN"
ciphertext = "defend the east wall of the castle"

text = Ciph.RowTrans(keyword).encrypt(ciphertext)
print(text)
print(Ciph.RowTrans(keyword).decrypt(text))

print("done")