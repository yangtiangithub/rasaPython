from pyltp import Segmentor, Postagger,Parser,SementicRoleLabeller,NamedEntityRecognizer
import os

LTP_DATA_DIR = ".\ltp_data_v3\ltp_data_v3.4.0"#LTP模型目录
cws_model_path = os.path.join(LTP_DATA_DIR, "cws.model")    #分词模型路径
pos_model_path = os.path.join(LTP_DATA_DIR, 'pos.model')    #词性标注路径
pas_model_path = os.path.join(LTP_DATA_DIR, "parser.model")     #依存句法路径
# srl_model_path = os.path.join(LTP_DATA_DIR, 'srl')  # 语义角色标注模型目录路径，模型目录为`srl`。注意该模型路径是一个目录，而不是一个文件。
ner_model_path = os.path.join(LTP_DATA_DIR, 'ner.model')  # 命名实体识别模型路径，模型名称为`pos.model`


#分词实例
segmentor = Segmentor()
segmentor.load(cws_model_path)
#词性标注
postagger = Postagger()
postagger.load(pos_model_path)
#依存句法
parser = Parser()
parser.load(pas_model_path)
#命名实体识别
recognizer = NamedEntityRecognizer() # 初始化实例
recognizer.load(ner_model_path)  # 加载模型
'''
#语义角色标注
labeller = SementicRoleLabeller() # 初始化实例
labeller.load(srl_model_path)  # 加载模型
'''

#分词
words = segmentor.segment("我想听周杰伦的歌")
# print ("|".join(words))
# print("type words:",type(words))
# print("words:",words)
# segmentor.release()
list_words = list(words)
print("list_words :",list_words)
#词性标注
postags = postagger.postag(words)
# print("type postagger:",type(postags))
# print("postags:",postags)
list_postags = list(postags)
print(list_postags)
#依存句法
arcs = parser.parse(list_words,list_postags)
print(type(arcs))
print("\t".join("%d:%s" % (arc.head, arc.relation) for arc in arcs))
'''
#语义角色标注
roles = labeller.label(words, postags, arcs)  # 语义角色标注
for role in roles:
    print (role.index, "".join(
        ["%s:(%d,%d)" % (arg.name, arg.range.start, arg.range.end) for arg in role.arguments]))
'''

# 命名实体识别
netags = recognizer.recognize(words, postags)
print ('\t'.join(netags))

# print("打印arcs属性",dir(arcs))
print('后面是for')
for w in words:
    print(w)
for arc in arcs:
    print(arc.head,":",arc.relation)

# print("打印arc属性", dir(arcs[0]))

SOVS = []
for index_subject in range(len(arcs)):
    if arcs[index_subject].relation == "SBV":
        predicate = words[arcs[index_subject].head-1] # 谓语
        subjects = [words[index_subject]]  # 主语列表
        binyus = [] # 宾语列表

        index_bin = -1
        for index_coo in range(len(arcs)):
            if arcs[index_coo].relation == "COO" and arcs[index_coo].head == index_subject+1:
                subjects.append(words[index_coo])  # 并列主语
            elif arcs[index_coo].relation == "VOB" and arcs[index_coo].head == arcs[index_subject].head:
                index_bin = index_coo
                binyus.append(words[index_coo])
            elif index_bin > 0 and arcs[index_coo].relation == "COO" and arcs[index_coo].head == index_bin + 1:
                binyus.append(words[index_coo])

        for subj in subjects:
            if len(binyus) > 0:
                for binyu in binyus:
                    print (subj, predicate, binyu)
                    SOVS.append((subj, predicate, binyu))
            else:
                print (subj,predicate)
                SOVS.append((subj,predicate))
print(SOVS)

# 释放模型
segmentor.release()
postagger.release()
parser.release()
recognizer.release()
# labeller.release()