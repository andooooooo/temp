import sys
from collections import defaultdict
import re
import ngram
import matplotlib.pyplot as plt
from statistics import mean, median,variance,stdev
from util import bunkatsu, suujishori
import MeCab
from statistics import mean

if __name__ == '__main__':
    """
    sentenceSet = []
    doc = open("4.txt").read()
    for sentences in doc.split("/文末/"):
        sentences = sentences.replace("<comma>",",").replace("slash","@").replace("space"," ").strip("\"")
        sentences = sentences.strip()
        sentence2 = ""
        flag = 0
        sentence = ""
        kugiri = ""
        for i in list(sentences):
            if flag == 1:
                if i == "/":
                    flag = 0
                    kugiri = kugiri[:-1]
                    kugiri += "|" + "\t"
            elif i == "/":
                flag = 1
            else:
                sentence += i + "\t"
                kugiri += "\t"
        aftersentence = ""
        info = []
        sentenceSet.append(sentence)
        sentenceSet.append(kugiri)
    with open("clause2.txt","w")as f:
        f.write("\n".join(sentenceSet).replace("@","/"))
    """
    
    sentenceSet = []
    mecab = MeCab.Tagger('-u /Users/one/Downloads/ComeJisyoV5-0993/user.dic')
    for sentence in open("/Users/one/carte/data/sinad.csv"):
        sentence2 = ""
        sentence = sentence.strip().split(",")
        sentence = sentence[2].replace("<comma>",",").strip("\"")
        #print(sentence)
        sentence = sentence.strip().replace(" ","　")
        node = mecab.parseToNode(sentence)
        aftersentence = ""
        kugiri = ""
        info = []
        while node:
            info.append((node.surface, node.feature.split(",")[0], node.feature.split(",")[1], node.feature.split(",")[6]))
            node = node.next
        if len(info) ==2:
            continue
        for i in list(sentence):
            sentence2 += i + "\t"
        sentenceSet.append(sentence2)
        if len(info) <5:
            continue
        #print(info)
        for i in range(len(info)):
            if i == 0:
                beforeOne ,beforeTwo, afterOne, afterTwo = ["","","",""], ["","","",""], info[i+1], info[i+2]
            elif i == 1:
                beforeOne ,beforeTwo, afterOne, afterTwo = info[i-1], ["","","",""], info[i+1], info[i+2]
            elif i+1 == len(info):
                beforeOne ,beforeTwo, afterOne, afterTwo = info[i-1], info[i-2] ,["","","",""] , ["","","",""]
            elif i+2 == len(info):
                beforeOne ,beforeTwo, afterOne, afterTwo = info[i-1], info[i-2] ,info[i+1], ["","","",""]
            else:
                beforeOne ,beforeTwo, afterOne, afterTwo = info[i-1], info[i-2] ,info[i+1], info[i+2]
            #print(beforeOne[1])
            if info[i][2] == "サ変接続" and afterOne[1] == "名詞":
                aftersentence += info[i][0] + "|"
            elif info[i][2] == "読点" or info[i][2] == "句点":
                aftersentence += info[i][0] + "|"
            elif info[i][1] == "動詞" and afterOne[1] != "助動詞" and beforeOne[1] != "動詞":
                aftersentence += info[i][0] + "|"
            elif info[i][1]=="助動詞" and afterOne[1] != "助動詞":
                aftersentence += info[i][0] + "|"
            elif beforeOne[0]=="こと" and info[i][2] == "格助詞":
                aftersentence += info[i][0] + "|"
            elif info[i][2]=="接続助詞" and afterOne[2] != "読点":
                aftersentence += info[i][0] + "|"
            elif info[i][2] == "括弧開" or info[i][2] == "括弧閉":
                aftersentence += info[i][0] + "|"
            elif info[i][3]=="副詞可能" and afterOne[2] != "読点":
                aftersentence += info[i][0] + "|"
            elif info[i][2] == "係助詞":
                aftersentence += info[i][0] + "|"
            else:
                aftersentence += info[i][0]
        flag = 0
        for i in list(aftersentence):
            if flag == 1:
                flag = 0
                continue
            if i == "|":
                kugiri = kugiri[:-1]
                kugiri += "|" + "\t" + "\t"
                flag = 1
            else:
                kugiri += "\t"
        
        sentenceSet.append(kugiri)
    with open("clause.txt","w")as f:
        f.write("\n".join(sentenceSet))
    
    """
    sentenceSet = []
    mecab = MeCab.Tagger('-u /Users/one/Downloads/ComeJisyoV5-0993/user.dic')
    for sentence in open("/Users/one/carte/data/sinad.csv"):
        sentence = sentence.strip().split(",")
        sentence = sentence[2].replace("<comma>",",")
        #print(sentence)
        node = mecab.parseToNode(sentence)
        aftersentence = ""
        info = []
        while node:
            info.append((node.surface, node.feature.split(",")[0], node.feature.split(",")[1], node.feature.split(",")[6]))
            node = node.next
        if len(info) ==2:
            continue
        if len(info) <5:
            sentenceSet.append(sentence)
            continue
        #print(info)
        for i in range(len(info)):
            if i == 0:
                beforeOne ,beforeTwo, afterOne, afterTwo = ["","","",""], ["","","",""], info[i+1], info[i+2]
            elif i == 1:
                beforeOne ,beforeTwo, afterOne, afterTwo = info[i-1], ["","","",""], info[i+1], info[i+2]
            elif i+1 == len(info):
                beforeOne ,beforeTwo, afterOne, afterTwo = info[i-1], info[i-2] ,["","","",""] , ["","","",""]
            elif i+2 == len(info):
                beforeOne ,beforeTwo, afterOne, afterTwo = info[i-1], info[i-2] ,info[i+1], ["","","",""]
            else:
                beforeOne ,beforeTwo, afterOne, afterTwo = info[i-1], info[i-2] ,info[i+1], info[i+2]
            #print(beforeOne[1])
            if info[i][2] == "サ変接続" and afterOne[1] == "名詞":
                aftersentence += info[i][0]
            elif info[i][1] == "動詞" and (afterOne[1] != "動詞" and afterTwo[1] != "動詞")and (afterOne[2] != "連体化" and afterTwo[2] != "連体化")and (afterOne[3] != "体言接続" and afterTwo[3] != "体言接続"):
                    aftersentence += info[i][0] + "|"
            elif info[i][1]=="助動詞" and (afterOne[1] != "助動詞" and afterTwo[1] != "助動詞") and (beforeOne[1] != "動詞" and beforeTwo[1] != "動詞"):
                aftersentence += info[i][0] + "|"
            else:
                aftersentence += info[i][0]
        sentenceSet.append(aftersentence)
    with open("clause.txt","w")as f:
        f.write("\n".join(sentenceSet))
"""
#elif (info[i][1] == "動詞" or info[i][2] == "サ変接続") and (afterOne[1] != "動詞" and afterTwo[1] != "動詞") and (afterOne[2] != "サ変接続" and afterTwo[2] != "サ変接続") and afterOne[1] != "助動詞":
# (beforeOne[1] != "動詞" and beforeTwo[1] != "動詞") and

