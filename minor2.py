import loadData
from numpy import *
from sklearn import *

def create_pref_model(trainData):
	pref_matrix=zeros((943,1682))
	m = shape(trainData)[0]
	n = shape(trainData)[1]
	# for i in range(0,m):
	# 	for j in range(0,n):
	# 		if trainData[i][j] not in (1,2,3,4,5):
	# 			trainData[i][j]=0
	# print trainData
	total=0
	greater1=0
	equal1=0
	pref1=0
	greater2=0
	equal2=0
	pref2=0
	greater3=0
	equal3=0
	pref3=0
	greater4=0
	equal4=0
	pref4=0
	greater5=0
	equal5=0
	pref5=0

	for i in range(0,m):
		total=0
		lesser1=0
		equal1=0
		pref1=0
		lesser2=0
		equal2=0
		pref2=0
		lesser3=0
		equal3=0
		pref3=0
		lesser4=0
		equal4=0
		pref4=0
		lesser5=0
		equal5=0
		pref5=0
		for j in range(0,n):
			if trainData[i][j]:
				total+=1
			if trainData[i][j]==1:
				equal1+=1
				lesser2+=1
				lesser3+=1
				lesser4+=1
				lesser5+=1
			if trainData[i][j]==2:
				equal2+=1
				lesser3+=1
				lesser4+=1
				lesser5+=1
			if trainData[i][j]==3:
				equal3+=1
				lesser4+=1
				lesser5+=1
			if trainData[i][j]==4:
				equal4+=1
				lesser5+=1
			if trainData[i][j]==5:
				equal5+=1

		pref1=(lesser1 + 0.5*equal1)/total
		pref2=(lesser2 + 0.5*equal2)/total
		pref3=(lesser3 + 0.5*equal3)/total
		pref4=(lesser4 + 0.5*equal4)/total
		pref5=(lesser5 + 0.5*equal5)/total

		for j in range(0,n):
			if trainData[i][j]==1:
				pref_matrix[i][j]=pref1
			elif trainData[i][j]==2:
				pref_matrix[i][j]=pref2
			elif trainData[i][j]==3:
				pref_matrix[i][j]=pref3
			elif trainData[i][j]==4:
				pref_matrix[i][j]=pref4
			elif trainData[i][j]==5:
				pref_matrix[i][j]=pref5

	# print pref_matrix
	return pref_matrix

# def userBasedKNN(inX,dataSet,k):
# 	dataSetSize=shape(dataSet)[0] # dataSet.shape[0]
# 	tempMat=tile(inX,(dataSetSize,1))
# 	diffMat=dataSet-tempMat
# 	sqDiffMat=diffMat**2
# 	sqDistances=sqDiffMat.sum(axis=1)
# 	distances=sqDistances**(1.0/2)
#
# 	sortedDistIndicies=argsort(distances) # distance.argsort()

	# classCount={}
	# for i in range(0,k):
	# 	if labels[sortedDistIndicies[i]] not in classCount:
	# 		classCount[labels[sortedDistIndicies[i]]]=1
	# 	else:
	# 		classCount[labels[sortedDistIndicies[i]]]+=1
	# sortedClassCount=sorted(classCount.iteritems(),key=operator.itemgetter(1),reverse=True)
	# # print sortedClassCount[0][0]
	# return sortedClassCount[0][0]

def test():
	trainData = loadData.loadTrainingData("u.data")
	# create_pref_model(trainData)
	pref_matrix = create_pref_model(trainData)
	# print pref_matrix
	return pref_matrix


# test()
