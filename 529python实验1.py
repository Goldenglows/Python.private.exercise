import pandas as pd

key=["a","b","c","d","e","f"]

myvar = pd.Series(key, index = [30,25,27,41,25,34])

myvar1 = pd.Series("g",27)

myvar.append(myvar1)

myvar["d"]=40

myvar[myvar>27]

myvar.drop(myvar[1:3])