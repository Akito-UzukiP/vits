import json
import os


a01 = open("./logs/uma.json",encoding='GBK')
js  = json.load(a01)
umaDict = dict()
for i in range(0,len(js['speakers'])):
    umaDict[js['speakers'][i]]=i
print(umaDict)





'''path0 = "./new/scn/"
for dirpath,dirnames,filenames in os.walk(path0):
    for path in filenames:
        a01 = open(path0 +path,encoding='UTF-8')
        output = open('NNNkr.txt', 'a',encoding='UTF-8')
        j01=json.load(a01)
        if not 'scenes' in j01:
            continue
        for i in j01['scenes']:
            if i is None or not 'texts' in i:
                continue
            for j in i['texts']:
                if j[3] is not None:
                    if'kr' in j[3][0]['voice']:
                        temp = j[2][0][1].strip("「")
                        temp = temp.strip("」")
                        temp = temp.replace('\\n', '')
                        outstring = 'dataset/kr/NNN'+j[3][0]['voice']+'.wav|'+temp+"\n"
                        print(outstring)

                        output.write(outstring)

'''