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
def generateCircle(center,radius,MAX):
	count,pai=0,math.pi
	resList=list()
	while count<MAX:
		rad=random.uniform(0,2*pai)
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
def generateRing(center,OuterRadius,InnerRadius):
	res=generateCircle(center,OuterRadius,500)
	result=res.copy()
	count,length=0,len(res)
	while count<length:
		cen=[center.x,center.y]
		dis=distance(cen,res[count])
		if dis<=InnerRadius:
			result.remove(res[count])
		count+=1
	return result
res=generateCircle(point(0,0),40,MAX_POINT)
res1=generateRing(point(0,0),100,70)
x,y=list(),list()
for e in res:
	x.append(e[0])
	y.append(e[1])
x1,y1=list(),list()
for e in res1:
	x1.append(e[0])
	y1.append(e[1])
type1_x=x
type1_y=y
type2_x=x1
type2_y=y1
type1 = axes.scatter(type1_x, type1_y, c='red')
type2 = axes.scatter(type2_x, type2_y, c='green')
type3 = axes.scatter(type3_x, type3_y, c='blue')
# plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(labels),
#             c=50 * numpy.array(labels), marker='o',
#             label='test')
plt.xlim(xmax=500,xmin=-500)
plt.ylim(ymax=500,ymin=-500)
plt.xlabel(u'每年获取的飞行里程数')
plt.ylabel(u'玩视频游戏所消耗的事件百分比')
axes.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc=2)

plt.show()