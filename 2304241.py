# 2.

# *args 是 无关键字参数；
# 函数中用列表或者元祖的形式传递参数时要用到的；

# **kwargs 是 有关键字参数；
# 当函数中要用字典形式传递参数时要用到的；

# *args的应用举例如下：
def argsprint(a,*args):
    b = args
    print(a,'\n',b)



# **kwargs的应用举例如下
def kwargsprint(c,**kwargs):
    print(c)
    dict = kwargs
    print("name=",dict['name'])
    print("key=",dict['key'])    


argsprint("123","kadsh","isaud","asdhg")
kwargsprint(0,name="wo",key=20)