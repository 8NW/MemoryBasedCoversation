import datetime
import nltk
import nltk.classify.util
from nltk.classify import NaiveBayesClassifier

 


class memory():
	def __init__(self, addressed, content, data):
		self.time = datetime.datetime.now()

		if addressed != '' or "":
			self.addressed = addressed
		elif:
			tempMemoryDict = MemoryDict.dict
			dictForMem = []
			for mems in tempMemoryDict:
				if mems.getTime() == self.time.minute():
					






		# check memories of similar time stamp and assume but allocate to "possibly" field
		
		self.content = content

		self.data = data


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

	







