FILE_PATH1='dataSet\heart_disease.txt'
FILE_PATH2='resultHeartKmeans.txt'
def loadData1(filePath):
	dataSet=list()
	fp=open(filePath,'r')
	line=fp.readline()
	while line!='':
		count,length=0,12
		#line=line[0:-1]
		#print(line)
		l=line.split(',')
		while count<=length:
			if l[count]=='?':
				l[count]='0'
			l[count]=float(l[count])
			count+=1
		label=int(l[13])
		dataSet.append([l[0:13],label])
		line=fp.readline()
	return dataSet
def loadData2(filePath):
	dataSet=list()
	fp=open(filePath,'r')
	line=fp.readline()
	while line!='':
		count,length=0,12
		l=line.split(',')
		while count<=length:
			l[count]=float(l[count])
			count+=1
		label=int(l[13])
		dataSet.append([l[0:13],label])
		line=fp.readline()
	return dataSet
def genDict(dataSet):
	resDict=dict()
	for e in dataSet:
		label=e[1]
		if label not in resDict:
			resDict[label]=[e[0]]
		else:
			resDict[label].append(e[0])
	return resDict
def genDictReverse(dataSet):
	print(dataSet)
	resDict=dict()
	for e in dataSet:
		data=tuple(e[0])
		resDict[data]=e[1]
	return resDict
'''dataSetOrigin=loadData1(FILE_PATH1)
dataSetResult=loadData2(FILE_PATH2)
resDictOrigin=genDict(dataSetOrigin)
resDictResult=genDictReverse(dataSetResult)
key=list(resDictOrigin.keys())
accuracyNIC=list()
for e in key:
	accuracyNIC.append(0)
accuracyNIC.append(0)
for e in key:
	count,length=0,len(key)
	tempList=list()
	while count<=length:
		tempList.append(0)
		count+=1
	temp=resDictOrigin[e]
	for point in temp:
		if tuple(point) in resDictResult:
			tempList[resDictResult[tuple(point)]]+=1
	max=0
	for num in tempList:
		if num>max:
			max=num
	accuracyNIC[e]=max/len(temp)
print(accuracyNIC)
finalResult=0
for e in accuracyNIC:
	finalResult+=e
finalResult/=len(accuracyNIC)-1
fp=open('resultScoreKmeans.txt','a')
fp.write('heart,'+str(finalResult)+'\n')'''
Insert into Table1() values(1,1,'f',20);
Insert into Table1() values(2,2,'m',22);
Insert into Table1() values(3,3,'f',23);
Insert into Table1() values(4,4,'f',22);
Insert into Table1() values(5,1,'f',24);
Insert into Table1() values(6,2,'m',19);
Insert into Table1() values(7,4,'f',26);
Insert into Table1() values(8,1,'f',24);
Insert into Table1() values(9,1,'f',20);
Insert into Table1() values(10,2,'m',22);
Insert into Table1() values(11,3,'f',23);
Insert into Table1() values(12,4,'f',22);
Insert into Table1() values(13,1,'f',24);
Insert into Table1() values(14,2,'m',19);
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import mlab
from matplotlib import rcParams
fig1 = plt.figure(2)
rects1 =plt.bar(left = (0.2,1.0),height = (0.7457643696453675,0.3585110824135215),color=('g'),label=(('NIC')),width = 0.2,align="center",yerr=0.000001)
rects2 =plt.bar(left = (0.4,1.2),height = (0.7029621230206096,0.24806071976803684),color=('r'),label=(('KMeans')),width = 0.2,align="center",yerr=0.000001)
plt.legend()
plt.xticks((0.3,1.1),('wine','heart_disease'))
plt.title('accuracy')

def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        plt.text(rect.get_x()+rect.get_width()/2., 1.03*height, '%s' % float(height))
autolabel(rects1)
autolabel(rects2)
plt.show()