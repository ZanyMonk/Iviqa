#!/usr/bin/env python3

if __name__ == "__main__":
	print("This shouldn't be executed liked that.")
	exit(1)

from ciphers.Cipher import Cipher
from utils.strings import *

class Iviqa(Cipher):
	def __init__(self):
		super().__init__("Iviqa", str)

	def __crypt(self, text: str, key: str, encrypt: bool) -> str:
		text = text.lower()
		key = strip_accents(key)

		s = ""
		d = -1 if not encrypt else 1
		x = 0

		for i in range(len(text)):
			if is_alpha(text[i]):
				a = ord(text[i]) - 96
				b = ord(key[ (i-x) % len(key) ]) - 96
				s += chr((a + b * d - 1) % 26 + 97)
			else:
				s += text[i]
				x += 1

		return s

	def encrypt(self, plaintext: str, key: str) -> str:
		return self.__crypt(plaintext, key, True)

	def decrypt(self, ciphertext: str, key: str) -> str:
		return self.__crypt(ciphertext, key, False)
