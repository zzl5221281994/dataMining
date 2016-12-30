from sklearn.cluster import KMeans
import numpy as np
import datetime
begin=datetime.datetime.now()
FILE_PATH='dataSet\wine.txt'
FILE_PATH_RESULT='resultHeartKmeans.txt'
def loadData1(filePath):
	dataSet=list()
	fp=open(filePath,'r')
	line=fp.readline()
	while line!='':
		count,length=0,12
		line=line[0:-1]
		l=line.split(',')
		while count<=length:
			if l[count]=='?':
				l[count]='0'
			l[count]=float(l[count])
			count+=1
		dataSet.append(l[0:13])
		line=fp.readline()
	return dataSet
dataSet=loadData1(FILE_PATH)
X = np.array(dataSet)
kmeans = KMeans(n_clusters=5, random_state=0).fit(X)
labels=kmeans.labels_

fp=open(FILE_PATH_RESULT,'w')
count,length=0,len(dataSet)
while count<length:
	dataSet[count].append(labels[count])
	count+=1
for e in dataSet:
	fp.write(str(e)[1:-1]+'\n')
	
end=datetime.datetime.now()
print(begin)
print(end-begin)


