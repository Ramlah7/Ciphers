def ceaser_cipher(plainText,key):
    ciphered=""
    for i in plainText:
        first=ord('A') if i.isupper() else ord('a')
        ciphered+=chr(((ord(i)+key)-first)%26 +first)
    return ciphered
print(ceaser_cipher('ABCDwxYZ',1))