#!Python3
# -*- coding: utf-8 -*-
import io
import sys 

class Vowels:
	# Initializes class. Assigns dictionary and output files to separate variables. Declares which letters are vowels.
	# IN: DICTIONARY - file containing all words to be checked, line by line; OUTPUTFILE - file to which the results will ultimately be returned
	# VOWELLESS_FILE - file to which all vowelless words will be returned
	def __init__(self, dictionary, outputfile_start, vowelless_file, outputfile_end):
		self.dictionary = dictionary
		self.outputfile_start = outputfile_start
		self.outputfile_end = outputfile_end
		self.vowelless_file = vowelless_file
		self.vowels = ['e', 'y', 'u', 'i', 'o', 'a', u'ą', u'ę', u'ó']
		# self.vowels = [u'ą']

	# Reads words from dictionary file to a list dictionary_list.
	# INPUT from DICTIONARY
	# OUTPUT to self.words_list
	def dictionary_to_list(self):
		words_list = []
		file = io.open(self.dictionary, 'r', encoding='utf-8')
		for element in file:
			words_list.append(element.rstrip())
		file.close()
		self.words_list = words_list

	# Finds words which have no vowels, and adds them to the list self.vowelless
	# INPUT self.words_list
	# OUTPUT vowelless list
	def no_vowels(self):
		self.vowelless = []
		a=u'bączek'
		for element in self.words_list:
			appears = False
			for i in element:
				if i in self.vowels:
					appears = True
					break
				else:
					continue
			if appears == False:
				self.vowelless.append(element)

	# Prints to a file - from list to line-by-line txt
	# INPUT: 1st filename, 2nd list with content
	# OUTPUT: file given as first argument
	def print_to_file(self, file, list_to_pass):
		f = io.open(file, 'w', encoding='utf-8')
		for element in list_to_pass:
			f.write(element)
		f.close()

	# creates a dict with words having sequence of consonants at the beginning of given lenght
	def starting_consonants(self):
		longest_start = {0 : [], 1 : [], 2 : [], 3 : [], 4 : [], 5 : [], 6 : [], 7 : [], 8 : [], 9 : [], 10 : []}
		for word in self.words_list:
			check = 0
			for position, letter in enumerate(word):
				# print (letter)
				# for a in self.vowels:
				# 	print (letter, a, letter == a)
				if letter in self.vowels:
					check = position
					break
				elif position + 1 == len(word):
					check = position + 1
				else:
					check = position
			longest_start[int(check)].append(word)
		return longest_start

# 0. Initialize instance of Vowels. As input, give (a) dictionary file, (b) output file for starting (c) vowelless.txt (d) output file for ending
instance = Vowels('slowa.txt', sys.argv[1], 'vowelless.txt')
# 1. Create a list based on dictionary.
instance.dictionary_to_list()
# 2. Create vowelless LIST.
instance.no_vowels()
# 3. Print (2) list to a file.
instance.print_to_file(instance.vowelless_file, instance.vowelless)
# 4. Create a dictionary, sorting words based on number of consonants at their beginning ('scholar' sorted as 3, 'cat' as 1, etc.)
beginning_consonants = instance.starting_consonants()
# To test, print keys of newly created dictionary.
print(beginning_consonants.keys())
# That part is basically hard-coded - as it comes out, longest sequence of consonants at the beginning of polish words is 6
# Hence I will print this sequence to a variable, and then a file.
final_start = beginning_consonants[6]
instance.print_to_file(instance.outputfile_start)