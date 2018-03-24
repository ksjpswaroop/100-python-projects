for x in range(1,101):
	res = ''
	if not x % 3:
		res += 'fizz'
	if not x % 5:
		res += 'buzz'
	if not res:
		res = x
	print(res)
