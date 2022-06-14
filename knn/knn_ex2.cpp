#include <iostream>
#include <fstream>
#include <cstdlib>
#include <string>
#include <vector>
#include <math.h>
#include <bits/stdc++.h>
using namespace std;

class Sample
{
public:
    int f1;
    string label;
    int f2;
    Sample(int feature1=-1,int feature2=-1,string classlabel=""){
        f1=feature1;
        f2=feature2;
        label=classlabel;
    }
};


// lớp để lưu khoảng cách và nhãn của mẫu để dễ so sánh
class Distance{
    public:
        double d;
        string label;
    bool operator < (const Distance& d2) const
    {
        return (d < d2.d);
    }
};


// đọc file đêỷ lấy dữ liệu huấn luyện
vector<Sample> getTrainData(){
ifstream MyFile("trainData_ex2_cpp.txt");
    string text;
    vector<Sample> traindata;
    while (getline(MyFile, text))
    {
        string temp;
        Sample tempsample;
        for (int i = 0; i < text.size(); i++)
        {
            if (text[i] >= '0' && text[i] <= '9')
            {
                temp = "";
                for (int j = i; j < text.size(); j++)
                {
                    if (text[j] >= '0' && text[j] <= '9')
                    {
                        temp += text[j];
                    }
                    else
                    {
                        i += (j - i);
                        break;
                    }
                }
                int num = atoi(temp.c_str());
                if (tempsample.f1 == -1)
                {
                    tempsample.f1 = num;
                }
                else
                {
                    tempsample.f2 = num;
                }
            }
        }
        tempsample.label = text[text.size() - 1];
        traindata.push_back(tempsample);
    }
    MyFile.close();
    return traindata;
}

// lấy dữ liệu kiểm thử
vector<Sample> getTestData(){
ifstream MyFile("testData_ex2_cpp.txt");
    string text;
    vector<Sample> testdata;
    while (getline(MyFile, text))
    {
        string temp;
        Sample tempsample;
        for (int i = 0; i < text.size(); i++)
        {
            if (text[i] >= '0' && text[i] <= '9')
            {
                temp = "";
                for (int j = i; j < text.size(); j++)
                {
                    if (text[j] >= '0' && text[j] <= '9')
                    {
                        temp += text[j];
                    }
                    else
                    {
                        i += (j - i);
                        break;
                    }
                }
                int num = atoi(temp.c_str());
                if (tempsample.f1 == -1)
                {
                    tempsample.f1 = num;
                }
                else
                {
                    tempsample.f2 = num;
                }
            }
        }
        tempsample.label = text[text.size() - 1];
        testdata.push_back(tempsample);
    }
    MyFile.close();
    return testdata;
}


// ma trận lỗi
double getConfusionmatrix(vector<Sample> testdata,vector<string> plabel){
    int pp=0,pm=0,mp=0,mm=0;
    for(int i=0;i<testdata.size();i++){
        // cout<<testdata[i].label<<"\t"<<plabel[i]<<endl;
        if(testdata[i].label=="+" && plabel[i]=="+") pp++;
        else if(testdata[i].label=="+" && plabel[i]=="-") pm++;
        else if(testdata[i].label=="-" && plabel[i]=="+") mp++;
        else mm++;
    }
    cout<<"     +    -\n";
    cout<<"+    "<<pp<<"    "<<pm<<endl;
    cout<<"-    "<<mp<<"    "<<mm<<endl;
    double accuracy=(double(pp+mm))/(pp+mm+pm+mp)*100;
    return accuracy;
}


// hàm dự đoán nhãn
string getLabel(vector<Sample> traindata,Sample t,int k){
    vector<Distance> d;
    Distance temp;
    for(int i =0; i<traindata.size();i++){
        temp.d=sqrt(pow((traindata[i].f1-t.f1),2)+pow((traindata[i].f2-t.f2),2));
        temp.label=traindata[i].label;
        d.push_back(temp);
    }
    sort(d.begin(),d.end());
    // for(int i = 0;i<d.size();i++){
    //     cout<<d[i].d<<" "<<d[i].label<<endl;
    // }
    int cp=0,cm=0;
    for(int i = 0;i<k;i++){
        if(d[i].label=="+") cp++;
        else cm++;
    }
    // cout<<"cp: "<<cp<<"cm: "<<cm<<endl;
    if (cp>cm) return "+";
    return "-";
}

int main(int argc, char const *argv[])
{
    vector<Sample> traindata=getTrainData();
    int k=5;
    vector<Sample> testdata=getTestData();
    vector<string> plabel;
    string temp;
    for(int i=0;i<testdata.size();i++){
        temp=getLabel(traindata,testdata[i],k);
        plabel.push_back(temp);
        cout<<"Feature 1: "<<testdata[i].f1<<"\tFeature 2: "<<testdata[i].f2<<"\tPredictedLabel: "<<temp<<endl;
    }
    cout<<"Acurancy: "<<getConfusionmatrix(testdata,plabel)<<"%";
    return 0;
}
