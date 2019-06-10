def ReadWriteFile(f):
    d = open(f, encoding="utf8")
    f= open("SentensesListDistinct.txt","w+",encoding="utf8")

    d1 = d.readlines()
    ditinctSentences = findDistinct(d1)
    count= 0
    for x in ditinctSentences:
        count += 1
        f.write(removeNumbers(x,count))
    
    f.close()
    d.close()

def removeNumbersx(x):
    removelist = ["_","0","1","2","3","4","5","6","7","8","9"]
    newsent = ""
    for i in x:
        if i not in removelist:
            newsent += i
    return newsent

def removeNumbers(x,d):
    removelist = ["_","0","1","2","3","4","5","6","7","8","9"]
    newsent = str(d) + "."
    for i in x:
        if i not in removelist:
            newsent += i
    return newsent

def findDistinct(lines):
    distinct = []
    for x in lines:
        y = removeNumbersx(x)
        if y not in distinct:
            distinct.append(y)
    
    return distinct




file = "train.txt"
ReadWriteFile(file)
