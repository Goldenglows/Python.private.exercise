#5

from operator import itemgetter

Scores = [('Adam',89),('Bob',75),('Alice',96),('Lisa',78)]

print(sorted(Scores,key = itemgetter(0)))
print(sorted(Scores,key=lambda item: item[0]))