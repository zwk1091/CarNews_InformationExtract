import numpy as np
import pandas as pd
import csv
import re

technologyPath = "技术词.txt"
carPath = "汽车词典统计.xlsx"

reader = open(technologyPath, encoding='utf-8')
technology_data = reader.readlines()
technology_data_length = len(technology_data)

car_data=pd.read_excel(carPath)
company=car_data["汽车集团"].values
company=list(set(company))
company_length=len(company)

car = car_data["汽车"].values
print (car[0])
car_length=len(car)

cars=[]
for i in range(car_length):
    cars += str(car[i]).split(";")
cars=list(set(cars))
cars_length=len(cars)
# print (cars)

print(car_data["汽车集团"].values)

for i in range(technology_data_length):
    technology_data[i] = technology_data[i].replace("\n", "")

count_technology = [0]*technology_data_length
count_company=[0]*company_length
count_car=[0]*cars_length
rawDataPath = "NewsCar_new_after_process/"
# 读取原始文件
for i in range(1,19782):
    inPath  = rawDataPath+str(int((i-1)/1000)+1)+"/"+str(i)+".txt"
    with open(inPath,'r',encoding="UTF-8" ) as f:
        text=f.read()
        # print (text)
        # print ("------------------------")
        for j in range(company_length):
            if(company[j] in text):
                count_company[j]=count_company[j]+1
        for j in range(cars_length):
            if (cars[j] in text):
                count_car[j] = count_car[j] + 1

        for j in range(technology_data_length):
            if(technology_data[j] in text):
                # print (technology_data[j])
                # print (i)
                count_technology[j]=count_technology[j]+1


name_technology=['technology','count']
name_company=['company','count']
name_car = ['car','count']

list_technology=[]
for i in range(technology_data_length):
    oneline=[]
    oneline.append(technology_data[i])
    oneline.append(count_technology[i])
    list_technology.append(oneline)
# print(list)

list_company=[]
for i in range(company_length):
    oneline=[]
    oneline.append(company[i])
    oneline.append(count_company[i])
    list_company.append(oneline)

list_cars=[]
for i in range(cars_length):
    oneline = []
    oneline.append(cars[i])
    oneline.append(count_car[i])
    list_cars.append(oneline)
# 负责排序
def takeSecond(elem):
    return elem[1]

list_technology.sort(key=takeSecond,reverse=True)
list_company.sort(key=takeSecond,reverse=True)
list_cars.sort(key=takeSecond,reverse=True)
# print(len(list))
res_technology = pd.DataFrame(columns=name_technology,data=list_technology)
res_technology.to_csv("count_technology.csv")

res_company=pd.DataFrame(columns=name_company,data=list_company)
res_company.to_csv("count_company.csv")

res_cars = pd.DataFrame(columns=name_car,data=list_cars)
res_cars.to_csv("count_cars.csv")



