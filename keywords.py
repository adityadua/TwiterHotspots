import re
import json
from nltk.tokenize import word_tokenize

with open('python.json', 'r') as f:
	for  i in f:		
		#line = i.readline()
		tweet = json.loads(i)
		#print(json.dumps(tweet, indent = 4))
		#print(word_tokenize(tweet['text']))
		print(preprocess(tweet['text']))
