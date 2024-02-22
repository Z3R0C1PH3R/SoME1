import math

tn = 1000

def check_div(num, N):
    a = N//10 
    p = 10*a-N
    x = num//10
    y = num % 10
    t = x*p + y*a
    return t%N==0

b = 10000
primes=[]

for i in range(2, b):
    for j in range(2, i):
        if (i % j) == 0:
            break
    else:
        primes.append(i)

print(primes)

for i in primes:
    for j in range(tn):
        if check_div(j, i) != (j%i==0):
            print(j, i)
