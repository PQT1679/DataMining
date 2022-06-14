import turtle
import math

def visualf(traindata,f1,f2):
    t=turtle.Turtle()
    turtle.speed(0)
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
        t.setpos(data[f1]*50,data[f2]*50)
        if(data[4]=="Iris-setosa"):
            t.pencolor("Red")
        elif data[4]=="Iris-versicolor":
            t.pencolor("Blue")
        else:
            t.pencolor("Green")
        t.dot()
    turtle.done()


#dự đoán nhãn bằng knn
def getlabel(test,trainingdata,k,f1,f2):        #f1,f2 là 2 thuộc tính ta chọn để phân lớp
    d=list()
    for t in trainingdata:
        label=t[4]
        d1=math.sqrt(pow(test[f1]-t[f1],2)+pow(test[f2]-t[f2],2))
        d.append((d1,label))
    d.sort()
    count = {
        "Iris-setosa": 0,
        "Iris-versicolor": 0,
        "Iris-virginica": 0
    }
    for i in range(k):
        count[d[i][1]]+=1
    return max(count, key=count.get)



#Trực quan từng cặp thuộc tính để chọn thuộc tính nổi trội -> chọn được thuộc tính nổi trội là thuộc tính 3 và 4 (2,3)
def visual(traindata):
    # visualf(traindata,0,1)
    # visualf(traindata,0,2)
    # visualf(traindata,0,3)
    # visualf(traindata,1,2)
    # visualf(traindata,1,3)
    visualf(traindata,2,3)

trainingdata= list()
f = open("iris.data","r")
for x in f:
    sample= x.split("\n")[0].split(",")
    trainingdata.append((float(sample[0]),float(sample[1]),float(sample[2]),float(sample[3]),sample[4]))

testingdata= list()
f = open("iris_testdata.data","r")
for x in f:
    sample= x.split("\n")[0].split(",")
    testingdata.append((float(sample[0]),float(sample[1]),float(sample[2]),float(sample[3])))


#chọn số K láng giềng gần nhất
k=5
print("Feature 1    |    Feature 2   |    Feature 3   |    Feature 4   |    Predicted Label")
for t in testingdata:
    print("  "+str(t[0])+"\t     |      "+str(t[1])+"\t      |   "+str(t[2])+"\t       |     "+str(t[3])+"\t|    "+str(getlabel(t,trainingdata,k,2,3)))

visual(trainingdata)
