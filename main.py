import MyCiphers as Ciph

plaintext = "defend the east wall of the castle"
key = "phqgiumeaylnofdxkrcvstzwb".upper()

cipher = Ciph.PolybiusSquare(key).encrypt(plaintext)
print(cipher)

print(Ciph.PolybiusSquare(key).decrypt(cipher))


print("done")