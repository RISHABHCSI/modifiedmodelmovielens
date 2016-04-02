from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir
import minor2
import loadData

def classify0(inX,dataSet,k):
	dataSetSize=shape(dataSet)[0] # dataSet.shape[0]
	tempMat=tile(dataSet[inX[0],:],(dataSetSize,1))
	diffMat=dataSet-tempMat
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1)
	distances=sqDistances**(1.0/2)
	summation=0
	num=0
	sortedDistIndicies=argsort(distances) # distance.argsort()
	for i in range(k):
		if dataSet[sortedDistIndicies[i]][inX[1]]!=0:
			summation+=dataSet[sortedDistIndicies[i]][inX[1]]
			num+=1
	if num!=0:
		avg=summation/num
		return avg
	else:
		return 3
	# classCount={}
	# for i in range(0,k):
	# 	if labels[sortedDistIndicies[i]] not in classCount:
	# 		classCount[labels[sortedDistIndicies[i]]]=1
	# 	else:
	# 		classCount[labels[sortedDistIndicies[i]]]+=1
	# sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	# # print sortedClassCount[0][0]
	# return sortedClassCount[0][0]

def file2matrix(filename):
	fr=open(filename)
	arrayOfLines=fr.readlines()
	numberOfLines=len(arrayOfLines)
	returnMat=zeros((numberOfLines,3))
	classLabelVector=[]
	i=0
	for line in arrayOfLines:
		listFromLine=line.split('\t')
		returnMat[i,:]=listFromLine[0:3]
		classLabelVector.append(int(listFromLine[-1]))
		i+=1
	return returnMat,classLabelVector

def normalize(dataSet):
	minVals=dataSet.min(0)
	maxVals=dataSet.max(0)
	ranges=maxVals-minVals
	m=dataSet.shape[0]
	dataSet=(dataSet-tile(minVals,(m,1)))/tile(ranges,(m,1))
	return dataSet,ranges,minVals
	# return dataSet

def classifierTest(dataSet,labels):
	# ratio=0.10
	m=dataSet.shape[0]
	# numOfTests=int(m*ratio)
	# dataSet,ranges,minVals=normalize(dataSet)
	trainData=loadData.loadTrainingData("u.data")
	numOfErrors=0
	for i in range(0,dataSet.shape[0]):
		classifierResult=int(classify0(dataSet[i,:],trainData,25))
		# print classifierResult,labels[i]
		# print
		# print "the classifier came back with: %d, the real answer is: %d"% (classifierResult, labels[i])
		if classifierResult!=labels[i]:
			numOfErrors+=1
	errorRate=numOfErrors*1.0/dataSet.shape[0]
	print errorRate


def mainFunction():
	testData,testLabel=loadData.loadTestData("u1.test")
	classifierTest(testData,testLabel)

mainFunction()
