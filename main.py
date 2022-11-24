import MyCiphers as Ciph

plaintext = "defend the east wall of the castle"
key = "HELLO"
cipher = Ciph.Autokey(key).encrypt(plaintext)
print(cipher)


print(Ciph.Autokey(key).decrypt(cipher))


print("done")