from gensim.models import word2vec

# 加载分句后的文件
sentences=word2vec.Text8Corpus('NewsCar_new_after_process/1/2.txt')

# 转换为一个个字
tokens=[]
for sen in sentences:
    print (type(sen))
    for j in sen:
        for token in j:
            tokens.append(token)

# size 表示向量维度 min_count表示最小出现次数
model=word2vec.Word2Vec(tokens,size=100,min_count=1)

# 计算和车最相似的5个字
x=model.most_similar("车",topn=5)
print (x)

# 输出'汽车'的词向量
print(model['车'])

# 保存模型
model.save("res.model")
# 对应的加载方式
# model_2 = word2vec.Word2Vec.load("text8.model")



