import MyCiphers as Ciph

plaintext = "act"
key = "GYBNQKURP"
cipher = Ciph.Hill(key).encrypt(plaintext)
print(cipher)


print(Ciph.Hill(key).decrypt(cipher))


print("done")