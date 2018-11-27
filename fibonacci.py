#Fibonnaci series
#Name-Kanav Gupta
#Division-M
#Roll no-25
n=int(input("enter a number:"))
a=0                                   #a is first element of fibonnaci series
b=1                                   #b is second element of fibonacci series
l=[]                                  #list is defined
if n<0:
 print("enter positive")
elif n==0:
 print('0')
elif n==1:
 print('0,1')
else:
 l.append(a)                          #put the value of a in list
 l.append(b)                          #put the value of b in list
for i in range(n-2):
 f=a+b                                #next value will always be the sum of previous two values
 l.append(f)
 a=b
 b=f
print(l)
