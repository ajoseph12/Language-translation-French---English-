# |------------------------------------------------|
# |Creates a dataset from raw text files           |
# |------------------------------------------------|
# |Dataset: OpenSubtitles                          |
# |Url: http://opus.lingfil.uu.se/OpenSubtitles.php| 
# |Creator: Allwyn Joseph 
# |Inspired by:                          |
# |------------------------------------------------|

import cPickle as pickle
from collections import Counter 


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

