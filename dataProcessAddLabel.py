import numpy as np
import pandas as pd
import csv
import re

filename = r'D:\NLP\NewCars\1_zhangchen\1_zhangchen\103.txt'
reader = open(filename,encoding='utf-8')
dic_text = '威马EX5;威马EX6;威马EVOLVE;CommendatoreGT;威马AG2020;威马EX5Pro;威马EX5520;威马EX5Mate400;EX5;EX6;EX5Pro;EX5520;EX5Mate400'
dic = dic_text.split(';')
list_data = reader.readlines()
s = ""
ans = ""
res = []
count = 1;

for i in list_data:
    s += i
    s += '\n'
print(s)
for i in dic:
    for j,c in enumerate(s):
        if j+len(i) < len(s) and s[j:j+len(i)] == i:
            ans = ans+'T'+str(count)+'\t'+'car'+'\t'+str(j)+'\t'+str(j+len(i))+'\t'+s[j:j+len(i)]
            res.append(ans)
            ans = ""
            count = count+1
print(res)
f = open(r'D:\NLP\NewCars\1_zhangchen\1_zhangchen\test.ann','w',encoding='utf-8')
for i in res:
    temp_line = i+"\n"
    f.write(temp_line)
f.close()
