import gmpy2
import math

def primes():
    n = 2
    while True:
        yield n
        n = gmpy2.next_prime(n)

def help_func(n):
    counter = 0
    arr = []
    for k in primes():
        # print(k)
        if n % k == 0 and k % 2 == 1:
            counter+=1
            arr.append(k)
        if counter > 4:
            break
    if counter == 4:
        print(str(arr) + " ", end='')
        return True
    else:
        return False


for i in range(35000000, 40000001):
    if help_func(i):
        print(i)

# for i in primes():
#     print(i)
#     if i > 100:
#         break