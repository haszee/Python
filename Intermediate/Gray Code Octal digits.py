def Octal(n,output):
	if n == 0:
		print(output)

	for i in range(8):
		Octal(n-1,str(i)+output)



Octal(2,"")