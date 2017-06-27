#!/usr/bin/env python3

if __name__ == "__main__":
	print("This shouldn't be executed liked that.")
	exit(1)

def is_alpha(s: str) -> bool:
	b = True

	for c in s:
		i = ord(c)
		if i < 65 or i > 90 and i < 97 or i > 122:
			b = False
			break

	return b

def strip_accents(s: str) -> str:
	r = ""

	for c in s:
		if c in list("éèëê"):
			r += "e"
		elif c in list("îïìí"):
			r += "i"
		elif c in list("àâàáâãäå"):
			r += "a"
		elif c in list("ôòóôõö"):
			r += "o"
		elif c in list("ûùúûü"):
			r += "u"
		else:
			r += c

	return r
