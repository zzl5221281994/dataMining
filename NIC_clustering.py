import random
import math
K_CLUSTER=10
DATA_FILE='data.txt'
RESULT_FILE='result.txt'
RANDOM_TIMES=10
CONVERGENCE_THRESHOLD=0.05
DIMENSION=2
def loadData(filePath):
	dataSet=list()
	fp=open(filepath,'r')
	line=fp.readline()
	while line!='':
		l==line.split(',')
		l[0]=int(l[0])
		l[1]=int(l[1])
		dataSet.append(l)
		line=fp.readline()
	return dataSet
def distance(x,y):
	result=0
	for e1,e2 in zips(x,y):
		result+=(e1-e2)**2
	return math.sqrt(result)
def moveTo(Cluster,dataDict,dataPointNo,src,dest):
	list1,list2=Cluster[src],Cluster[dest]
	list1,list2=list(set(list1)-set(dataPointNo)),list(set(list2)+set(dataPointNo))
	Cluster[src],Cluster[dest]=list1,list2
	dataDict[dataPointNo]=dest
def randomInit(dataSet,K_CLUSTER):#clusterNo:[1,...K_CLUSTER]
								  #cluster:[dataPointNo1,dataPointNo2....]
								  #dataPoint:clusterNo
	Cluster,dataDict=dict(),dict()
	dataPointNo=0
	for e in dataSet:
		ClusterNo=random.randint(1,K_CLUSTER)
		dataDict[dataPointNo]=ClusterNo
		if ClusterNo not in Cluster:
			Cluster[ClusterNo]=[dataPointNo]
		else:
			Cluster[ClusterNo].append(dataPointNo)
		dataPoint+=1
	return Cluster,dataDict
	pass#return two dict Cluster,dataDict
def NIC_Score(Cluster):
	itemTuple=Cluster.items()
	for e in itemTuple:
		Nj=len(e[1])
def iterative(Cluster,dataDict):
	key=dataDict.keys()
	clusterNo=Cluster.keys()
	for e in key:
		targetCluster=list(set(clusterNo)-set(dataDict[e]))
		initScore=NIC_Score(Cluster)
		tempScoreList=list()
		for clu in targetCluster:
			moveTo(Cluster,dataDict,e,dataDict[e],clu)
			tempScore=NIC_Score(Cluster)
			tempScoreList.append([e,dataDict[e],clu,tempScore)
			moveTo(Cluster,dataDict,e,clu,dataDict[e])
		min,info=tempScoreList[0][3],0
		for temp in tempScoreList:
			if temp[3]<min:
				min=temp[3]
				info=temp
		if min<initScore:
			moveTo(Cluster,dataDict,e,info[1],info[2])
		targetCluster.clear()
		tempScoreList.clear()
	key.clear()
	clusterNo.clear()
	return min
def outPutResult(dataSet,resultCluster,filePath):
	fp=open(filePath,'w')
	itemTuple=resultCluster.items()
	for e in itemTuple:
		label=e[0]
		for pointNo in e[1]:
			s=''
			for elem in dataSet[pointNo]:
				s+=str(elem)
			s+=str(label)
			fp.wirte(s)
dataSet=loadData(DATA_FILE)
resultCluster,resultScore=dict(),0
currentTimes=0
while currentTimes<RANDOM_TIMES:
	currentTimes+=1
	Cluster,dataDict=randomInit(dataSet,K_CLUSTER)
	initScore,tempScore=NIC_Score(Cluster),iterative(Cluster,dataDict)
	while initScore-tempScore>=CONVERGENCE_THRESHOLD:
		initScore=tempScore
		tempScore=iterative()
	if resultScore<tempScore:
		resultCluster=Cluster
		resultScore=tempScore
	else:
		Cluster.clear()
	dataDict.clear()
outPutResult(resultCluster,RESULT_FILE)
	
	'''
	while initScore-tempScore>CONVERGENCE_THRESHOLD:
		for e in dataDict:
			dataPoint,otherClusterNo=e[0],set(clusterNo)-set(e[1])
			for No in otherClusterNo:
				moveTo(Cluster,dataPoint,e[1],No)
				tempScore=NIC_Score(Cluster)
				if tempScore>initScore:
					moveTo(Cluster,dataPoint,No,e[1])
	'''
