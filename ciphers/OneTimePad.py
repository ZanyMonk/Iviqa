#!/usr/bin/env python3

if __name__ == "__main__":
	print("This shouldn't be executed liked that.")
	exit(1)

from ciphers.Cipher import Cipher
from utils.strings import *

class OneTimePad(Cipher):
	def __init__(self):
		super().__init__("OneTimePad", str)

	def __crypt(self, text: str, key: str, encrypt: bool) -> str:
		if len(text) > len(key):
			raise Exception("Key length has to be equal to plaintext or ciphertext length.")
		else:
			text = text.lower()
			key = key.lower()
			d = -1 if not encrypt else 1
			return "".join([chr((ord(text[i])-97+((ord(key[i])-97)*d))%26+97) if is_alpha(text[i]) else text[i] for i in range(len(text))])

	def encrypt(self, plaintext: str, key: str) -> str:
		return self.__crypt(plaintext, key, True)

	def decrypt(self, ciphertext: str, key: str) -> str:
		return self.__crypt(ciphertext, key, False)