"""
    document = []
    keys=defaultdict(int)
    lastsentense2 = ""
    flag2 = 0
    for i in range(1,109):
        summary = []
        summary2 = []
        carte = []
        num = str(i).zfill(3)
        lists = "poi"
        for line in open(str(i)+".md"):
            line = line.strip()
            if len(line) == 0:
                continue
            if "---summary---" in line:
                lists = summary
                continue
            if "---/summary---" in line:
                lists = carte
                continue
            if "---summary2---" in line:
                lists = summary2
                continue
            if "---/summary2---" in line:
                lists = carte
                continue
            if "<tag>" in line:
                continue
            if "</tag>" in line:
                continue
            if "---date" in line:
                continue
            if lists == "poi":
                continue
            if "---date---" in line:
                continue
            #print(type(line),type(flag2),type(lastsentense2),type(lists))
            lists,flag2,lastsentense2 = bunkatsu(line,flag2,lists,lastsentense2)
        #print(len(summary),len(summary2))
        carte = suujishori(carte)
        summary = suujishori(summary)
        summary2 = suujishori(summary2)
        document.append((carte,summary,summary2))


zeroone=0
zerozero=0
oneone =0
onezero=0
bunsuu = 0
goi = defaultdict(int)
mecab = MeCab.Tagger('-u /Users/one/Downloads/ComeJisyoV5-0993/user.dic')
count=0
#print(len(document))
totte1 =[]
totte2=[]
totte3=[]
tott1 =[]
tott2=[]
tott3=[]
to1 =[]
to2=[]
to3=[]
for i in document:
    bunsuu += 1
    to1.extend( i[0])
    to1.extend(i[1])
    to1.extend(i[2])
    with open("kari.txt","a")as f:
        f.write(str(bunsuu) + "\n" + "\n".join(to1))
    to1 = []
"""
"""
for i in document:
    count+=1
    #rint(i[1])
    t=0
    t2=0
    t3=0
    for x in i[0]:
        t+=len(x)
        #print(x)
        node = mecab.parseToNode(x)
        c=0
        while node:
            goi[node.surface] += 1
            c+=1
            node = node.next
        to1.append(c)
    for y in i[1]:
        t2+=len(y)
        #print(y)
        node = mecab.parseToNode(y)
        c=0
        while node:
            goi[node.surface] += 1
            c+=1
            node = node.next
        to2.append(c)
    tott2.append(t2/t)
    for z in i[2]:
        t3+=len(z)
        #print(z)
        node = mecab.parseToNode(z)
        c=0
        while node:
            goi[node.surface] += 1
            c+=1
            node = node.next
        to3.append(c)
    tott3.append(t3/t)

    bunsuu += len(i[0])
    totte1.append(len(i[0]))
    bunsuu += len(i[1])
    totte2.append(len(i[1]))
    bunsuu += len(i[2])
    totte3.append(len(i[2]))
    if len(i[1]) == 0:
        if len(i[2]) == 0:
            zerozero += 1
        else:
            zeroone += 1
    else:
        if len(i[2]) == 0:
            onezero += 1
        else:
            oneone += 1
#print(zerozero,zeroone,onezero,oneone)
print(len(goi))
print(mean(totte1),mean(totte2),mean(totte3),mean(tott2),mean(tott3))
"""
"""
    print(len(document))
    #print(len(carte),len(summary),len(summary2))
    #26517 2980 2759
    value = []
    count = 0
    documentbetu = []
    for i in document:
        value = []
        if len(i[1]) ==0:
            continue
        n = ngram.NGram(i[0],pad_len=1)
        for j in i[1]:
            result = n.search(j)
            result=result[0] if len(result)!=0 else ("","0")
            value.append(float(result[1]))
        documentbetu.append(mean(value))
    #print(len(documentbetu))
    for i in value:
        if i == 1:
            count += 1
    print(count,len(value))
    #dic = {0:0,1*20:0,2*20:0,3*20:0,4*20:0,5*20:0,6*20:0,7*20:0,8*20:0,9*20:0,10*20:0,11*20:0,12*20:0,13*20:0,14*20:0,15*20:0,16*20:0,17*20:0,18*20:0,19*20:0,20*20:0}
    #print(max(sumary),min(sumary),mean(sumary),median(sumary))
    #keys = sorted(keys.items(), key=lambda x: x[0])
    
    dic = {}
    for i in range(11):
        dic[i/10] = 0
    tate=[]
    yoko=[]
    #print(keys)
    for i in documentbetu:
        dic[int(i*10)/10] += 1
        #print(mean(i))
    keys = sorted(dic.items())
    #print(keys)
    for i in keys:
        tate.append(i[0])
        yoko.append(i[1])
    #print(yoko,tate)
    plt.plot(tate,yoko)
    plt.show()
    #461
"""
"""
retu = ""
for sentence in open("sinad.csv"):
    sentence = sentence.strip().split(",")
    sentence = sentence[2].replace("<comma>","、").strip("\"")
    sentence = sentence.replace("/", "slash").strip()
    if sentence[-1] == "." or sentence[-1] == "．":
        sentence = sentence[:-1] + "。"
    elif sentence[-1] != "。":
        sentence = sentence + "。"
    retu += sentence
"""
"""
c = 0
new = ""
for sentence in open("clause2.txt"):
    sentence = sentence.rstrip("\n")
    c += 1
    if c%2 == 0:
        sentence = sentence[:-1]
        new += sentence + "|\n"
    else:
        new += sentence + "\n"
with open("clause3.txt", "w")as f:
    f.write(new)
"""
