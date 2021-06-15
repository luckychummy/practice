import sys
def leaderArray(arr,n):
	max_value=-sys.maxsize -1
	for i in range(n-1,-1,-1):
		if max_value<arr[i]:
			max_value = arr[i]
			print(max_value)

if __name__ == '__main__':
	arr=[10,6,3,1,7,9,3]
	n=len(arr)
	print(leaderArray(arr,n))