# encoding: utf-8
import numpy as np
import pandas as pd
import csv
import re

fileNameCarDic = r'CarDic.xlsx'
CarDic = pd.read_excel(fileNameCarDic)
CompanyList = []
CarList = []
GroupList = []

print(CarDic.loc[0,['汽车']]['汽车'])
print(CarDic.loc[0,['汽车公司']]['汽车公司'])
print(CarDic.loc[0,['汽车集团']]['汽车集团'])
# 将数据存储到三个列表中
for i in range(0,len(CarDic)):
    CompanyList.append(str(CarDic.loc[i,['汽车公司']]['汽车公司']))
    GroupList.append(str(CarDic.loc[i,['汽车集团']]['汽车集团']))
    str_temp_list = []
    str_temp_list = str(CarDic.loc[i,['汽车']]['汽车']).split(';')
    for j,stre in enumerate(str_temp_list):
        str_temp_list[j] = str_temp_list[j].replace(' ','')
    CarList.append(str_temp_list)
#对已经出现的汽车企业，按照长度进行排序
for i,care in enumerate(CarList):
    CarList[i].sort(key = lambda p:len(p),reverse=True)
    print(CarList[i])
#获取要标记的数据，并对每条结果进行处理
for m in range(400,1000):
    #fileName 是数据存放的路径，记得修改
    fileNameBase = r''
    fileName = fileNameBase+str(m)+".txt"
    # print(fileName)
    reader = open(fileName,encoding='utf-8')
    list_data = reader.readlines()
    s = ''
    for j in list_data:
        s += j
        s += '\n'
    res = []    #res存放记录的结果
    count = 1
    isInText = []
    print(s)
    isInAnn = np.zeros(len(s))
    ans = ""
    for k,c in enumerate(s):
        for i,care in enumerate(CarList):
            for j in CarList[i]:
                if(k+len(j) < len(s) and s[k:k+len(j)] == j and s[k] != '\n' and len(j) != 0 and j != '\n'):
                    print(s[k:k+len(j)] )
                    print(j)
                    print('*'*1000)
                    isAnnc = False
                    temp_count = k
                    while(temp_count < k+len(j)):
                        if(isInAnn[temp_count] == 1):
                            isAnnc = True
                            break
                        temp_count = temp_count+1
                    if(isAnnc == False):
                        ans = ans+'T'+str(count)+'\t'+'carLabel'+' '+str(k)+' '+str(k+len(j))+'\t'+s[k:k+len(j)]
                        res.append(ans)
                        ans = ""
                        count = count + 1
                        temp_count = k
                        while(temp_count < k+len(j)):
                            isInAnn[temp_count] = 1
                            temp_count = temp_count + 1
                        print(ans)
        for j in CompanyList:
            if(k + len(j) < len(s) and s[k:k + len(j)] == j and s[k] != '\n' and len(j) != 0 and j != '\n'):
                temp_count = k
                isAnnc = False
                while (temp_count < k + len(j)):
                    if (isInAnn[temp_count] == 1):
                        isAnnc = True
                        break
                    temp_count = temp_count + 1
                if (isAnnc == False):
                    ans = ans + 'T' + str(count) + '\t' + 'companyLabel' + ' ' + str(k) + ' ' + str(k + len(j)) + '\t' + s[k:k + len(j)]
                    res.append(ans)
                    ans = ""
                    count = count + 1
                    temp_count = k
                    while (temp_count < k + len(j)):
                        isInAnn[temp_count] = 1
                        temp_count = temp_count + 1
                    print(ans)
        for j in GroupList:
            if (k + len(j) < len(s) and s[k:k + len(j)] == j and s[k] != '\n' and len(j) != 0 and j != '\n'):
                temp_count = k
                isAnnc = False
                while (temp_count < k + len(j)):
                    if (isInAnn[temp_count] == 1):
                        isAnnc = True
                        break
                    temp_count = temp_count + 1
                if (isAnnc == False):
                    ans = ans + 'T' + str(count) + '\t' + 'companyLabel' + ' ' + str(k) + ' ' + str(k + len(j)) + '\t' + s[k:k + len(j)]
                    res.append(ans)
                    ans = ""
                    count = count + 1
                    temp_count = k
                    while (temp_count < k + len(j)):
                        isInAnn[temp_count] = 1
                        temp_count = temp_count + 1
                    print(ans)
    for i,resli in enumerate(res):
        print(i)
        print(resli)
    #writeNamebase是写入路径，记得修改
    writeNamebase = r''
    writeName = writeNamebase+str(m)+'.ann'
    f = open(writeName,'w',encoding='utf-8')
    for i in res:
        temp_line = i+'\n'
        f.write(temp_line)
    f.close()