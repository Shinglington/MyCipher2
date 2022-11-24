import MyCiphers as Ciph

plaintext = "we are discovered save yourself"
key = "MONARCHY"
cipher = Ciph.Playfair(key).encrypt(plaintext)
print(cipher)


print(Ciph.Playfair(key).decrypt(cipher))


print("done")