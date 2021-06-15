def insertionSort(arr):
	n = len(arr)

	for i in range(1, n):
		key=arr[i]
		j=i-1

		while j>=0 and key<arr[j]:
			arr[j+1]=arr[j]
			j-=1
			arr[j+1]=key

	return arr




A=[12, 11, 13, 5, 6]
print(insertionSort(A))

#i=1, j=0 11, 12, 13, 5, 6, key=11
#i=2, j=1 11, 12, 13, 5, 6, key=
#i=3, j=2 key=5

