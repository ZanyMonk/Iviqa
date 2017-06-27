#!/usr/bin/env python3

if __name__ == "__main__":
	print("This shouldn't be executed liked that.")
	exit(1)

from ciphers.Iviqa import Iviqa
from ciphers.Rot import Rot
from ciphers.OneTimePad import OneTimePad

ciphers = {
	'Iviqa': Iviqa(),
	'Rot': Rot(),
	'OneTimePad': OneTimePad()
}
