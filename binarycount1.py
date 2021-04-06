import math
import os
import random
import re
import sys
if __name__ == '__main__':
    n =55
    x =''
    count1 =0
    count =0

    while n != 1:
        x= x+str(n % 2)
        n = n // 2
    x = list('1' + x[::-1]+'0')
    for i in range(len(x)):
        if x[i] =='1':
            count+=1
        elif x[i]!='1':
            if count>count1:
                count1=count
                count = 0
    print(count1)
    print(x)




        # elif count1>count:
        #     count = count1
