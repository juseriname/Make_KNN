import random
import numpy as np

r = [] #사과 0
b = [] #배 1
for i in range(50):
    #크기가 5~15 사이에 있고, 무게가 60~110 사이에 있으면 사과
    r.append([random.randint(5,15),random.randint(60,110)])
    #크기가 10~20 사이에 있고, 무게가 90~140 사이에 있으면 배
    b.append([random.randint(10,20),random.randint(90,140)])
    
#점a(new)와 점b(기존)의 거리
def distance(a,b):
    return np.sqrt(pow((a[0]-b[0]),2)+pow((a[1]-b[1]),2))

#knn알고리즘
def knn(x,y,k):
    result=[]
    cnt=0
    for i in range(len(y)):
        result.append([distance(x,y[i]),y[i][2]])
    result.sort() # 오른차순
    for i in range(k):
        if(result[i][1]==1):
            cnt+=1
    if(cnt > (k/2)):
        print("해당 데이터는 배")
    else:
        print("해당 데이터는 사과")
        
mean = np.mean(r+b, axis=0) #평균
std = np.std(r+b, axis=0) #표준편차
z = ((r+b - mean) / std).tolist() #z-점수 정규화
for i in range(50):
    z[i].append(0)
    z[i+50].append(1)

print("크기가 5~15 사이에 있고, 무게가 60~110 사이에 있으면 사과")
print("크기가 10~20 사이에 있고, 무게가 90~140 사이에 있으면 배")
print("분류할 데이터 입력.")
size = int(input("크기 : "))
weight = int(input("무게 : "))
num = int(input("k : ")) #이웃 개수

new=[]
new.append(size)
new.append(weight)
new = (new-mean)/std

knn(new, z, num)
