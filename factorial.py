#Factorial 
#Name-Kanav Gupta
#Division-M
#Roll no-25
f=1                                  #f is initialised to 1
n=int(input("enter a number:"))
if n<0:
 print("enter positive")
elif n==0 or n==1:
 print('1')
else:
 while n>1:                          #starting of loop
  f=f*n                              
  n=n-1                             #the value of n is decreasing by 1
 print(f)
