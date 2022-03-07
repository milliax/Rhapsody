import random

def inpu():
    text = input('Press any key to continue.\nPress Q to quit.\n')
    return text

def exam(i):
    j = 0
    while j<i:
        n = str(random.randint(1, 9))
        j+=1
        if n not in lis:
            lis.append(n)
        else:
            j-=1
    return ''.join(lis)

def guess():
    n = input('Enter the number you guess <3.\n(or press Q to quit)\n')
    return n

def check(ans):
    global A, B
    t = 0
    chlis = []
    for i in ans:
        if i not in chlis:
            if i in lis:
                if t == lis.index(i):
                    A+=1
                else:
                    B+=1
        t+=1
        chlis.append(i)
    

t = 4
lis = []

text = input('Press S to start.\n')
ex = exam(t)

while text == 's' or text == 'S': 
    A = 0
    B = 0
    ans = guess()
    check(ans)
    print(f'{A}A{B}B')
    if ans == 'q'or ans == 'Q':
        break
    
    
        
        
