import numpy as np
import pandas as pd

#读取文件中的数据
data = pd.read_csv(“train.csv”)

#### 1、船上男女人数及比例？
data1=data["Sex"].value_counts()
d1=data1["male"].value_counts()
d2=data2["female"].value_counts()
rate1=d1/d2

#### 2、幸存的男女数量及男女比例？
Survived_m = data.Survied[data.Sex == 'male'].value_counts()
Survived_f = data.Survied[data.Survived == 'female'].value_counts()
rate_fm=Survived_m/Survived_f

#### 3、男/女性的生还数量及生还率？ 
Survived_m = data.Survied[data.Sex == 'male'].value_counts()
Survived_f = data.Survied[data.Survived == 'female'].value_counts() 
Survived_1 = data.Pclass[data.Survived == 1].value_counts() 
rate_1=Survived_1/(Survived_f+Survived_m)

# 4、按照年龄，将乘客划分为儿童（<=12）、少年(>12 <18)、
# 成年人(>=18 <65)和老年人(>=65)，分析四个群体生还情况
child_s=data[data["Age"]<=12]
young_s=data[data["Age"]>12 && data["Age"]<18]
adult_s=data[data["Age"]>=18 && data["Age"]<65]
old_s=data[data["Age">=65]]

#### 5、有/无兄弟姐妹的乘客的生还人数和生还率
g1 = data.groupby(['SibSp','Survived']) # 按堂兄弟/妹分组
df1 = pd.DataFrame(g1.count()['PassengerId'])
print(data_train['SibSp'].value_counts())
rate_dfs=df1/891

#### 6、有/无父母子女的乘客的生还人数和生还率
g2 = data.groupby(['Parch','Survived'])# 按孩子/父母分组
df2 = pd.DataFrame(g2.count()['PassengerId'])
print(data_train['Parch'].value_counts())
rate_df2s=df2/891

#### 7、统计各港口上船人数、生还人数及生还率
Embarked_0 = data.Embarked[data.Survived == 0].value_counts()
Embarked_1 = data.Embarked[data.Survived == 1].value_counts()
rate_embarkeds = Embarked_1 / (Embarked_1+Embarked_0)


#### 8、分析票价对生存的影响（选做）
data.loc[data['Survived'] == 0, 'Fare'].plot(kind='kde', color='red', label='未获救')
data.loc[data['Survived'] == 0, 'Fare'].plot(kind='hist', color='steelblue', edgecolor='white', density=True, label='未获救')
data.loc[data['Survived'] == 1, 'Fare'].plot(kind='kde', color='green', label='获救')
data.loc[data['Survived'] == 1, 'Fare'].plot(kind='hist', color='pink', edgecolor='white', density=True, label='获救')
plt.legend()
plt.title(u'获救/未获救乘客的票价分布密度图')
plt.show()


