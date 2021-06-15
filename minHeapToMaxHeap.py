
class minMaxHeap

def minToMax(arr, n):
	for i in range(n-1, 0, -1):
		if arr[0]<arr[n-1]:
			arr[0],arr[n-1]=arr[n-1],arr[0]

































A=[1,3, 2, 6, 8, 4, 5]
m = minMaxHeap()
n= len(A)

print(minToMax(A, n))