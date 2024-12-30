k = 17
n = 4

A=[0,1,1,1,1,2,2,2,2,3,3,3,3,0,0,0,0]

ones_start = A.index(1) 
twos_start = A.index(2) 
threes_start = A.index(3)

result = set()

for i in range(n):
	result.add((ones_start+i,twos_start+i,threes_start+i))

print(result)