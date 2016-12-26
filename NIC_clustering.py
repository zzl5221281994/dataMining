import random
import math
K_CLUSTER=2
DATA_FILE='dataSet18.txt'
RESULT_FILE='result18.txt'
RANDOM_TIMES=5
CONVERGENCE_THRESHOLD=0.01
DIMENSION=2
disDict=dict()
def loadData(filePath):
	dataSet=list()
	fp=open(filePath,'r')
	line=fp.readline()
	while line!='':
		l=line.split(' ')
		l[0]=float(l[0])
		l[1]=float(l[1])
		dataSet.append(l)
		line=fp.readline()
	return dataSet
def whiting(dataSet):
	'''暂时没实现'''
	return dataSet
def distance(x,y):
	result=0
	for e1,e2 in zip(x,y):
		result+=(e1-e2)**2
	return math.sqrt(result)
def moveTo(Cluster,dataDict,dataPointNo,src,dest):
	#print('***',dataPointNo)
	#print('&&&&&&&1',Cluster[src],Cluster[dest])
	Cluster[src].remove(dataPointNo)
	Cluster[dest].append(dataPointNo)
	#print('&&&&&&&2',Cluster[src],Cluster[dest])
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
		dataPointNo+=1
	return Cluster,dataDict
	pass#return two dict Cluster,dataDict
def SumlogDis(dataSet,dataPointList):
	iter,tempDict=dataPointList.copy(),dict()
	res=0
	for e1 in iter:
		for e2 in dataPointList:
			if (e1,e2) not in tempDict and (e2,e1) not in tempDict and e1!=e2:
				#print(distance(dataSet[e1],dataSet[e2]))
					res+=math.log(disDict[(e1,e2)])
					tempDict[(e1,e2)]=1
	return res
def NIC_Score(dataSet,Cluster):
	itemTuple=Cluster.items()
	#print(itemTuple)
	dataLen=len(dataSet)
	res=0
	for e in itemTuple:
		dis=SumlogDis(dataSet,e[1])
		Nj=len(e[1])
		res+=(DIMENSION/(Nj-1))*dis
	return res
def iterative(Cluster,dataDict,dataSet):
	print('!@#$%^&*')
	key=dataDict.keys()
	key=list(key)
	clusterNo=Cluster.keys()
	clusterNo=list(clusterNo)
	for e in key:
		print(e)
		#print("##@",list([dataDict[e])))
		targetCluster=list(set(clusterNo)-set([dataDict[e]]))
		initScore=NIC_Score(dataSet,Cluster)
		tempScoreList=list()
		for clu in targetCluster:
			src=dataDict[e]
			#print(src,clu,'%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
			moveTo(Cluster,dataDict,e,src,clu)
			tempScore=NIC_Score(dataSet,Cluster)
			tempScoreList.append([e,src,clu,tempScore])
			moveTo(Cluster,dataDict,e,clu,src)
		#print(tempScoreList)
		min,info=tempScoreList[0][3],tempScoreList[0]
		for temp in tempScoreList:
			if temp[3]<min:
				min=temp[3]
				info=temp
		#print('##########@@#@#@',Cluster)
		if min<initScore:
			moveTo(Cluster,dataDict,e,info[1],info[2])
		#targetCluster.clear()
		#tempScoreList.clear()
	#key.clear()
	#clusterNo.clear()
	return min
def outPutResult(dataSet,resultCluster,filePath):
	print(resultCluster)
	fp=open(filePath,'w')
	itemTuple=resultCluster.items()
	for e in itemTuple:
		label=e[0]
		for pointNo in e[1]:
			s=''
			for elem in dataSet[pointNo]:
				s+=str(elem)+' '
			s+=str(label)+'\n'
			fp.write(s)
def getDistance(dataSet):
	iter,resDict=dataSet.copy(),dict()
	e1,e2,length=0,0,len(dataSet)
	while e1<length:
		e2=e1
		while e2<length:
			resDict[(e1,e2)]=distance(dataSet[e1],dataSet[e2])
			resDict[(e2,e1)]=distance(dataSet[e1],dataSet[e2])
			e2+=1
		e1+=1
	return resDict
dataSet=loadData(DATA_FILE)
dataSet=whiting(dataSet)
disDict=getDistance(dataSet)
resultCluster,resultScore=dict(),-10000
currentTimes=0
while currentTimes<RANDOM_TIMES:
	currentTimes+=1
	print(currentTimes)
	Cluster,dataDict=randomInit(dataSet,K_CLUSTER)
	#print(Cluster,'##################################',dataDict)
	initScore=NIC_Score(dataSet,Cluster)
	tempScore=iterative(Cluster,dataDict,dataSet)
	while initScore-tempScore>=CONVERGENCE_THRESHOLD:
		print(initScore-tempScore,CONVERGENCE_THRESHOLD)
		initScore=tempScore
		tempScore=iterative(Cluster,dataDict,dataSet)
	#print(Cluster)
	if resultScore<tempScore:
		resultCluster=Cluster
		resultScore=tempScore
outPutResult(dataSet,resultCluster,RESULT_FILE)