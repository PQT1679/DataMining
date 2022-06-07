import turtle


class Sample:
    def __init__(self, f1, f2, f3, label):
        self.f1 = f1
        self.f2 = f2
        self.f3 = f3
        self.label = label

def load_traindata():
    trainingdata= list()
    f = open("trainData.txt","r")
    for x in f:
        sample = x.split("\n")[0].split("   ")
        temp=Sample(int(sample[0]),int(sample[1]),int(sample[2]),sample[3])
        trainingdata.append(temp)
    return trainingdata

def load_testdata():
    testdata= list()
    f = open("testData.txt","r")
    for x in f:
        sample = x.split("\n")[0].split("   ")
        temp=Sample(int(sample[0]),int(sample[1]),int(sample[2]),"")
        testdata.append(temp)
    return testdata


def get_label(traindata,testdata):
    count={
        "f1":{"+":0,"-":0},
        "f2":{"+":0,"-":0},
        "f3":{"+":0,"-":0},
        "+":0,
        "-":0
    }
    for i in traindata:
        if(i.f1==testdata.f1):
            if i.label =="+":
                count["f1"]["+"]+=1
            else:
                count["f1"]["-"]+=1
        if(i.f2==testdata.f2):
            if i.label =="+":
                count["f2"]["+"]+=1
            else:
                count["f2"]["-"]+=1
        if(i.f3==testdata.f3):
            if i.label =="+":
                count["f3"]["+"]+=1
            else:
                count["f3"]["-"]+=1
        if i.label == "+":
            count["+"]+=1
        else:
            count["-"]+=1
    # print(count)    
    py=(count["f1"]["+"]/count["+"])*(count["f2"]["+"]/count["+"])*(count["f3"]["+"]/count["+"])*(count["+"]/len(traindata))
    pn=(count["f1"]["-"]/count["-"])*(count["f2"]["-"]/count["-"])*(count["f3"]["-"]/count["-"])*(count["-"]/len(traindata))
    # print(py)
    # print(pn)
    if(py>pn):
        return "+"
    return "-"


traindata=list()
traindata=load_traindata()
testdata = load_testdata()
for testsample in testdata:
    print("Feature 1: "+str(testsample.f1)+"\tFeature 2: "+str(testsample.f2)+"\tFeature 3: "+str(testsample.f3)+"\tPredicted Label: "+get_label(traindata,testsample)+"\n")