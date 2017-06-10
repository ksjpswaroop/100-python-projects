
def colalg(n,step):
  if n < 0:
      return 0
  elif n == 1:
      return step
  elif n % 2 == 0:
      step+=1
      return colalg(n/2,step)
  else:
      step+=1
      return colalg(n * 3 + 1,step)




inpt = input("Number: ")
step = 0
print(colalg(int(inpt),step))
