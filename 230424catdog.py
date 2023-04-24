
#生成猫猫 需要输入猫猫的年龄
def creat_cat(age):
    jia_cat=100
    return jia_cat

#生成狗狗 需要输入狗狗的种类
def creat_dog(kind):
    jia_dog=100
    return jia_dog

def cat_action(age,dog_jia): 
    if age>2:
        dog_jia-=40
    else:
        dog_jia-=10
    return dog_jia

def dog_action(kind,cat_jia):
    if kind == "Pekingba":
        cat_jia-=20
    elif kind == "Tibetan Mastiff":
        cat_jia-=80
    return cat_jia

age=int(input("Please tell me how old is your cat:"))
cj=creat_cat(age)
kind = input("Please tell me which kind is your dog Pekingba or Tibetan Mastiff:")
dj=creat_dog(kind)
print(cat_action(age,dj))
print(dog_action(kind,cj))