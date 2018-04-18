import numpy as np
import csv


#读取csv文件 并设置台湾编码big5
csv_reader = csv.reader(open('train.csv', encoding='big5'))
#此时cvs_reader的格式是object 每一行是一个list


#将object转换为二维list

file_list =[]
for row in csv_reader:
    file_list.append(row)
#获取文件行数
j= len(file_list)

#清洗数据 只考虑pm2.5
pm2_5 = []
for i in range(j):
    if(file_list[i][2]=="PM2.5"):
        pm2_5.append(file_list[i][3:])


#training data
traindataX = []
traindataY = []
for i in range(len(pm2_5)):

    for j in range(15):
        traindataX.append(pm2_5[i][j:j+9])

for i in range(len(pm2_5)):

    for j in range(15):
        traindataY.append(pm2_5[i][j+9])

x = np.array(traindataX,float)
y = np.array(traindataY,float)

# 在feature基础上加入bias
x = np.concatenate((np.ones((x.shape[0],1)),x),axis=1)

#初始化参数
learning = 10
w = np.zeros((len(x[0])))
sum2_grad=np.zeros(len(x[0]),float)
iteration=10000  #迭代10000次
for i in range(iteration):
    tem = np.dot(x,w)
    loss = y - tem

    grad = (-2)*np.dot(x.transpose(),loss)
    sum2_grad += grad**2
    ada = np.sqrt(sum2_grad)
    w = w - learning*grad/ada

#predict
