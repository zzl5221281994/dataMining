K_CLUSTER=10
DATA_FILE='data.txt'
RESULT_FILE='result.txt'
RANDOM_TIMES=10
CONVERGENCE_THRESHOLD=1
def randomInit(dataSet,K_CLUSTER):#clusterNo:[1,...K_CLUSTER]
								  #cluster:[dataPointNo1,dataPointNo2....]
								  #dataPoint:clusterNo
	pass#return two dict Cluster,dataDict
def NIC_Score(Cluster):
	pass
def iterative():
	pass
def outPutResult():
	pass
dataSet=loadData(DATA_FILE)
resultCluster,resultScore=dict(),0INF
currentTimes=0
while currentTimes<RANDOM_TIMES:
	currentTimes+=1
	Cluster,dataDict=randomInit(dataSet,K_CLUSTER)
	initScore,tempScore=NIC_Score(Cluster),iterative()
	while initScore-tempScore>=CONVERGENCE_THRESHOLD:
		initScore=tempScore
		tempScore=iterative()
	if resultScore<tempScore:
		resultCluster=Cluster
		resultScore=tempScore
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
