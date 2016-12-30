from matplotlib import pyplot as plt
from matplotlib import font_manager

import random
import math
MAX_POINT=200

""" 比较好看的绘制方法 """

plt.figure(figsize=(8, 5), dpi=80)
axes = plt.subplot(111)

type1_x = [1,2,3,4]
type1_y = [2,3,4,9]
type2_x = [24,22,11,11,334]
type2_y = [123,123,554,123,32]
type3_x = [1,23,54,76,3]
type3_y = [1,23,43,23,23]

class point:
	def __init__(self,x,y):
		self.x=x
		self.y=y
def distance(x,y):
	result=0
	for e1,e2 in zip(x,y):
		result+=(e1-e2)**2
	return math.sqrt(result)
def isInCircle(center,radius,point):
	res=math.sqrt((point.x-center.x)**2+(point.y-center.y)**2)
	return res<=radius
def generateCircle(center,radius,MAX,rad1,rad2):
	count,pai=0,math.pi
	resList=list()
	while count<MAX:
		rad=random.uniform(rad1,rad2)
		num=random.uniform(0,100)
		l=0
		if num<=15:
			l=random.uniform(0,radius/4)
		else:
			l=random.uniform(radius/4,radius)
		#l=random.uniform(0,radius)
		x=center.x+l*math.cos(pai/2-rad)
		y=center.y+l*math.sin(pai/2-rad)
		resList.append([x,y])
		count+=1
	return resList
def generateRing(center,OuterRadius,InnerRadius,num,rad1,rad2):
	res=generateCircle(center,OuterRadius,100*num,rad1,rad2)
	result=res.copy()
	count,length=0,len(res)
	while count<length:
		cen=[center.x,center.y]
		dis=distance(cen,res[count])
		if dis<=InnerRadius:
			result.remove(res[count])
		count+=1
	return result
def generateSquare(leftTop,height,width,num):
	count=0
	resList=list()
	while count<num:
		count+=1
		x=random.uniform(leftTop.x,leftTop.x+width)
		y=random.uniform(leftTop.y-height,leftTop.y)
		resList.append([x,y])
	return resList
def outPutResult(res,filepath):
	fp=open(filepath,'a')
	for e in res:
		s=str(e[0])+' '+str(e[1])+'\n'
		fp.write(s)
res0=generateCircle(point(0,0),8,MAX_POINT,0,2*math.pi)
#res4=generateCircle(point(20,20),15,MAX_POINT,0,2*math.pi)
#res3=generateCircle(point(-10,-10),15,MAX_POINT,0,2*math.pi)

res1=generateRing(point(0,0),50,48,200,0,2*math.pi)
res2=generateRing(point(0,0),30,28,200,0,2*math.pi)
#res3=generateSquare(point(0,10),3,10,70)
#res5=generateSquare(point(4,5),5,2,90)
#outPutResult(res,'dataSet2.txt')
#outPutResult(res1,'dataSet7.txt')
#outPutResult(res4,'dataSet15.txt')
#outPutResult(res0,'dataSet15.txt')
outPutResult(res0,'dataSet21.txt')
outPutResult(res1,'dataSet21.txt')
outPutResult(res2,'dataSet21.txt')
#outPutResult(res3,'dataSet15.txt')
#outPutResult(res1,'dataSet10.txt')
#outPutResult(res5,'dataSet10.txt')
x,y=list(),list()
for e in res0:
	x.append(e[0])
	y.append(e[1])
x1,y1=list(),list()
for e in res1:
	x1.append(e[0])
	y1.append(e[1])
x2,y2=list(),list()
for e in res2:
	x2.append(e[0])
	y2.append(e[1])

x5,y5=list(),list()
for e in res2:
	x5.append(e[0])
	y5.append(e[1])
x6,y6=list(),list()
for e in res2:
	x6.append(e[0])
	y6.append(e[1])
type1_x=x
type1_y=y
type2_x=x1
type2_y=y1
type3_x=x2
type3_y=y2

type1 = axes.scatter(type1_x, type1_y, c='red')
type2 = axes.scatter(type2_x, type2_y, c='green')
type3 = axes.scatter(type3_x, type3_y, c='blue')
type4 = axes.scatter(x5, y5, c='black')
type5 = axes.scatter(x6, y6, c='purple')
# plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(labels),
#             c=50 * numpy.array(labels), marker='o',
#             label='test')
plt.xlim(xmax=100,xmin=-100)
plt.ylim(ymax=100,ymin=-100)
plt.xlabel(u'每年获取的飞行里程数')
plt.ylabel(u'玩视频游戏所消耗的事件百分比')
axes.legend((type1, type2, type3,type4,type5), (u'不喜欢', u'魅力一般', u'极具魅力',u'xx',u'aa'), loc=2)

plt.show()