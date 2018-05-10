# |------------------------------------------------|
# |Creates a dataset from raw text files           |
# |------------------------------------------------|
# |Dataset: OpenSubtitles                          |
# |Url: http://opus.lingfil.uu.se/OpenSubtitles.php| 
# |Creator: Allwyn Joseph 						   |
# |Code Inspired by: Nemanja Tomic                 |
# |------------------------------------------------|

import cPickle as pickle
from collections import Counter 
import re

_WordInput = re.compile(',." ;:)(][?!')


def read_sentence(file_path):
	
	"""
	The function strips the txt file and stores it as a list

	Argument:
	file_path -- path of the subtitled file

	Returns:
	sentences -- list of phrases wihin the subtitled file
	"""

	phrases = []
	with open(file_path, 'r') as reader:

		for phrase in reader:
			phrases.append(phrase)

def create_datasets(en_phrase, fr_phrase):
	
	"""
	This function would extract the words from each of the phrases
	and store in a sorted manner within a dictionary. The function 
	further goes on to create word2indx and indx2word dictionaries
	along with input and target lists.

	Argument:
	en_phrases -- list of english phrases 
	fr_phrases -- list of french phrases

	Returns:
	word2indx --
	indx2word -- 
	X -- 
	Y -- 

	"""
	sp = ',." ;:)(][?!'
	
	# creating a dictionary of unique words with their frequency as the key
	en_vocab_dict = Counter(word.strip(sp) for phrase in en_phrases for word in phrase.split())
	fr_vocab_dict = Counter(word.strip(sp) for phrase in fr_phrases for word in phrase.split())

	# creating a list of words in descending order of their frequency 
	en_vocab = list(map(lambda x: x[0], sorted(en_vocab_dict.items(), key = lambda x: -x[1])))
	fr_vocab = list(map(lambda x: x[1], sorted(fr_vocab_dict.items(), key = lambda x: -x[1])))
	


	unique()


































