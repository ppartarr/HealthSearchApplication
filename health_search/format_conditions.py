import re

def openfile():
    file=open("conditions.txt","r")
    conditions=[]
    while True:
        condition=file.readline()
        if condition=='':
            break
        conditions+=[re.sub("[\(\[].*?[\)\]]", "",condition)[:-1]]
    return conditions

print openfile()