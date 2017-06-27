#!/usr/bin/env python3

if __name__ == "__main__":
	print("This shouldn't be executed liked that.")
	exit(1)

class Cipher:
	def __init__(self, cipher_name):
		self.name = cipher_name

	def encrypt(self, plaintext: str, key: str) -> str:
		raise NotImplementedError("Cipher.encrypt(plaintext: str, key: str) is abstract.")

	def encrypt(self, plaintext: str, n: int) -> str:
		raise NotImplementedError("Cipher.encrypt(plaintext: str, key: int) is abstract.")

	def decrypt(self, ciphertext: str, key: str) -> str:
		raise NotImplementedError("Cipher.decrypt(ciphertext: str, key: str) is abstract.")

	def decrypt(self, ciphertext: str, n: int) -> str:
		raise NotImplementedError("Cipher.decrypt(ciphertext: str, key: int) is abstract.")
