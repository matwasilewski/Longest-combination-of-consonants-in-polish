#!Python3
# -*- coding: utf-8 -*-
import sys 

class Vowels:
	# Initializes class. Assigns dictionary and output files to separate variables. Declares which letters are vowels.
	def __init__(self, dictionary, outputfile, vowelless_file):
		self.dictionary = dictionary
		self.outputfile = outputfile
		self.vowelless_file = vowelless_file
		self.vowels = ['e', 'y', 'u', 'i', 'o', 'a', 'ą', 'ę', 'ó']

	# Reads words from dictionary file to a list dictionary_list
	def dictionary_to_list(self):
		words_list = []
		file = open(self.dictionary, 'r')
		for element in file:
			words_list.append(element)
		file.close()
		self.words_list = words_list

	# Finds words which have no vowels, and adds them to the list self.vowelless
	def no_vowels(self):
		self.vowelless = []
		for element in self.words_list:
			appears = False
			for i in self.vowels:
				if i in element:
					appears = True
					break
				else:
					continue
			if appears == False:
				self.vowelless.append(element)

	# Prints vowelless to a file, declared by command line
	def print_vowelless(self, file):
		f = open(file, 'w')
		for element in self.vowelless:
			f.write(element)
		f.close()

	# creates a dictionary with words having sequence of consonants at the beginning of given lenght
	def starting_consonants(self):
		longest_start = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : []}
		for word in self.words_list:
			check = 0
			for position, letter in enumerate(word):
				if letter in self.vowels:
					check = position
					break
				elif position + 1 == len(word):
					check = position + 1
				else:
					check = position
				print(position)
			longest_start[int(check)].append(str(word))
		print(longest_start)





vowelless_file = sys.argv[1]
instance = Vowels('slowa.txt', 'test.txt', sys.argv[1])
instance.dictionary_to_list()
instance.no_vowels()
instance.print_vowelless(instance.vowelless_file)
instance.starting_consonants()
