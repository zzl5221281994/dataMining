from matplotlib import pyplot as plt
from matplotlib import font_manager
""" 比较好看的绘制方法 """

plt.figure(figsize=(8, 5), dpi=80)
axes = plt.subplot(111)
# 将三类数据分别取出来
# x轴代表飞行的里程数
# y轴代表玩视频游戏的百分比
type1_x = [1,2,3,4]
type1_y = [2,3,4,9]
type2_x = [24,22,11,11,334]
type2_y = [123,123,554,123,32]
type3_x = [1,23,54,76,3]
type3_y = [1,23,43,23,23]

type1 = axes.scatter(type1_x, type1_y, s=20, c='red')
type2 = axes.scatter(type2_x, type2_y, s=40, c='green')
type3 = axes.scatter(type3_x, type3_y, s=50, c='blue')
# plt.scatter(matrix[:, 0], matrix[:, 1], s=20 * numpy.array(labels),
#             c=50 * numpy.array(labels), marker='o',
#             label='test')
plt.xlabel(u'每年获取的飞行里程数')
plt.ylabel(u'玩视频游戏所消耗的事件百分比')
axes.legend((type1, type2, type3), (u'不喜欢', u'魅力一般', u'极具魅力'), loc=2)

plt.show()