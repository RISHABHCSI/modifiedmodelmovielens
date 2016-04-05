import loadData
from numpy import *
from sklearn import *

trainData=loadData.loadTrainingData("u.data")
def pca(dataSet,k):# taking k dimensions
	meanValues=mean(dataSet,axis=0)#1Xn
	dataSet=mat(dataSet)
	dataSet=dataSet-meanValues
	m=shape(dataSet)[0]
	n=shape(dataSet)[1]
	covMat=(1.0/943)*(dataSet.T)*dataSet # nXn
	u,s,v=linalg.svd(mat(covMat),full_matrices=True)
	uReduced=u[:,:]#nXm
	z=dataSet*uReduced
	return z

from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
from os import listdir
import minor2
import loadData
import math
pred_rating=[]

def classify0(inX,dataSet,k):
	dataSetSize=shape(dataSet)[0] # dataSet.shape[0]
	tempMat=tile(dataSet[inX[0],:],(dataSetSize,1))
	dataSet=array(dataSet)
	tempMat=array(tempMat)
	diffMat=dataSet-tempMat
	sqDiffMat=diffMat**2
	sqDistances=sqDiffMat.sum(axis=1)
	distances=sqDistances**(1.0/2)
	summation=0
	num=0
	sortedDistIndicies=argsort(distances) # distance.argsort()
	for i in range(k):
		if trainData[sortedDistIndicies[i]][inX[1]]!=0:
			summation+=trainData[sortedDistIndicies[i]][inX[1]]
			num+=1
	if num!=0:
		avg=summation/num
		return avg
	else:
		return 3

# def normalize(dataSet):
# 	minVals=dataSet.min(0)
# 	maxVals=dataSet.max(0)
# 	ranges=maxVals-minVals
# 	m=dataSet.shape[0]
# 	dataSet=(dataSet-tile(minVals,(m,1)))/tile(ranges,(m,1))
# 	return dataSet,ranges,minVals

def classifierTest(dataSet,labels):
	# ratio=0.10
	m=dataSet.shape[0]
	neighbour=25
	# numOfTests=int(m*ratio)
	# dataSet,ranges,minVals=normalize(dataSet)
	# trainData=loadData.loadTrainingData("u.data")
	# trainData=minor2.test()
	# print shape(trainData)
	ds=pca(trainData,100)
	# print shape(ds)
	# return
	# print shape(trainData)
	# return
	numOfErrors=0
	dictionary={}
	prev=-1
	testD=loadData.loadTrainingData("u1.test")
	for i in range(0,dataSet.shape[0]):
		user=dataSet[i,0]
		movie=dataSet[i,1]
		classifierResult=int(classify0(dataSet[i,:],ds,neighbour))
		if i==0:
			prev=user
			dictionary[movie]=classifierResult
		else:
			if user!=prev:
				pred_rating.append(dictionary)
				dictionary={}
				dictionary[movie]=classifierResult
				prev=user
			else:
				dictionary[movie]=classifierResult
	if len(dictionary):
		pred_rating.append(dictionary)
	i=0;ndcg=0
	prec=0;recall=0
	for l in pred_rating:
		# tuPlus=[]
		tuPlus=0;intersection=0
		prec_u=0;recall_u=0;dcg_u=0;idcg_u=0;ndcg_u=0
		temp=sorted(l.items(),key=operator.itemgetter(1),reverse=True)
		top_n=temp[:neighbour]
		for j in range(testD.shape[1]):
			if testD[i,j]==5:
				tuPlus+=1
				num=1
				for q in top_n:
					idcg_u+=(1.0/math.log(num+1,2))
					if q[0]==j+1:
						dcg_u+=(1.0/math.log(num+1,2))
						intersection+=1
					num+=1
				ndcg_u=dcg_u/idcg_u
		print intersection,neighbour,tuPlus
		prec_u=intersection*1.0/neighbour
		if tuPlus:
			recall_u=intersection*1.0/tuPlus
		prec+=prec_u
		recall+=recall_u
		ndcg+=ndcg_u
		i+=1
	prec=prec*1.0/i
	recall=recall*1.0/i
	ndcg=ndcg*1.0/i
	print prec,recall,ndcg

		# print temp
		# return
		# pred_rating[user-1].append({movie:classifierResult})
		# print classifierResult,labels[i]
		# print
		# print "the classifier came back with: %d, the real answer is: %d"% (classifierResult, labels[i])
	# 	if classifierResult!=labels[i]:
	# 		numOfErrors+=1
	# errorRate=numOfErrors*1.0/dataSet.shape[0]
	# print errorRate


def mainFunction():
	testData,testLabel=loadData.loadTestData("u1.test")
	classifierTest(testData,testLabel)

mainFunction()
