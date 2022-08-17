#!/usr/bin/env python3
from itertools import zip_longest
import pyperclip as pc # copy = copy to clipboard / paste = paste from clipboard


class list2tsv:
	def __init__(self, text, uniqueStartString=""):
		##  Split string into a list
		lst = self.string2list(text)
		##  Set Separator String, if necessary
		if uniqueStartString == "":
			uniqueStartString = lst[0]
		##  create sublists from main list 
		lst_new = self.createSublists(lst, breakOn=uniqueStartString)
		##  Join lists into a tsv string 
		self.output = self.createTSV(lst_new)
		
	def createTSV(self, lst_new):
		"""createTSV: takes list of lists; returns TSV string"""
		delim = "\t"
		output = ""
		for item in lst_new:
			output += delim.join(item) + "\n"
		return output

	def createSublists(self, lst, breakOn):
		"""createSublists: 
			takes a list and the breakOn token that starts each row
			returns a list of lists with each sublist starting with the breakOn token"""
		indices = [i for i, j in enumerate(lst) if breakOn in j]
		return [lst[i:j] for i, j in zip_longest(indices, indices[1:])]

	def string2list(self, text):
		return text.split('\n')

clip = pc.paste() # get the clipboard
clipboard = list2tsv(clip) # transform
pc.copy(clipboard.output) # put result on clipboard
print(clipboard.output) # show the world

