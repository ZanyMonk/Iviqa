#!/usr/bin/env python3

if __name__ == "__main__":
	print("This shouldn't be executed liked that.")
	exit(1)

class App:
	default_settings = {}

	def __init__(self, _name: str, _settings: dict = None):
		self.name = _name
		self.settings = _settings if _settings != None else self.default_settings

	def get(self, setting: str):
		if setting in self.settings.keys() and "value" in self.settings[setting].keys():
			return self.settings[setting]["value"]
		else:
			return None

	def parseArgs(self, args: list):
		if len(args) == 1:
			self.printUsage()
		else:
			for s in self.settings.keys():
				flag = self.settings[s]["flag"]
				if type(flag) == str:
					a = self.seekArg(args, flag)
					if self.settings[s]["required"] and (a == False or a == None):
						raise Exception("Missing " + s + " parameter.")
					elif a != None and a != False:
						self.settings[s]["value"] = a
				elif type(flag) == int:
					a = self.seekPositionalArg(args, flag)
					if a != False:
						self.settings[s]["value"] = a
					elif self.settings[s]["required"]:
						raise Exception("Missing " + s + " parameter")

				elif type(flag) == dict:
					found = False
					for k in flag.keys():
						a = self.seekArg(args, k)
						if a != False:
							found = True
							self.settings[s]["value"] = flag[k]
							break

					if self.settings[s]["required"] and not found:
						raise Exception("Missing " + s + " parameter.")

	def seekPositionalArg(self, args: list, pos: int):
		if len(args) < pos:
			return False

		a = args[pos]
		if a[0] == "-":
			return None
		else:
			return a

	def seekArg(self, args: list, arg: str):
		for i in range(len(args)):
			if args[i] == "-"+arg:
				if args[i+1][0] == "-":
					return None
				else:
					return args[i+1]

		return False

	def printUsage(self):
		print("""Iviqa

Usage :
	./Iviqa.py -c Iviqa -d "ciphertext" "key"

Options :
	-c			Cipher

Ciphers :
	Rotation		Simple rotation
	Iviqa			Rotation, ordinal from key

Mode :
	-d			decrypt
	-e			encrypt
""")
