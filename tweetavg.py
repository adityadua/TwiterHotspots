import re
import json
from nltk.tokenize import word_tokenize
import dateparser

with open('python.json', 'r') as f:
	j=1
	k=0
	tot_time=0
	tweet=0
	tweetx=f.readline()
	tweetx=json.loads(tweetx)
	for i in f:		
		#line = i.readline()
		if j==50:
			tweet = json.loads(i)
			#tot_time=tot_time+t1-t2;
			j=0
			k=k+1
		j=j+1
	
	t1=dateparser.parse((tweet['created_at'])[11:19])
	t2=dateparser.parse((tweetx['created_at'])[11:19])
	print (t1-t2)/k
		#print(json.dumps(tweet, indent = 4))
		#print(word_tokenize(tweet['text']))
		#print(preprocess(tweet['text']))
