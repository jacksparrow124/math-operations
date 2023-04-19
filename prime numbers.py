def test_prime(num): 
    maybe_prime = True
    
    for n in range(2, num-1):
        
        f = num / n
        i = int(f)
        
        if f == i:
           
            maybe_prime = False
            
    return maybe_prime
    
primes = 1 
n = 2
while primes <= 60:
    if test_prime(n):
        print ('%i - %i' % (primes, n))
        primes += 1
    n += 1
    
