
f = open('input_data.txt','r')

for line in f:
	inputed_data = line

print len(inputed_data)
just_numbers = []
for i in range(0, len(inputed_data)):
	if (inputed_data[i]=="[" or inputed_data[i]=="]" or inputed_data[i]==" "):
		#print inputed_data[i]
		continue
	else:
		just_numbers.append(inputed_data[i])

#def flush(b):
#	a = 0

def get_number(a, b):
	c = int(a) + 10*b
	return c
a =0
b = 0
out_array1 = []
for i in range(0, len(just_numbers)-1):
	if just_numbers[i]==",":
		if a!=0:
			out_array1.append(a)	
		a = 0
	else:
		a = get_number(just_numbers[i], a)
out_array1.append(a)	
#print out_array1

#n**2+n-2*len(out_array1)=0
height = int((-1+(1+8*len(out_array1))**0.5)/2)
#print height

input_tr = []
for i in range(1,height+1):
	input_tr.append(out_array1[i-1:(2*i-1)])
#print input_tr

#checking if a simple equality copies the data structure or just copies the pointer
output_tr1 = input_tr
#input_tr[0][0] = 12
#input_tr[0][0] - output_tr[0][0] <- this result is zero which impleies that only the pointer is copied.
def copy_array(array1):
	output_array1 = []
	for i in range(0, len(array1)):
		output_array1.append(array1[i])
	return output_array1
def copy_triangle(input_triangle):
	output_triangle = []
	for i in range(0,height):
		output_triangle.append(copy_array(input_triangle[i]))
	return output_triangle
output_tr = copy_triangle(input_tr)
#input_tr[0][0] = 12
#print output_tr, input_tr[0][0] - output_tr[0][0]

def gen_arr_trav(height):
	arr_trav = []
	for i in range(0,height):
		arr_trav.append(int(height-i-1))
	return arr_trav
arr_2_trav = gen_arr_trav(height)
#print arr_2_trav
for i in arr_2_trav:
	for j in range(0,i+1):
		if i==height-1:
			output_tr[i][j] = output_tr[i][j]
		else:
			#print i,j
			output_tr[i][j] = output_tr[i][j] + min(output_tr[i+1][j],output_tr[i+1][j+1])
#			print i,j

#print output_tr, "\n", input_tr
minima = []
indices = []
j=0
for i in range(0, height):
	minima.append(output_tr[i][j])
	indices.append(j)
	#count = i
	print [i,i+1]
	for j in [i,i+1]:
		if output_tr[i][j] < minima[i]:
			minima[i] = output_tr[i+1][j]
			indices[i] = j
		#count = count + 1

putput = []
for i in range(0, height):
	putput.append(input_tr[i][indices[i]])
print "\n", minima, indices, "\n", putput

//edit entry on 23jan15
def output_path():
	for i in range(0, height):
		

