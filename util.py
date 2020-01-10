import sys
import re

pattern = r"[^。.．]+[。.．]?"
pattern2 = r"[0-9０-９]+[.．]+"

def suujishori(numlis):
    kanlis = []
    flag = 0
    temp = ""
    for i in range(len(numlis)):
        text2 = numlis[i][-2:]
        hantei = re.match(pattern2,text2)
        if not isinstance(hantei,type(None)):
            if temp == "":
                temp = numlis[i]
            temp = temp + numlis[i+1]
            flag = 1
        else:
            if flag == 0:
                kanlis.append(numlis[i])
            else:
                kanlis.append(temp)
                temp = ""
                flag = 0
    return kanlis

def bunkatsu(line,flag,sentences,lastsentense):
    if flag == 0:
        if "。" in line:
            if "、" == line[-1] or "," == line[-1]:
                sentences.extend(re.findall(pattern,line)[:-1])
                flag = 1
                lastsentense = str(re.findall(pattern,line)[:-1])
            else:
                sentences.extend(re.findall(pattern,line))
        else:
            if "、" == line[-1] or "," == line[-1]:
                flag = 1
                lastsentense = line
            else:
                sentences.append(line)
    else:
        if "。" in line:
            if "、" == line[-1] or "," == line[-1]:
                sentences.extend(re.findall(pattern,line)[1:-1])
                flag = 1
                temp = lastsentense + str(re.findall(pattern,line)[0])
                sentences.append(temp)
                lastsentense = str(re.findall(pattern,line)[:-1])
            else:
                sentences.extend(re.findall(pattern,line)[1:])
                temp = lastsentense + str(re.findall(pattern,line)[0])
                sentences.append(temp)
                flag = 0
                lastsentense = ""
        else:
            if "、" == line[-1] or "," == line[-1]:
                flag = 1
                lastsentense = lastsentense + line
            else:
                sentences.append(lastsentense + line)
                flag = 0
                lastsentense = ""
    #(type(sentences),type(flag),type(lastsentense))
    return sentences,flag,lastsentense
