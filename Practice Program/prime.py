no = 1

# any prime no greater than 2 is odd
# naive approach
def prime(no):
    if no<=1:
        print("not prime")
    for i in range(2,no+1):
        if no%i==0:
            print("no is not prime")
            break
        else:
            print("no is prime")
            break
    return 
            
prime(no)
            
                
        
# optimized method

def prime_opt(n):
    if n<=1:
        return False
    elif n<=3:
        return True
    elif (n % 2 == 0 or n % 3 == 0) : 
        return False
    p = 5 
    # Instead of checking till n, we can check till √n
    # because a larger factor of n must be a multiple of a smaller factor that has been already checked.
    while(p * p <n):
        if (n % p == 0 or n % (p + 2) == 0) :
            return False
        p = p+6
    return True
        
# if we take the square root of number and check from 2 to sqrt(n) then return
import math
import time
def prime_no(no):
    if no<=1:
        return False
    elif no==2:
        return True
    elif no>2 and no%2==0:
        return False
    value = math.floor(math.sqrt(no))
    for i in range(3, value+1, 2):
        if no%i==0:
            return False
    return True

# Driver function 
t0 = time.time() 
c = 0 #for counting 
  
for n in range(1,100000): 
    x = prime_no(n) 
    c += x 
print("Total prime numbers in range :", c) 
  
t1 = time.time() 
print("Time required :", t1 - t0) 
    
