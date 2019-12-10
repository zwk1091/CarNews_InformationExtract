import sys
import numpy as np
import pandas as pd
import re
import string
import matplotlib.pyplot as plt
import os
import jieba

def cut_sent(para):
    para = re.sub('([。！？\?])([^”’])', r"\1\n\2", para)  # 单字符断句符
    para = re.sub('(\.{6})([^”’])', r"\1\n\2", para)  # 英文省略号
    para = re.sub('(\…{2})([^”’])', r"\1\n\2", para)  # 中文省略号
    para = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', para)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = para.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    return para.split("\n")
def cut_voc(para):
    seg_list = jieba.cut(para)
    return seg_list

def cut_sentence_to_oneline(inPath, outPath):
    # 19782
    for i in range(1, 19782):
        infile = inPath + str(i) + ".txt"
        with open(infile, 'r', encoding="UTF-8") as f:
            sentenceList = []
            for line in f:
                line = line[3:]
                # line = clean_data(line)
                res = cut_sent(line)
                sentenceList.extend(res)
        resDir = int(i / 1000) + 1
        outDir = outPath+ str(resDir)
        # print (outDir)
        if not os.path.exists(outDir):
            os.makedirs(outDir)
        outfile = outDir + "/" + str(i) + ".txt"
        with open(outfile, "w", encoding="UTF-8") as resultFile:
            # print(sentenceList.__len__())
            resultFile.writelines("\n".join(sentenceList))
    return sentenceList

def cut_sentence_to_word(inPath, outPath):
    for i in range(1, 19782):
        infile = inPath + str(i) + ".txt"
        with open(infile, 'r', encoding="UTF-8") as f:
            sentenceList = []
            for line in f:
                line = line[3:]
                # line = clean_data(line)
                res = cut_sent(line)
                sentenceList.extend(res)
        resDir = int(i / 1000) + 1
        outDir = outPath + str(resDir)
        # print (outDir)
        if not os.path.exists(outDir):
            os.makedirs(outDir)
        outfile = outDir + "/" + str(i) + ".txt"
        with open(outfile, "w", encoding="UTF-8") as resultFile:
            # print(sentenceList.__len__())
            for sen in sentenceList:
                resultFile.writelines(" ".join(cut_voc(sen)))
                resultFile.writelines("\n")
    return

inPath="D:/知识图谱资料/NewsCar_new/NewsCar_new/"
outPath_oneline="D:/知识图谱资料/NewsCar_new_after_process/"
outPath_oneword ="D:/知识图谱资料/NewsCar_new_after_cutWord/"
cut_sentence_to_word(inPath, outPath_oneword)