import random
import time
#import msvcrt
import decimal

try:
    times1=int(input("请输入想掷骰子的次数（0=一直骰）"))
except:
    print("这是数字？？默认为0")
    times1=0
    time.sleep(1)
cdef int times=times1
cdef int shape=0
cdef int zheng=0
cdef int fan=0
cdef int true1=0
if times > 0:
    while times > 0:
        cdef int shape=random.randint(0,1)
        if shape == 1:
            zheng=zheng+1
        else:
            fan=fan+1
        times=times-1
        true1=true1+1
        print("正面:"+str(zheng)+",反面:"+str(fan)+",总次数:"+str(true1)+"频数:"+str(decimal.Decimal(zheng)/ decimal.Decimal(true1)))
#    print("请按任意键退出~")
#    ord(msvcrt.getch())
else:
    while True:
        cdef int shape=random.randint(0,1)
        if shape == 1:
            zheng=zheng+1
        else:
            fan=fan+1
        times=times-1
        true1=true1+1
        if true1%100000 == 0:
            #print(true1)
            print("正面:"+str(zheng)+",反面:"+str(fan)+",总次数:"+str(true1)+"频数:"+str(decimal.Decimal(zheng)/ decimal.Decimal(true1)))
