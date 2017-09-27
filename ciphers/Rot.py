#!/usr/bin/env python3

if __name__ == "__main__":
	print("This shouldn't be executed liked that.")
	exit(1)

from re import match

from ciphers.Cipher import Cipher
from utils.strings import is_alpha

class Rot(Cipher):
	def __init__(self):
		super().__init__("Rot", int)

	def __crypt(self, text: str, n: int, encrypt: bool) -> str:
		d = -1 if not encrypt else 1
		r = ""
		text = text.lower()

		if match(r"^[0-9]+-[0-9]+$", n):
			values = n.split("-")
			values[0] = int(values[0])
			values[1] = int(values[1])
			if len(values) == 2 or values[0] > 0 or values[0] < 26 or values[1] > 0 or values[1] < 26:
				for i in range(values[0], abs(values[0]-values[1])+1):
					r += "+" + str(i) + ":\t" + "".join([chr((ord(c)-97 + d*int(i))%26+97) if is_alpha(c) else c for c in text]) + "\n"
			else:
				raise Exception("Invalid key. Choose an integer between 1 and 25 or a range like 1-13.")
		elif match(r"^(-?[1-2]?\d,?)+$", n):
			n = n.split(",")
			j = 0
			for i in range(len(text)):
				if is_alpha(text[i]):
					r += chr((ord(text[i])-97 + d*int(n[j%len(n)]))%26+97)
					j += 1
				else:
					r += text[i]
		else:
			raise Exception("Invalid key. Choose an integer between 1 and 25 or a range like 1-13.")

		return r

	def encrypt(self, plaintext: str, n: int) -> str:
		return self.__crypt(plaintext, n, True)

	def decrypt(self, ciphertext: str, n: int) -> str:
		return self.__crypt(ciphertext, n, False)
