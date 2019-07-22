import datetime
import pickle
import nltk, nltk.classify.util, nltk.metrics
from nltk.classify import NaiveBayesClassifier
from nltk.metrics import BigramAssocMeasures
from nltk.probability import FreqDist, ConditionalFreqDist
import paralleldots

class memory():
	paralleldots.set_api_key('mdpros0UrW4dvSHoeqeLhA5RVNStbUccWB6BpVpT6h0')

	def __init__(self, addressed, content):
		time = datetime.datetime.now()

		if addressed != '' or "":
			self.addressed = addressed
		else:
			names = getNames(content)
			self.addressed = names[0]

		#this will take the actual sentence
		self.content = str(content)

		#this will be the NLTK review?
		data = []
		# data.add(classifier.classify(format_sentence(data)))
		sentiment = paralleldots.sentiment(str(content))
		data.append(sentiment)

		emotion = paralleldots.emotion(str(content))
		data.append(emotion)
		print emotion

		abuse = paralleldots.abuse(str(content))
		data.append(abuse)

		intent = paralleldots.intent(str(content))
		data.append(intent)



	def getMemory(self):
		arrayMemory = []

		arrayMemory.add(self.time)
		arrayMemory.add(self.addressed)
		arrayMemory.add(self.content)
		arrayMemory.add(self.data)

		return arrayMemory

	# sets the addresed in the memory to a new addressed.
	def setAddressed(self, addressed):
		self.addressed = addressed

	def getMemoryStrength(self):
		
		return self.content

	def getTime(self):
		return self.time

	def getNames(text):
	    tokens = nltk.tokenize.word_tokenize(text)
	    pos = nltk.pos_tag(tokens)
	    sentt = nltk.ne_chunk(pos, binary = False)
	    person_list = []
	    person = []
	    name = ""
	    for subtree in sentt.subtrees(filter=lambda t: t.node == 'PERSON'):
	        for leaf in subtree.leaves():
	            person.append(leaf[0])
	        if len(person) > 1: #avoid grabbing lone surnames
	            for part in person:
	                name += part + ' '
	            if name[:-1] not in person_list:
	                person_list.append(name[:-1])
	            name = ''
	        person = []

	    return person_list


# class conversationWork():
# 	def endPage(self):

# 		pkl_file = open('data_dict.pkl', 'wb')
# 		pickle.dump(self.mlData, pkl_file)

# 		pkl_file = open('content_dict.pkl', 'wb')
# 		pickle.dump(self.labelDict, pkl_file)

# 		pkl_file = open('data_dict.pkl', 'wb')
# 		pickle.dump(self.mlData, pkl_file)

# 		pkl_file = open('content_dict.pkl', 'wb')
# 		pickle.dump(self.labelDict, pkl_file)


if __name__ == '__main__':
	memoryTest = memory('Aiden', "Go fuck yourself!")
	





