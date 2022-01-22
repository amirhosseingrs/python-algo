#get two numbers and print all the prime numbers between them including themselves
#question link : https://quera.ir/problemset/293/



x = int(input())
y = int(input())
i = x
primes = []
while i <= y : 
    isPrime = True
    for x in range(2,i):
        if i%x == 0 : 
            isPrime = False 
    if i == 1 : isPrime = False
    if isPrime == True : primes.append(i)
    i += 1
[print(x) for x in primes]    