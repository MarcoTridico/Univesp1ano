a = 0
b = 1
c = 0
i = 1

def calcFibo(num):
    global a
    global b
    global c
    global i
    if i != num:
        c = a + b
        a = b
        b = c
        i = i + 1
        calcFibo(num)
    else:
        print(c)

calcFibo(12)
    
