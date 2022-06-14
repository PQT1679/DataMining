import math
import turtle

def load_traindata():
    trainingdata= list()
    f = open("trainData.txt","r")   #read

    for x in f: #từng dòng trong file       #\n: xuống dòng \t: tab 
        sample = x.split("\n")[0].split("   ")  #2   10\n         split("\n") "2   10","" [0]="2   10"   split("   ") sample[0]=2 sample[1]=10
        print(sample)
        temp=(int(sample[0]),int(sample[1]))
        trainingdata.append(temp)
    return trainingdata

#Khởi tạo tâm
def initcenters(traindata,k):
    centers=list()
    for i in range(0,k):
        centers.append(traindata[i])
    return centers

#Cập nhật lại tâm
def updatecenters(arr):
    x=0
    y=0
    for i in arr:       #x=(2+5+4)/3=3.66666     y=(10+8+9)/3=9.000000
        x+=i[0]
        y+=i[1]
    return [x/len(arr),y/len(arr)]
data=load_traindata()

def getDistance(a,b):
    return math.sqrt((a[0]-b[0])*(a[0]-b[0])+(a[1]-b[1])*(a[1]-b[1]))

# trực quan dữ liệu bằng thư viện Turtle
def visualization(data,centers):
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
    color=("blue","red","green")        #color[0]="blue"    color[1]="red" color[2]="red"
    i=0
    for cluster in data:        
        t.pencolor(color[i])    #ban đầu -> color[0]
        t.pensize(5)
        for item in cluster:
            t.setpos(item[0]*20,item[1]*20)
            t.dot() 
        t.pensize(10)
        t.setpos(centers[i][0]*20,centers[i][1]*20)
        t.dot()           
        i+=1
    turtle.done()


# phân cụm
def clustering(data,k):
    centers=initcenters(data,k)
    clusters=list()
    stop=False
    while(not stop):
        print("---centers----")
        print(centers)
        print("-------\n")
        cluster1=list()
        cluster2=list()
        cluster3=list()
        for i in data:      #duyệt qua từng phần từ trong tập dữ liệu
            d1=getDistance(i,centers[0])
            d2=getDistance(i,centers[1])
            d3=getDistance(i,centers[2])
            print("("+str(i[0])+","+str(i[1])+")\t:   "+str(d1)+"\t"+str(d2)+"\t"+str(d3))
            if(d1<d2 and d1<d3):        #d nhỏ nhất
                cluster1.append(i)
            elif d2<d1 and d2<d3:
                cluster2.append(i)
            else:
                cluster3.append(i)
        if centers[0]==updatecenters(cluster1) and centers[1]==updatecenters(cluster2) and centers[2]==updatecenters(cluster3):
            clusters.append(cluster1)
            clusters.append(cluster2)
            clusters.append(cluster3)
            stop=True
        print("-----clusters------")
        print(cluster1)
        print(cluster2)
        print(cluster3)
        print("-----------")
        centers[0]=updatecenters(cluster1)
        centers[1]=updatecenters(cluster2)
        centers[2]=updatecenters(cluster3)
        
    return clusters,centers

traindata=load_traindata()
result,centers=clustering(traindata,3)
print("Cum 1: "+str(result[0])+"\tCenter: "+str(centers[0]))
print("Cum 2: "+str(result[1])+"\tCenter: "+str(centers[1]))
print("Cum 3: "+str(result[2])+"\tCenter: "+str(centers[2]))
visualization(result,centers)

