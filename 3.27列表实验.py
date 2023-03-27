#1
score=[]
numl=[68,87,92,100,76,88,54,89,76,61]
for i in numl:
    #2
    score.append(i)
#print(score)

#3
print(score[2])

#4
for v in range(0,6):
    print(score[v])

#5
score.insert(2,59)
# print(score)

#6
num = 76
print (score.count(num))

#7
if num in score:
    print ('存在该考试成绩')
else:
    print ('不存在该考试成绩')

#8
print(score.index(100))

#9
score[score.index(59)]+=1
# print(score)

#10
del score[0]
# print(score)

#11
leng=len(score)
# print(leng)

#12
score.sort()
# print(score)
print('最小的元素为')
print(score[0])
print('最大的元素为')
print(score[len(score)-1])

#13
score.reverse()
# print(score)

#14
list_pop=score.pop(len(score)-1)
print ("删除的项为 :", list_pop)
# print(score)

#15
score.append(88)
# print(score)
score.remove(88)
# print(score)

#16
score1=[80,61]
score2=[71,95,82]
score3 = score1 +score2
print(score3)

#17
score2 = score1 * 5
print(score2)



