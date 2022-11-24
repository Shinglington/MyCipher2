import MyCiphers as Ciph

plaintext = "defend the east wall of the castle"
key = "FORTIFICATION"
cipher = Ciph.Beaufort(key).encrypt(plaintext)
print(cipher)


print(Ciph.Beaufort(key).decrypt(cipher))


print("done")