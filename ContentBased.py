from numpy import *
import loadData
genre=["unknown","Action","Adventure","Animation","Children's","Comedy","Crime","Documentary",
"Drama","Fantasy","Film-Noir","Horror","Musical","Mystery","Romance","Sci-Fi","Thriller","War","Western"]
f=open("u.item")
lines=f.readlines()
l=[]
for line in lines:
    l.append([float(v) for v in line.split("|")[5:]])
# print l
# print l[1]
for i in range(len(l)):
    count=0
    for j in range(len(l[i])):
        if l[i][j]==1:
            count+=1
    for j in range(len(l[i])):
        if l[i][j]==1:
            l[i][j]/=count
# print l[1]
trainData=loadData.loadTrainingData("u.data")
alpha=0.01
# thres=0.001
theta=mat(zeros((943,19)))
# while True:
print shape(mat(l))
# return
for i in range(10):
    for k in range(19):
        old=theta[i,k]
        thres=0.1
        sumi=0
        # T=2
        while True:
            for j in range(1682):
                if trainData[i,j]:
                    sumi+=(mat(l[j])*theta[i,:].T- trainData[i,j])*l[j][k]
            theta[i,k]-=alpha*sumi
            if abs(theta[i,k]-old)<thres:
                break
            # T-=1
print theta[0]
testData,testLabel=loadData.loadTestData("u1.test")
index=0
for t in testData:
    user,movie=int(t[0])-1,int(t[1])-1
    label=testLabel[index]
    rating=theta[user,:]*mat(l[movie]).T
    print label,rating
    index+=1
