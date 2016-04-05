# your code goes here
from numpy import *
import loadData
import math
top_nrecommendtest=[]

def trainClassifier(trainData,k):
	m=trainData.shape[0]
	n=trainData.shape[1]
	norm_trainData=trainData/5
	# watched=[0]*943
	watched=zeros((943,1682))
	trans=norm_trainData.T
	model=mat(trans)*mat(norm_trainData)
	final_model=mat(zeros((1682,1682)))

	for i in range(0,m):
		for j in range(0,n):
			if trainData[i,j]==0:
				watched[i,j]=0
			else:
				watched[i,j]=1

	trans_watch=watched.T
	watch_together=mat(trans_watch)*mat(watched)
	# print final_model.shape[0],final_model.shape[1]
	# print model.shape[0],model.shape[1]
	# print watch_together.shape[0],watch_together.shape[1]

	# print model[0,0]
	for i in range (0,n):
		for j in range (0,n):
			if watch_together[i,j]!=0:
				final_model[i,j]=model[i,j]/watch_together[i,j]*1.0
			# else:
			# 	final_model[i,j]=0.0
	for i in range(0,n):
		for j in range(0,n):
			if i==j:
				final_model[i,j]=0

	# print final_model
	u=zeros((943,1682))
	for i in range (0,m):
		for j in range (0,n):
			if trainData[i,j]==0:
				u[i,j]=1;
			else:
				u[i,j]=0

	trans_u=u.T
	recommend=final_model*trans_u
	recommend=recommend.T
	for i in range (0,943):
		for j in range (0,1682):
			if u[i,j]==0:
				recommend[i,j]=0

	topn=zeros((943,1682))
	sumi=0
	# print recommend[0]
	# print
	# for i in range (0,n):
	# 	if recommend[0,i]!=0:
	# 		print i
	# 		sumi=sumi+1
	# print sumis

	for i in range (0,m):
		topn[i]=argsort(recommend[i])

	testData=loadData.loadTrainingData("u1.test")
	# print argmax(recommend[0])
	# print testData[0,argmax(recommend[0])]



	# for i in range (n-1,0,-1):
	# 	print topn[0,i],testData[0,topn[0,i]]


	# print sumi


	# print k
	# print topn
	topn_recommendation=zeros((943,k))
	for i in range (0,m):
		topn_recommendation[i]=topn[i,n-k:]

	for i in range(0,topn_recommendation.shape[0]):
		temp=[]
		for j in range(0,len(topn_recommendation[i])):
			if(testData[i,topn_recommendation[i,j]]!=0):
				temp.append(topn_recommendation[i,j]);
		top_nrecommendtest.append(temp);


	# testData=loadData.loadTrainingData("u1.test")
	# sum1=0
	# sum2=0
	# for i in range(0,trainData.shape[1]):
	# 	if trainData[0,i]!=0:
	# 		sum1=sum1+1
	# for i in range(0,testData.shape[1]):
	# 	if testData[0,i]!=0:
	# 		sum2=sum2+1

	# print sum1,sum2,sum1+sum2

	# print topn_recommendation
	# for i in range (0,k):
	# 	print testData[0,topn_recommendation[0,i]]
	# print topn_recommendation
	return topn_recommendation

def testClassifier():
	k=25;m=943;n=1682
	trainData=loadData.loadTrainingData("u.data")
	testData=loadData.loadTrainingData("u1.test")
	trainClassifier(trainData, k)

	ndcg=0;dcg=0;idcg=0;prec=0;recall=0

	for i in range(0,testData.shape[0]):
		# print "inside i loop"
		ndcg_u=0;dcg_u=0;idcg_u=0;tuPlus=0;intersection=0;prec_u=0;recall_u=0
		for j in range(0,testData.shape[1]):
			if testData[i,j]==5:
				# print "inside if"

				num=1
				tuPlus=tuPlus+1
				for n in range (0,k):
					idcg_u+=(1.0/math.log(num+1,2))
					# print j in topn[i]

					for a in range(0,k): #if j in topn[i]
						print j,top_nrecommendtest[i][a]
						if j==top_nrecommendtest[i][a]:
							print "inside if"
							intersection+=1
							dcg_u+=(1.0/math.log(num+1,2))
					num+=1
				ndcg_u=dcg_u/idcg_u
		prec_u=1.0*intersection/k
		if tuPlus:
			recall_u=1.0*intersection/tuPlus

		print prec_u,recall_u,ndcg_u
		prec+=prec_u
		recall+=recall_u
		ndcg+=ndcg_u
	ndcg=1.0*ndcg/m
	prec=1.0*prec/m
	recall=1.0*recall/m
	print prec,recall,ndcg

def test():
	trainData=loadData.loadTrainingData("u.data")
	# trainClassifier(trainData, 25)
	testClassifier()


test()

 
