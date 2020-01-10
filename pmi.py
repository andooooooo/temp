import re
import math
from scipy.stats import rankdata
import numpy as np
from util import bunkatsu, suujishori
import matplotlib.pyplot as plt
from collections import defaultdict
from statistics import mean, median,variance,stdev
from scipy.spatial.distance import correlation
from scipy.stats import spearmanr
from scipy.stats import kendalltau
from scipy.stats import pearsonr
import MeCab

"""
from collections import defaultdict

pmi={}
pmi2=[]
f = open("/Users/one/nlptutorial/data/wiki-en-test.word").readline
for line in f:
    line = line.rstrip()
    line = line.split(" ")
    for j  in line:
        if j not in pmi2:
            pmi2.append(j)

lines = ""
num = 0
for line in open("g.txt"):
    if "<div style" in line:
        line = line.replace(": 15px;\">",": 15px;\">\n<label class=\"newTaskFormQuestion\">")
    if "。" in line:
        line = line.replace("。","。</label>")
    if "<input name=" in line:
        line = line.replace("<input name","<label><input name")
        line = line.replace(" />"," /></label>")
        line = re.sub('name=\"[0-9]', "name=\"line"+str(num),line)
        num+=1
    line = line.replace("div", "p")
    lines += line

with open("renew.txt","w") as f:
    f.write(lines)
"""
"""
n=[]
for line in open("ex.py"):
    n.append(line.strip().split("\t"))
for i in range(6):
    xs=[]
    for xi in n[i]:
        xs.append(float(xi))
    array = np.array(xs)
    xs = rankdata(array)
    for j in range(i+1,6):
        N=0
        K=0
        L=0
        tx=0
        ty=0
        ys=[]
        for yi in n[j]:
            ys.append(float(yi))
        array = np.array(ys)
        ys = rankdata(array)
        for k in range(len(xs)):
            for z in range(k+1,len(xs)):
                if xs[k] > xs[z] and ys[k] > ys[z]:
                    K+=1
                elif xs[k] < xs[z] and ys[k] < ys[z]:
                    K+=1
                elif xs[k] == xs[z]:
                    tx += 1
                elif ys[k] == ys[z]:
                    ty += 1
                else:
                    L+=1
                N+=1
        print((K-L)/(math.sqrt(N-tx)*math.sqrt(N-ty)))
"""
"""
maea=0
maed=0
atoa=0
atod=0
mode=0
ae=0
aa=0
de=0
da=0
a=0
d=0
for line in open("/Users/one/ad.csv"):
    line = line.strip().split(",")
    lastline = line
    if "a" in line[1] and line[2] != "":
        num = float(line[2])
        if num == 1 :
            ae +=1
        else:
            aa +=1
    if "d" in line[1] and line[2] != "":
        num = float(line[2])
        if num ==1:
            de +=1
        else:
            da +=1
    if "カルテ" in line[0]:
        continue
    if "入院まで" in line[0] or "入院前" in line[0] or "現病" in line[0]:
        mode = 1
    if mode == 1:
        if "a" in line[1]:
            maea += 1
        if "d" in line[1]:
            maed += 1
    if "入院後" in line[0] or "入院中" in line[0]:
        if "a" in lastline[1]:
            a += 1
        if "d" in lastline[1]:
            d += 1
    if mode ==2:
        if "a" in line[1]:
            atoa += 1
        if "d" in line[1]:
            atod += 1
print(maea,maed,atoa,atod)
print(da,de,aa,ae)
print(a,d)
"""
"""
def extcarte (filemei):
    lists = "poi"
    summary = []
    summary2 = []
    carte = []
    lastsentense2 = ""
    flag2 = 0
    for line in open(filemei):
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
        if lists == "poi":
            continue
        if "---date---" in line:
            continue
        lists,flag2,lastsentense2 = bunkatsu(line,flag2,lists,lastsentense2)
    carte = suujishori(carte)
    summary = suujishori(summary)
    summary2 = suujishori(summary2)
    return carte


def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


taiou = {}
sinline = ""
count = 0
flag = 0
for line in open("taiou.csv"):
    taiou[line.strip().split()[1]] = line.strip().split()[0]
for line in open("a-d.csv"):
    print(count)
    line = line.strip()
    sub = line.split(",")
    if "カルテ" in sub[0]:
        num = re.search('[0-9]+',sub[0]).group()
        if "koko" in sub[0] or flag == 1:
            flag = 1
            docnum = int(num)
        elif "@" in sub[0]:
            docnum = taiou[num + "@"]
        else:
            docnum = taiou[num.zfill(2)]
        sinline += line + "," + "\n"
        continue
    sumsen = sub[2]
    if sumsen == "":
        continue
    saichou = 0
    for i in extcarte(str(docnum)+".md"):
        icchi = long_substr([i,sumsen])
        if saichou < len(icchi):
            saichou = len(icchi)
    kasanarido = saichou/len(sumsen)
    sinline += line + "," + str(kasanarido) + "\n"
    count += 1
with open("sinad.csv","w")as f:
    f.write(sinline)
"""
"""
stat = ""
koudou = 0
taiou =0
chiryou =0
sindan =0
suitei =0
kanousei =0
state = [[0,0,0,0,0,0],[0,0,0,0,0,0]]
for line in open("shousai.csv"):
    stat = ""
    c=[0,0,0,0,0,0]
    line = line.strip().split(",")
    #print(line[-1])
    if line[-1] == "":
        continue
    if line[4] != "":
        c[0]=1
    if line[5] != "":
        c[1]=1
    if line[6] != "":
        c[2]=1
    if line[7] != "":
        c[3] =1
    if line[8] != "":
        c[4]=1
    if line[9] != "":
        c[5]=1
    if line[2] != "":
        stat = "kanja"
    if line[3] != "":
        stat = "hikanja"
    if line[2] != "" and line[3] != "":
        stat = "kankanja"
    if line[2] == "" and line[3] == "":
        stat = "shindekudasai"
"""
"""
    if stat == "kanja":
        for i in range(6):
            state[0][i]+=c[i]
    if stat == "hikanja":
        for i in range(6):
            state[1][i]+=c[i]
    if stat == "kankanja":
        for i in range(6):
            state[0][i]+=c[i]
            state[1][i]+=c[i]
"""
"""
    co=0
    if stat == "shindekudasai":
        for i in range(6):
            co+=c[i]
            state[1][i]+=c[i]
        if co == 0:
            taiou+=1
print(state,taiou)
"""
"""
e = 0
a = 0
ea = 0
ed = 0
aa = 0
ad = 0
for line in open("sinad.csv"):
    line =line.strip().split(",")
    if line[1] == "":
        continue
    if float(line[3]) >= 1.0:
        e += 1
        if line[1] == "a":
            ea += 1
        else:
            ed += 1
    else:
        a += 1
        if line[1] == "a":
            aa += 1
        else:
            ad += 1
print(e,a,ea,ed,aa,ad)
"""
"""
def spearman(list_a, list_b):
    N = len(list_a)                                                          
    return 1 - ((6 * sum(map(lambda a, b: (a - b) ** 2,list_a, list_b) / float(N ** 3 - N))))

mecab = MeCab.Tagger('-u /Users/one/Downloads/ComeJisyoV5-0993/user.dic')
statlist=[]
co=0
flag = 0
templist = []
kekka = defaultdict(list)
c=0
w=0
s=0
sd=[]
cd=[]
wd=[]
b=0
for line in open("sinad.csv"):
    w=0
    c=0
    line =line.strip().split(",")
    sentence = line[2].replace("<comma>",",")
    if "カルテ" in line[0]:
        
        if flag == 1 or flag == 2:
            if co != 0:
                statlist.append((templist,1/co))
        flag = 1
        co=0
        templist = []
        
        continue
    
    if "入院まで" in line[0] or "現病" in line[0] or "入院前" in line[0]:
        flag =1
        sd.append(s)
        s=0
        b+=1
    
    if "入院後" in line[0] or "入院中" in line[0]:
        sd.append(s)
        s=0
        b+=1
        flag = 2
    
    if flag == 2:
        c += len(sentence)
        node = mecab.parseToNode(sentence)
        while node:
            w+=1
            node = node.next
        s+=1
        cd.append(c)
        wd.append(w)
        continue
    
    if line[1] == "a":
        templist.append(1)
    else:
        templist.append(0)
"""
"""
    if float(line[3]) == 1.0:
        templist.append(1)
    else:
        templist.append(0)
"""
"""
    co+=1
if co != 0:
    statlist.append((templist,1/co))
for i in statlist:
    memori = i[1]*100
    memori = int(memori)
    mae = 0
    zenji = 0
    for k in i[0]:
        zenji += memori
        for j in range(mae,zenji):
            #print(j)
            kekka[j].append(k)
        mae = zenji
        saigo = k
        if zenji >= 100:
            zenji = 100
    if zenji < 100:
        #print(zenji)
        for j in range(zenji,100):
            #print(j)
            kekka[j].append(saigo)
saishuu = []
#print(len(kekka))
for i in kekka:
    #print(len(kekka[i]))
    saishuu.append(mean(kekka[i]))
#print(mean(sd),mean(wd),mean(cd),b)

x = []
for i in range(0,100):
    x.append(i)
plots = plt.plot(x, saishuu)
plt.ylim([0.60,0.96])
plt.show()
#print(len(saishuu))
"""
"""
statlist=[]
co=0
flag = 0
templist = []
kekka = defaultdict(list)
for line in open("sinad.csv"):
    line =line.strip().split(",")
    if "入院後" in line[0] or "入院中" in line[0]:
        flag = 2
    if "カルテ" in line[0]:
        if flag == 1 or flag == 2:
            if co != 0:
                statlist.append((templist,1/co))
        flag = 1
        co=0
        templist = []
        continue
    if flag == 2:
        continue
"""
"""
    if line[1] == "d":
        templist.append(1)
    else:
        templist.append(0)
"""
"""
    if float(line[3]) == 1.0:
        templist.append(1)
    else:
        templist.append(0)
    
    co+=1
if co != 0:
    statlist.append((templist,1/co))
for i in statlist:
    memori = i[1]*100
    memori = int(memori)
    mae = 0
    zenji = 0
    for k in i[0]:
        zenji += memori
        for j in range(mae,zenji):
            #print(j)
            kekka[j].append(k)
        mae = zenji
        saigo = k
        if zenji >= 100:
            zenji = 100
    if zenji < 100:
        #print(zenji)
        for j in range(zenji,100):
            #print(j)
            kekka[j].append(saigo)
saishuu2 = []
#print(len(kekka))
for i in kekka:
    #print(len(kekka[i]))
    saishuu2.append(mean(kekka[i]))
correlation, pvalue = spearmanr(saishuu,saishuu2)
print("相関係数", correlation)   
print("p値",pvalue)
"""
"""
mecab = MeCab.Tagger('-u /Users/one/Downloads/ComeJisyoV5-0993/user.dic')
summary=0
summary2=0
h=0
w=0
for i in range(1,109):
    f=0
    flag = 0
    for line in open(str(i)+".md"):
        line = line.strip()
        if len(line) == 0:
            continue
        if "---summary---" in line:
            summary+=1
            f+=1
            flag = 1
            continue
        if "---/summary---" in line:
            #lists = carte
            flag = 1
            continue
        if "---summary2---" in line:
            summary2+=1
            f+=1
            flag = 1
            continue
        if "---/summary2---" in line:
            #lists = carte
            flag = 1
            continue
        if "---date---" in line:
            continue
        if "tag" in line:
            continue
        if flag == 1:
            w+=1
print(w)
"""
def extcarte (filemei):
    lists = "poi"
    summary = []
    summary2 = []
    carte = []
    lastsentense2 = ""
    flag2 = 0
    for line in open(filemei):
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
        if lists == "poi":
            continue
        if "---date---" in line:
            continue
        lists,flag2,lastsentense2 = bunkatsu(line,flag2,lists,lastsentense2)
    carte = suujishori(carte)
    summary = suujishori(summary)
    summary2 = suujishori(summary2)
    return (carte,summary,summary2)


def long_substr(data):
    substr = ''
    if len(data) > 1 and len(data[0]) > 0:
        for i in range(len(data[0])):
            for j in range(len(data[0])-i+1):
                if j > len(substr) and is_substr(data[0][i:i+j], data):
                    substr = data[0][i:i+j]
    return substr

def is_substr(find, data):
    if len(data) < 1 and len(find) < 1:
        return False
    for i in range(len(data)):
        if find not in data[i]:
            return False
    return True


taiou = {}
sinline = ""
count = 0
flag = 0
for n in range(1,109):
    i=extcarte(str(n)+".md")
    if len(i[1]) != 0:
        for j in i[1]:
            for z in i[0]:
                icchi = long_substr([j,z])
                if len(j) == len(icchi):
                    count += 1
                    break
                else:
                    flag += 1
    if len(i[2]) != 0:
        for j in i[2]:
            for z in i[0]:
                icchi = long_substr([j,z])
                if len(j) == len(icchi):
                    count += 1
                    break
                else:
                    flag += 1
print(count,flag)
