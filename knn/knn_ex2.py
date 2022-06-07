import math
from random import randint
import turtle


class Sample:
    def __init__(self, x1, x2,label):
        self.x1 = x1
        self.x2 = x2
        self.label = label

def getlabel(test,trainingdata,k):
    d=list()
    for t in trainingdata:
        label=t.label
        d1=math.sqrt(pow(test.x1-t.x1,2)+pow(test.x2-t.x2,2))
        d.append((d1,label))
    d.sort()
    # print(d[:k-1])
    ca=0
    cb=0
    for i in range(k):
        if d[i][1]==0:
            ca+=1
        else: cb+=1
    if ca >cb:
        return "+"
    return "-"
def confusionmatrix(testingdata,labels):
    pp=0
    pn=0
    np=0
    nn=0
    for i in range(0,len(testingdata)):
        if testingdata[i].label=="+" and labels[i]=="+":
            pp+=1
        elif testingdata[i].label=="+" and labels[i]=="-":
            pn+=1
        elif testingdata[i].label=="-" and labels[i]=="+":
            np+=1
        else:
            nn+=1
    accurancy=(pp+nn)/(pp+pn+np+nn)*100
    print("\n---------Confusion Matrix--------")
    print("  + -")
    print("+ "+ str(pp)+" "+str(pn))
    print("- "+ str(np)+ " "+str(nn))
    print("Accurancy: "+str(int(accurancy))+"%")        

def visual(traindata,testdata):
    t=turtle.Turtle()
    style = ('Arial', 10, 'italic')
    t.pendown()
    t.pencolor("black")
    t.pensize(5)
    t.forward(400)
    t.write('X', font=style, align='center')
    t.setpos(0,0)
    t.left(90)
    t.forward(300)
    t.write('Y', font=style, align='center')
    t.penup()
    
    for data in traindata:
        t.setpos(data.x1*20,data.x2*20)
        if data.label=='+':
            t.pencolor("Red")
        else:
            t.pencolor("Blue")
        t.write(data.label, font=style, align='center')
    t.pencolor("Green")
    for data in testdata:
        t.setpos(data.x1*20,data.x2*20)
        t.write('?', font=style, align='center')
    turtle.done()

def swapPositions(list, pos1, pos2):
     
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

trainingdata= list()
f = open("trainData.txt","r")
for x in f:
    sample = x.split("\n")[0].split("\t")
    # print(sample)
    temp=Sample(int(sample[0]),int(sample[1]),sample[2])
    trainingdata.append(temp)

for i in range(len(trainingdata)):
    trainingdata=swapPositions(trainingdata,i,randint(0,len(trainingdata)-1))

p=80
k=5
testingdata=trainingdata[int(len(trainingdata)*p/100):]
trainingdata=trainingdata[:int(len(trainingdata)-len(testingdata))]

# print(len(testingdata))
# print(len(trainingdata))
predictedlabels=list()
for i in testingdata:
    predicted=getlabel(i,trainingdata,k)
    predictedlabels.append(predicted)
    print("x1: "+str(i.x1)+" x2: "+str(i.x2)+"\tLabel: "+str(predicted))
    # print("label: "+str(predicted))
print(confusionmatrix(testingdata,predictedlabels))
visual(trainingdata,testingdata)