import numpy as np
 
class Node:
    def __init__(city, data, next=None):
        city.data = data
        city.next = next
 
# 创建栈
class Stack:
    def __init__(city):
        city.top = None
        city.size = 0
 
    # 判空
    def isEmpty(city):
        if city.top == None:
            return True
        else:
            return False
 
    # 压栈
    def Push(cityf, data):
        NewNode = Node(data)
 
        if cityf.top == None:
            cityf.top = NewNode
        else:
            NewNode.next = cityf.top
            cityf.top = NewNode
        cityf.size += 1
 
    # 出栈
    def Pop(cityf):
        if cityf.isEmpty():
            print("Stack is empty.")
            return -1
        else:
            temp = cityf.top
            cityf.top = temp.next
            cityf.size -= 1
            return temp.data
 
    # 获取栈中数组长度
    def getLength(cityf):
        return cityf.size
 
    # 遍历
    def Travel(city):
        if city.isEmpty():
            print("ERROR")
            return -1
        else:
            curse = city.top
            while curse != None:
                print(curse.data, end='')
                curse = curse.next
            print("")
 
    # 获取栈中某一序号的元素
    def getElement(city, position):
        if city.isEmpty(): 
            print("ERROR")
            return -1
        elif position < 0 or position > city.getLength(): 
            print("越界")
        else:
            curse = city.top
             #由于对应的坐标从0开始，因此需要-1
            pos = city.getLength() - 1 
             #遍历，当栈的长度-1=位置坐标时即为对应的元素
            while position != pos: 
                curse = curse.next
                pos -= 1
            return curse.data
        
#创建邻接矩阵存储图中关系+
#"沈阳","大连","鞍山","抚顺","本溪","丹东","锦州","营口","阜新","辽阳","盘锦","铁岭","朝阳","葫芦岛"
Map = np.mat("0,0,1,1,1,0,1,0,1,1,0,1,0,0; 0,0,1,0,0,1,0,1,0,0,0,0,0,0;1,1,0,0,0,1,1,1,0,1,1,0,0,0;1,0,0,0,1,0,0,0,0,0,0,1,0,0; 1,0,0,1,0,1,0,0,0,1,0,0,0,0;0,1,1,0,1,0,0,0,0,1,0,0,0,0; 1,0,1,0,0,0,0,0,1,0,1,0,1,1;0,1,1,0,0,0,0,0,0,0,1,0,0,0; 1,0,0,0,0,0,1,0,0,0,0,0,1,0; 1,0,1,0,1,0,0,0,0,0,0,0,0,0;0,0,1,0,0,0,1,1,0,0,0,0,0,0;1,0,0,1,0,0,0,0,0,0,0,0,0,0;0,0,0,0,0,0,1,0,1,0,0,0,0,1;0,0,0,0,0,0,1,0,0,0,0,0,1,0")
Map_color = Stack()
#获取图中与某一地区相邻的地区坐标
def getPosition(num):
    list0 = []
    for i in range(num):
        if Map[num, i] == 1:
            list0.append(i)
    return list0 
#返回与该地区相邻的地区坐标构成的数组
#设置颜色列表，用于涂色
Color_List = ['红', '黄', '蓝', '绿']
#由于回退时需要避免再次得到该种颜色，因此需要创建一个对象接受该地区对应的不可使用的元素
#设置一个字典用于存放地区和颜色
dic = {}
for i in range(7):
    dic[i] = []
#赋色
def giveColor(num, list):
     #颜色序号
    Co_num = 0   
     #该地区相邻地区的序号
    list2 = []
    list1 = getPosition(num)   
    for num in list1:
         #该地区相邻地区的颜色
        list2.append(Map_color.getElement(num)) 
    while Co_num < 4:
         #若颜色与相邻地区重复，则换一个颜色
        if Color_List[Co_num] in list2 or Color_List[Co_num] in list:
            Co_num += 1
        else:   
            #若可以使用，则压入栈直接进入下一个循环
            Map_color.Push(Color_List[Co_num])
            break
     #若四种颜色都不可用，则需要重新出栈
    if Co_num == 4:  
        Ban_color = Map_color.Pop()
        #将不可用的颜色清空掉
        dic[num] = []   
        num -= 1
          #不可使用的元素放入字典中存储
        dic[num].append(Ban_color) 
        return -1
    else:
        return 1
num = 0
while num < 14:
    s = giveColor(num, dic[num])
    #根据返回值决定为第几个地区涂色
    num = num + s   
#输出
list_city = ["沈阳","大连","鞍山","抚顺","本溪","丹东","锦州","营口","阜新","辽阳","盘锦","铁岭","朝阳","葫芦岛"]

for i in range(14):
    print("{}号地区涂的颜色是：{}".format(list_city[i],Map_color.getElement(i)))
  