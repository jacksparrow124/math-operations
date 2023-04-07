def test_prime(num): 
    maybe_prime = True
    
    for n in range(2, num-1):
        #print ('calculating prime for %i with number %i'% (num, n) )
        f = num / n
        i = int(f)
        #print ('i = %i'% f)
        if f == i:
           # print ('f = %i'% f)
            maybe_prime = False
            
    return maybe_prime
    
primes = 1 
n = 2
while primes <= 60:
    if test_prime(n):
        print ('%i - %i' % (primes, n))
        primes += 1
    n += 1
    
