from sympy import *

def limit(fx, l):
  x = symbols('x')
  r = limit((fx),x,l)
  print(r)



def msg():
  inpt_1 = input("Give f(x): ")
  inpt_2 = input("Give limit: ")
  limit(inpt_1,inpt_2)

msg()
