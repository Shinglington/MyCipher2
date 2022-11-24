import MyCiphers as Ciph

plaintext = "dCode Morse"

cipher = Ciph.Morse().encrypt(plaintext)
print(cipher)

print(Ciph.Morse().decrypt(cipher))


print("done")