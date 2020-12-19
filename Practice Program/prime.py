no = 1007

# any prime no greater than 2 is odd
# 
def prime(no):
    for i in range(2,no+1):
        if no%i==0:
            print("no is not prime")
            break
        else:
            print("no is prime")
            break
    return 
            
prime(no)
            
                
        
    
    
    
