#define a funtion named angs
def angs(x):
 s=0                        #s is initialized to 0
 z=x                        #x is a number to be entered  
 while x>0:
   y=x%10
   s=y**3+s
   x=x//10
 print(s)
 if s==z:                 
  print("is a angstrom number")
 else:
  print("is not an angstrom number")

