import MyCiphers as Ciph

plaintext = "defend the east wall of the castle"

cipher = Ciph.Baconian().encrypt(plaintext)
print(cipher)

cipher = "AABBBAABAAABABAABABAABBAB"

print(Ciph.Baconian().decrypt(cipher))


print("done")