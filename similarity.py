import wikipedia
from connect import giveContent
import math
import nltk
from nltk.corpus import stopwords
def findSimilarity(fromNode, toNode):
	''' Decide the order of similarity between two 
		terms on the basis of common words
	'''
	fromNodeContent = (giveContent(fromNode).lower()).split()
	toNodeContent   = (giveContent(toNode).lower()).split()
	stop_words = set(stopwords.words('english'))
	fromDict = {}
	for word in fromNodeContent:
		if word not in stop_words:
			if word in fromDict:
				fromDict[word] += 1
			else:
				fromDict[word] = 1
	toDict = {}
	for word in toNodeContent:
		if word not in stop_words:
			if word in toDict:
				toDict[word] += 1
			else:
				toDict[word] = 1

	fromNodeWords   = set(fromDict)
	toNodeWords     = set(toDict)
	commonWords     = fromNodeWords.intersection(toNodeWords)

	dotProduct = 0
	for word in commonWords:
		dotProduct += fromDict[word]*toDict[word]
	magFrom = 0
	for word in fromDict:
		magFrom += fromDict[word]*fromDict[word]
	magTo = 0
	for word in toDict:
		magTo += toDict[word]*toDict[word]
	print(dotProduct/math.sqrt(magTo*magFrom))
# print(commonWords/min(len(fromNodeWords),len(toNodeWords)))
	# similarityScore  = 
	# print(fromNodeWords)
	# print(toNodeWords)

if __name__ == "__main__":
	startNode = input()
	endNode = input()
	findSimilarity(startNode, endNode)
