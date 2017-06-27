#!/usr/bin/env python3

from ciphers.Ciphers import ciphers

plaintext = "I can resist anything except temptation"
str_key = "The greatest knowledge is to know that we are surrounded by mystery"
int_key = 3

for i in ciphers.keys():
	print(i + " :")
	print("\t plain     : " + plaintext)
	if ciphers[i].key_type == str:
		encrypted = ciphers[i].encrypt(plaintext, str_key)
		print("\t encrypted : " + encrypted)
		print("\t decrypted : " + ciphers[i].decrypt(encrypted, str_key))
	elif ciphers[i].key_type == int:
		encrypted = ciphers[i].encrypt(plaintext, int_key)
		print("\t encrypted : " + encrypted)
		print("\t decrypted : " + ciphers[i].decrypt(encrypted, int_key))
