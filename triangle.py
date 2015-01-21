
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

output_tr = input_tr
input_tr[0][0] = 12
print input_tr[0][0], output_tr[0][0]
		

