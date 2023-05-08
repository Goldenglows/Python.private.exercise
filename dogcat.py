def BornCat(name, age, lifeValue):
    cat = [name, age, lifeValue]
    return cat


def BornDog(name, dogType, lifeValue):
    dog = [name, dogType, lifeValue]
    return dog


def CatAttack(cat, dog):
    if cat[1] <= 2:
        dog[2] -= 10
        print(cat[0] + "击中了" + dog[1] + "," + dog[1] + "的生命力-10.")
    else:
        dog[2] -= 40
        print(cat[0] + "击中了" + dog[1] + "," + dog[1] + "的生命力-40.")
    print(dog[0] + "的剩余生命值: " + str(dog[2]))
    if dog[2] <= 0:
        print(dog[0] + "死了.")


def DogAttack(cat, dog):
    if dog[1] == '京巴':
        cat[2] -= 20
        print(dog[0] + "击中了" + cat[0] + "," + cat[0] + "的生命力-20")
    else:
        cat[2] -= 80
        print(dog[0] + "击中了" + cat[0] + "," + cat[0] + "的生命力-80")
    print(cat[0] + "的剩余生命值: " + str(Tom[2]))
    if cat[2] <= 0:
        print(cat[0] + "死了.")


Tom = BornCat('Tom', 2, 100)
JinBa = BornDog('JinBa', '京巴', 100)
Wolf = BornDog('Wolf', '藏獒', 100)
CatAttack(Tom, JinBa)
CatAttack(Tom, Wolf)
DogAttack(Tom, JinBa)
DogAttack(Tom, Wolf)
