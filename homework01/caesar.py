import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    for i in plaintext:
        if i.isalpha():
            if (
                ord(i) + shift % 26 > ord("z")
                and i.islower()
                or ord(i) + shift % 26 > ord("Z")
                and i.isupper()
            ):
                ciphertext += chr(ord(i) + shift % 26 - 26)
            elif shift < 0 and (
                ord(i) + shift % 26 < ord("a")
                and i.islower()
                or ord(i) + shift % 26 < ord("A")
                and i.isupper()
            ):
                ciphertext += chr(ord(i) + shift % 26 + 26)
            else:
                ciphertext += chr(ord(i) + shift % 26)
        else:
            ciphertext += chr(ord(i))
    return ciphertext


"""Функция идентична encrypt_caesar, но shift берется с
противоположным знаком
"""


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    shift = -shift
    plaintext = ""
    for i in ciphertext:
        if i.isalpha():
            if (
                ord(i) + shift % 26 > ord("z")
                and i.islower()
                or ord(i) + shift % 26 > ord("Z")
                and i.isupper()
            ):
                plaintext += chr(ord(i) + shift % 26 - 26)
            elif shift < 0 and (
                ord(i) + shift % 26 < ord("a")
                and i.islower()
                or ord(i) + shift % 26 < ord("A")
                and i.isupper()
            ):
                plaintext += chr(ord(i) + shift % 26 + 26)
            else:
                plaintext += chr(ord(i) + shift % 26)
        else:
            plaintext += chr(ord(i))
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    return best_shift
