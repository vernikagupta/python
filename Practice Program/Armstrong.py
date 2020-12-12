number = 153
num1 = number
total = 0
while number!=0:
    rem = number % 10
    number = number//10
    total = total+(rem**3)

print("{} is Armstrong".format(num1)) if num1==total else print("Not Armstrong") 
