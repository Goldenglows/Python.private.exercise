import numpy as np
 
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
 
# 创建链栈
class Stack:
    def __init__(self):
        self.top = None
        self.size = 0
 
    # 判断栈是否非空
    def isEmpty(self):
        if self.top == None:
            return True
        else:
            return False
 
    # 将数据存入栈
    def Push(self, data):
        NewNode = Node(data)
 
        if self.top == None:
            self.top = NewNode
        else:
            NewNode.next = self.top
            self.top = NewNode
        self.size += 1
 
    # 删除最后进来的数据
    def Pop(self):
        if self.isEmpty():
            print("栈空无法出栈")
            return -1
        else:
            temp = self.top
            self.top = temp.next
            self.size -= 1
            return temp.data
 
    # 获取栈中数组长度
    def getLength(self):
        return self.size
 
    # 遍历栈
    def Travel(self):
        if self.isEmpty():
            print("栈空，无法遍历")
            return -1
        else:
            curse = self.top
            while curse != None:
                print(curse.data, end='')
                curse = curse.next
            print("")
 
    # 获取栈中某一序号的元素
    def getElement(self, position):
        if self.isEmpty():  # 栈空
            print("栈空，无法遍历")
            return -1
        elif position < 0 or position > self.getLength():  # 下标越界
            print("位置越界")
        else:
            curse = self.top
            pos = self.getLength() - 1  #由于对应的坐标从0开始，因此需要-1
            while position != pos:  #遍历，当栈的长度-1=位置坐标时即为对应的元素
                curse = curse.next
                pos -= 1
            return curse.data
#创建邻接矩阵存储图中关系+
#"沈阳","大连","鞍山","抚顺","本溪","丹东","锦州","营口","阜新","辽阳","盘锦","铁岭","朝阳","葫芦岛"
Map = np.mat("0,0,1,1,1,0,1,0,1,1,0,1,0,0;0,0")
MapColor = Stack()
#获取图中与某一地区相邻的地区坐标
def getPosition(CityNum):
    list0 = []
    for i in range(CityNum):
        if Map[CityNum, i] == 1:
            list0.append(i)
    return list0 #返回与该地区相邻的地区坐标构成的数组
#颜色组
ColorList = ['pink', 'yellow', 'red', 'green']
#由于回退时需要避免再次得到该种颜色，因此需要创建一个对象接受该地区对应的不可使用的元素
dic = {}
for i in range(7):  #初始化字典为空
    dic[i] = []
#赋色
def giveColor(CityNum, list):
    ColorNum = 0    #颜色序号
    list1 = getPosition(CityNum)    #该地区相邻地区的序号
    list2 = []
    for num in list1:
        list2.append(MapColor.getElement(num))  #该地区相邻地区的颜色（只考虑下半矩阵）
    while ColorNum < 4:
        if ColorList[ColorNum] in list2 or ColorList[ColorNum] in list: #若颜色与相邻地区重复 或 颜色不可使用，则尝试下一个颜色
            ColorNum += 1
        else:   #若可以使用，则压入栈直接进入下一个循环
            MapColor.Push(ColorList[ColorNum])
            break
    if ColorNum == 4:   #若序号为4，即四种颜色都不可用，则需要回溯，将已有的颜色出栈
        BanColor = MapColor.Pop()
        dic[CityNum] = []   #由于回溯，该地区对应的不可使用的颜色清空
        CityNum -= 1
        dic[CityNum].append(BanColor)   #不可使用的元素放入字典中存储
        return -1
    else:
        return 1
CityNum = 0
while CityNum < 14:
    s = giveColor(CityNum, dic[CityNum])
    CityNum = CityNum + s   #根据返回值决定为第几个地区涂色


#输出
list_city = ["沈阳","大连","鞍山","抚顺","本溪","丹东","锦州","营口","阜新","辽阳","盘锦","铁岭","朝阳","葫芦岛"]

for i in range(14):
    print("{}号地区涂的颜色是：{}".format(list_city[i],MapColor.getElement(i)))
  

