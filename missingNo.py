#Logic:Take the XOR of all elements from 1 to N(2, N+2) if we start from 1st element as 1 till n+1 (inclusive)
#Take the XOR of all elements in the array
#Take the XOR of both the values obtained.

def findMissingNum(a, n):
	x1 = a[0];
	x2 = 1;

	for i in range(1,n):  
		x1=x1^a[i];
	print(x1)

	for i in range(2, n+2):
		x2=x2^i;
	print(x2)

	return x1^x2;

if __name__ == '__main__':
	l=[1,5,3,4,6]
	n=len(l);
	miss = findMissingNum(l,n);
	print(miss)

