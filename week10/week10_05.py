# week10_05.py
import os
mypath = "c:\\s202444095"
myfile = "kjm_02.txt"

if False == os.path.exists(mypath):
    os.mkdir(mypath)
myfullfile = mypath + "\\" + myfile
if os.path.exists(myfullfile):
    scores = []
    with open(myfullfile, 'r') as f:
        lines = f.readlines()
        for line in lines:
            dict_scores = {}
            sub_scores = line.strip().split('|')
            for sub_score in sub_scores:
                kv = sub_score.split(',')
                dict_scores[kv[0]] = int(kv[1])
            if dict_scores:
                scores.append(dict_scores)
    if scores:
        for score in scores:
            print(score)
else:
    f = open(myfullfile, 'w')
    f.close()
'''
with open(myfullfile, 'r') as f:
        lines = f.readlines() #'m, 12|k, 22|e, 322\n'
        for line in lines:
            sub_scores = line.strip().split('|') #['m,12','k,20','e,322']
            for sub_score in sub_scores: #'m,10'
                kv = sub_score.split(',') #['m', '10']
                '''
