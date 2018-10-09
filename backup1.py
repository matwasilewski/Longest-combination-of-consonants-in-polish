#!Python3
# -*- coding: utf-8 -*-
import sys 

class Vowels:
	# Initializes class. Assigns dictionary and output files to separate variables. Declares which letters are vowels.
	def __init__(self, dictionary, outputfile):
		self.dictionary = dictionary
		self.outputfile = outputfile
		print self.outputfile
		self.vowels = ['e', 'y', 'u', 'i', 'o', 'a', 'ą', 'ę', 'ó']

	# Reads words from dictionary file to a list dictionary_list
	def dictionary_to_list(self):
		words_list = []
		file = open(self.outputfile, 'r')
		for element in file:
			words_list.append(element)
		file.close()
		self.words_list = words_list

instance = Vowels('slowa.txt', 'test.txt')
instance.dictionary_to_list()
print instance.words_list	