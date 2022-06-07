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
    ca=0
    cb=0
    for i in range(k):
        if d[i][1]==0:
            ca+=1
        else: cb+=1
    if ca >cb:
        return "+"
    return "-"

trainingdata= list()
f = open("trainData.txt","r")
for x in f:
    sample = x.split("\n")[0].split("\t")
    temp=Sample(int(sample[0]),int(sample[1]),sample[2])
    trainingdata.append(temp)

testdata= list()
f = open("testData.txt","r")
for x in f:
    sample = x.split("\n")[0].split("   ")
    print(sample)
    temp=Sample(int(sample[0]),int(sample[1]),"?")
    testdata.append(temp)

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

for t in testdata:
    print("x1: "+str(t.x1) +" x2: " +str(t.x2) +" Label: "+getlabel(t,trainingdata,5))
visual(trainingdata,testdata)