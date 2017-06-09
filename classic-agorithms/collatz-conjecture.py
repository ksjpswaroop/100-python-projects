
def colalg(n):
  step = [1]
  if n < 0:
      return 0
  elif n == 1:
      return sum(step)
  elif n % 2 == 0:
      step.append(1)
      return colalg(n/2)
  else:
      step.append(1)
      return colalg(n * 3)




inpt = input("Number: ")
print(colalg(int(inpt)))
