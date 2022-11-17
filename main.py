import MyCiphers as Ciph

keyword = "ZEBRA"

text = Ciph.ColTrans(keyword).encrypt("attack at dawn", True)
print(text)
print(Ciph.ColTrans(keyword).decrypt(text, True))

print("done")