import random
cat_hp=100
dog_hp=100

def create_cat():
    cat=random.randint(0,1)
    cat_age=lambda x:"猫的年龄:小于等于2岁" if x==0 else "猫的年龄:大于2岁"
    print(cat_age(cat))
    return cat

def create_dog():
        dog=random.randint(0,1)
        dog_class=lambda y:"狗为京巴"if y==0 else "狗为藏獒"
        print(dog_class(dog))
        return dog

def CatbeatDog(cat):
    global dog_hp
    if cat!=0:
        print("\n年龄>2的猫击中狗，狗的生命值-40")
        dog_hp=dog_hp-40
    else:
        print("\n年龄<=2的猫击中狗，狗的生命值-10")
        dog_hp=dog_hp-10
    if dog_hp>=0:
         print("###狗的剩余生命值：",dog_hp)
    else:
         print("###狗生命值不够了，挂了")
        
def DogbeatCat(dog):
    global cat_hp
    if dog!=0:
        print("\n藏獒狗击中猫，猫的生命值-80")
        cat_hp=cat_hp-80
    else:
        print("\n京巴狗击中猫，猫的生命值-20")
        cat_hp=cat_hp-20
    if cat_hp>=0:
         print("###猫的剩余生命值：",cat_hp)
    else:
         print("###狗生命值不够了，挂了")
        
cat=create_cat()
dog=create_dog()
CatbeatDog(cat)
DogbeatCat(dog)

print("\n再来一次......")
cat=create_cat()
dog=create_dog()
CatbeatDog(cat)
DogbeatCat(dog)
