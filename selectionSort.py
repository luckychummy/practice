
def selectionSort(arr):
	n=len(arr)
	for i in range(n):
		lowest=i
		for j in range(i+1, n):
			if arr[lowest]>arr[j]:
				lowest=j
		arr[i], arr[lowest]=arr[lowest],arr[i]
	return arr

A=[5,3,4,2,1]

print(selectionSort(A))