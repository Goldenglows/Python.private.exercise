import sys
import os
import csv

filename = 'C:\Users\Suainian\Desktop'
with open(filename) as f:
    data = csv.reader(f)
    head_row = next(data)   
    for row in data:
          print(data.line_num,row)
