"""
1. 对比前一个数和后一个数进行对比，如果前一个数大于后面那个数，就交换，否则，不变
2.
"""
# list1 = [45, 32, 8, 33, 12, 22]
list1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

# list1[0] = 45

# 1. 对比

# if list1[0]>list1[1]:
#     ## temp作为一个容器暂时存放数据，交换两个值
#     temp = list1[0]
#     list1[0] = list1[1]
#     list1[1] = temp
# def bubble(list1):
class BubbleSort:
    def bubble_sort(self,list1):
        for i in range(1, len(list1)):
            print("这是第{}次排序".format(i))
            for j in range(len(list1)-i):
                print("这是第{}次对比".format(j))
                if list1[j]>list1[j+1]:
                    list1[j],list1[j+1] = list1[j+1],list1[j]
        return list1
bubble = BubbleSort()
print(bubble.bubble_sort(list1))
