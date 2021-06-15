def bubbleSort(arr):
	n=len(arr)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j+1]<arr[j]:
				arr[j+1], arr[j] = arr[j],arr[j+1]
				
	return arr

A=[5,3,4,2,1]

print(bubbleSort(A))

#i=1, j=0, 3<5, 