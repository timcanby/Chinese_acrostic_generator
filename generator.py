import json
import os

import random
import argparse
def getfileFromfilter(rootdir):
    list = os.listdir(rootdir)
    ReturnList=[]
    for i in range(0, len(list)):
        if list[i]!='.DS_Store':

            path = os.path.join(rootdir, list[i])
            ReturnList.append(path)
    return (ReturnList)


def Gushigenerator(weight,text):

    sentencelist={}

    for eachJson in getfileFromfilter('json'):

        try:
            f=open(eachJson ,'r',encoding='utf-8')
            dict=json.load(f)

            for each in dict:
                for eachsentence in each['paragraphs']:
                    if len(eachsentence)==weight:

                        for eachCharacter in text:
                            if eachsentence[0] == eachCharacter:
                                sentencelist[each['author'],each['title'],eachsentence]=eachCharacter
        except:continue
    for eachcha in text:
        txt=[]
        for key, value in sentencelist.items():
            if value==eachcha:
                txt.append(key)
        print(random.choice(txt)[2])
parser = argparse.ArgumentParser(description='acrostic generator')
parser.add_argument('--Lengh', dest='length', type=int, default='16', help='12 or 16')
parser.add_argument('--Text', dest='Text', type=str, default='事事如意', help='Input the sentences：ex"事事如意"')
args = parser.parse_args()


try:
    Gushigenerator(args.length,args.Text)
except:
    print('no data')