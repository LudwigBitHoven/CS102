def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    res = ''
    key = key.upper()
    for i in range(len(a)):
        if a[i].isalpha():
            if ord(a[i]) + ord(key[i % len(key)]) - 65 > 122 and a[i].islower() or ord(a[i]) + ord(key[i % len(key)]) - 65 > 90 and a[i].isupper():
                res += chr(ord(a[i]) + ord(key[i % len(key)]) - 65 - 26)
            else:
                res += chr(ord(a[i]) + ord(key[i % len(key)]) - 65)
        else:
            res += a[i]
    return res


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    res = ''
    key = key.upper()
    for i in range(len(a)):
        if a[i].isalpha():
            if ord(a[i]) - ord(key[i % len(key)]) + 65 < 97 and a[i].islower() or ord(a[i]) - ord(key[i % len(key)]) + 65 < 65 and a[i].isupper():
                res += chr(ord(a[i]) - ord(key[i % len(key)]) + 65 + 26)
            else:
                res += chr(ord(a[i]) - ord(key[i % len(key)]) + 65)
        else:
            res += a[i]
    return res
