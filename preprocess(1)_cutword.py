import sys
import numpy as np
import pandas as pd
import re
import string
from zhon.hanzi import punctuation
import matplotlib.pyplot as plt
import os
import jieba

#清洗文本
def clean_text(text) :
    # 多个空格替换成一个
    text = re.sub(' +', '', text)
    text = re.sub(' ', '', text)
    text = re.sub('(.top_navdiva{.*})', ';', text)
    return text

def isDirtydata(text):
    jsElement=['fuction','document','window','padding','getElements','http']
    count=0
    for e in jsElement:
        count = count+text.count(e)
    if( count>2 ):
        return True
    else:
        return False

def cut_sent(para):
    para = re.sub('([。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split("\n")

#使用jieba分词
def cut_voc(para):
    seg_list = jieba.cut(para)
    return seg_list

path="NewsCar_new_after_process"
if not os.path.exists(path):
    os.makedirs(path)


inPath="NewsCar_new/NewsCar_new/"
outPath="NewsCar_new_after_process/"
outPath_afterCutWord ="NewsCar_new_after_cutWord/"

#19782
for i in range(1,19782):
    infile=inPath+str(i)+".txt"

    with open(infile, 'r', encoding="UTF-8" ) as f:
        sentenceList = []
        vocabularyList = []
        for line in f:
            line = line[3:]
            # line = clean_data(line)
            res = cut_sent(line)
            for sen in res:
                sen = clean_text(sen)
                if (not isDirtydata(sen)):
                    sen = cut_voc(sen)
                    vocabularyList.extend(sen)

    resDir = int(i / 1000) + 1
    outDir = outPath_afterCutWord + str(resDir)
    # print (outDir)
    if not os.path.exists(outDir):
        os.makedirs(outDir)
    outfile = outDir + "/" + str(i) + ".txt"
    with open(outfile, "w", encoding="UTF-8") as resultFile:
        # print(sentenceList.__len__())
        resultFile.writelines("\n".join(vocabularyList))

