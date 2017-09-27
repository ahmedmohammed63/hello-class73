from math import *
#just a test on github

def check_fermat (a,b,c,n):
 power_a= pow(a,n)
 power_b= pow(b,n)
 power_c= pow(c,n)

 if power_a + power_b == power_c:
     print ("Holy Smokes, Fermat was WRONG!")
 else:
     print("No buddy that doesn't work")



check_fermat(3,4,5,2)
check_fermat(3,4,5,3) 

def fermat_checker():
  a = int(input("enter value for 'a'"))
  b = int(input("enter value for 'b'"))
  c = int(input("enter value for 'c'"))
  n = int(input("enter value for 'n'"))
  
  check_fermat(a,b,c,n)

fermat_checker()

