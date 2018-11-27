#Angstrom Number
#define a funtion named angs
#Name-Kanav Gupta
#Division-M
#Roll no-25
def angs(x):
 s=0                        #s is initialized to 0
 z=x                        #x is a number to be entered  
 while x>0:                 #starting of while loop
   y=x%10                   #give remainder
   s=y**3+s                 #now the cube of remainder is initialised to s
   x=x//10                  #give quotient
 print(s)
 if s==z:                  #value of is initialized to z                 
  print("is a angstrom number")
 else:
  print("is not an angstrom number")

