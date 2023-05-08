
class cat:

    def __init__(self,name,age,lifevaue):
        self.name = name
        self.age = age
        self.lifevaue=lifevaue

    def catattack(name,age,dog_jia): 
        if age>2:
            dog_jia-=40
        else:
            dog_jia-=10
            return dog_jia

class dog:
    def __init__(self,name,d_type,lifevaue):
        self.name = name
        self.d_type = d_type
        self.lifevaue=lifevaue
   
    def dogattack(name,kind,cat_jia):
        if kind == "Pekingba":
            cat_jia-=20
        elif kind == "Tibetan Mastiff":
            cat_jia-=80
        return cat_jia

c=cat("Tom","2","100")
d1=dog("JINBA","Pekingba","100")
d2=dog("Wolf","Tibetan Mastiff","100")

dogleave=c.catattack(2,100)

print(dogleave)

catleave1=int(d1.dogattack("Pekingba",100))
catleave2=d2.dogattack("Tibetan Mastiff",catleave1)

print(catleave2)