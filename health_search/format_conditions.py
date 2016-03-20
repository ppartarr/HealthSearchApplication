import re

def openfile():
    file=open("conditions.txt","r")
    conditions=[]
    condition=file.readline()
    while True:
        if condition=='':
            break
        conditions+=[re.sub("[\(\[].*?[\)\]]", "",condition)]
    return conditions