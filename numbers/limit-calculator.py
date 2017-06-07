from sympy import *

def limitcalc(fx, l):
  x = symbols('x')
  if l == 'oo':
      r = limit(fx, x, l)
  else:
      r = limit(fx, x, int(l))
  print(r)


def msg():
  inpt_1 = input("Give f(x): ")
  inpt_2 = input("Give limit ('oo' for infinite): ")
  limitcalc(inpt_1,inpt_2)

msg()
