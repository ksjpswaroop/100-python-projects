
def colalg(n,step):
  if n < 0:
      return 0
  elif n == 1:
      return sum(step)
  elif n % 2 == 0:
      step.append(1)
      return colalg(n/2,step)
  else:
      step.append(1)
      return colalg(n * 3 + 1,step)




inpt = input("Number: ")
step = [1]
print(colalg(int(inpt),step))
