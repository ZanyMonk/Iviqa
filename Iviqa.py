#!/usr/bin/env python3

from sys import argv
from utils.strings import is_alpha

from app.App import App

from ciphers import Ciphers
from ciphers.Iviqa import Iviqa
from ciphers.Rot import Rot
from ciphers.OneTimePad import OneTimePad

if __name__ == "__main__":
	# if len(argv) == 1:
	# 	print(Iviqa.decrypt("dap mpul njps wj rzhw nkcf qtay... ggf d jpgkt xti wfv’o jzv au.", "elucubraient"))
	# 	print(Iviqa.decrypt("dap mpul njps gj rzhg naln mcgj... npw d imfbx miz ovq'o iwu ry.", "elucubraient"))
	# 	print(Iviqa.encrypt("you just make me feel like home... but i guess you can't get it.", "elucubraient"))

	app = App("Iviqa", {
		'cipher': {
			'value': "Iviqa",
			'flag': "c",
			'required': False
		},
		'mode': {
			'flag': {
				'd': False,
				'e': True
			},
			'required': True
		},
		'text': {
			'flag': -2,
			'required': True
		},
		'key': {
			'flag': -1,
			'required': True
		}
	})

	app.parseArgs(argv)
	if len(argv) > 1:
		cipher = Iviqa()
		if app.get("cipher") in Ciphers.ciphers.keys():
			cipher = globals()[app.get("cipher")]()
		else:
			raise Exception("Unknown cipher.")

		if app.get("text") == None:
			raise Exception("Missing text.")
		if app.get("key") == None:
			raise Exception("Missing key.")

		result = ""
		if app.get("mode"):
			result = cipher.encrypt(app.get("text"), app.get("key"))
		else:
			result = cipher.decrypt(app.get("text"), app.get("key"))

		print(result)
