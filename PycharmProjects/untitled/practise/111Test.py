# -*- coding: UTF-8 -*-
import  PyQt5
li=[]
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if(i != k) and (i != j) and (j != k):
                # print(i,j,k)
                li.append(i+j+k)
print(len(li))
