import MyCiphers as Ciph

a = 5
b = 3

text = Ciph.Affine(a, b).encrypt("defend the east wall of the castle",True)
print(text)
print(Ciph.Affine(a, b).decrypt(text,True))



print("done")