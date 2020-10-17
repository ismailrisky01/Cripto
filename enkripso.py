def eksrip(plaintext):
    ciphertext = ""
    for i in range(len(plaintext)):
        if (plaintext[i].isupper()):
            ciphertext += chr((ord(plaintext[i]) + 7 - 65) % 26 + 65)
        else:
            ciphertext += chr((ord(plaintext[i]) + 7 - 97) % 26 + 97)
    print("plaintext = " + plaintext)
    print("ciphertext = " + ciphertext)
if __name__ == '__main__':
    eksrip("Ismail Risky Rahmansyah")
