import random
n = int(input())
m = int(input())

def get_me_randoms(a):
	arr = []
	for j in range(0,a):
		arr.append(random.randint(1,m))
	return arr

out_array = []
for i in range(0,n):
	out_array.append(get_me_randoms(i+1))

p = random.randint(1,25)
print out_array

