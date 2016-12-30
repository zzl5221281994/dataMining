from matplotlib import pyplot as plt
from matplotlib import font_manager

plt.figure(figsize=(8, 5), dpi=80)
axes = plt.subplot(111)
type1_x = list()
type1_y = list()
type2_x = list()
type2_y = list()
type3_x = list()
type3_y = list()
resList=list()
count=0
while count<5:
	resList.append([[],[]])
	count+=1
fp=open('result20.txt','r')
line=fp.readline()
while line!='':
	l=line.split(' ')
	l[0]=float(l[0])
	l[1]=float(l[1])
	l[2]=int(l[2])
	resList[l[2]-1][0].append(l[0])
	resList[l[2]-1][1].append(l[1])
	line=fp.readline()
color=['red','green','blue','yellow','black']
count=0
typeS=[]
while count<5:
	typeS.append(axes.scatter(resList[count][0], resList[count][1], s=20, c=color[count]))
	count+=1
# plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(labels),
#             c=50 * numpy.array(labels), marker='o',
#             label='test')
plt.xlabel(u'xx')
plt.ylabel(u'xx')
axes.legend(tuple(typeS), (u'', u'', u''), loc=2)

plt.show()