import math
from random import randint
import turtle


class Sample:
    def __init__(self, x1, x2,label):
        self.x1 = x1
        self.x2 = x2
        self.label = label


#dự đoán nhãn bằng knn
def getlabel(test,trainingdata,k):
    d=list()
    for t in trainingdata:
        label=t.label
        d1=math.sqrt(pow(test.x1-t.x1,2)+pow(test.x2-t.x2,2))
        d.append((d1,label))
    d.sort()
    # print(d)
    ca=0
    cb=0
    for i in range(k):
        if d[i][1]=="+":
            ca+=1
        else: cb+=1
    if ca >cb:
        return "+"
    return "-"

#ma trận lỗi
def confusionmatrix(testingdata,labels):        #testing=((3,4,"+"),(3,5,"-"),(5,4,"+"))    #predict=("+","-","-")
    pp=0    #plus plus ++
    pn=0    #+ -
    np=0    #- +
    nn=0    #- -
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


#trực quan dữ liệu
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


#hàm để đổi vị trí các phần tử- dùng để trộn tập huấn luyện
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


#trộn dữ liệu huấn luyện
for i in range(len(trainingdata)):
    trainingdata=swapPositions(trainingdata,i,randint(0,len(trainingdata)-1))

p=80
k=5

#lấy 4 mẫu(20%) từ tập huấn luyện và cập nhật lại tập huấn luyện
testingdata=trainingdata[int(len(trainingdata)*p/100):] #16:19
trainingdata=trainingdata[:int(len(trainingdata)-len(testingdata))] #0:15

# print(len(testingdata))
# print(len(trainingdata))

#lưu nhãn dự đoán
predictedlabels=list()  #lưu nhãn dự đoán->tí so snash với nhãn thực để vẽ confusion matrix
for i in testingdata:
    predicted=getlabel(i,trainingdata,k)
    predictedlabels.append(predicted)
    print("x1: "+str(i.x1)+" x2: "+str(i.x2)+"\tLabel: "+str(predicted))
    # print("label: "+str(predicted))
print(confusionmatrix(testingdata,predictedlabels))
visual(trainingdata,testingdata)