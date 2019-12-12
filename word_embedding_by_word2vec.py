from gensim.models import word2vec

# 加载分词后的文件(使用jieba分词)
sentences=word2vec.Text8Corpus('../NewsCar_new_after_cutWord/1/2.txt')

# size 表示词向量维度 min_count表示最小出现次数
model=word2vec.Word2Vec(sentences,size=100,min_count=1)

# 计算和动力最相似的5个词
x=model.most_similar("动力",topn=5)
print (x)

# 输出'汽车'的词向量
print(model['汽车'])

# 保存模型
model.save("res.model")
# 对应的加载方式
# model_2 = word2vec.Word2Vec.load("text8.model")



