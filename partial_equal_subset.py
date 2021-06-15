def getSplitPoint(arr, n):
	leftSum=0
	for i in range(n):
		leftSum=leftSum+arr[i]

	rightSum=0

	for i in range(n-1,-1,-1):
		rightSum+=arr[i]
		leftSum-=arr[i]
		if leftSum==rightSum:
			return i
	return -1

if __name__ == '__main__':
 	arr=[1,2,3,4,5,5]
 	point = getSplitPoint(arr, len(arr))
 	if(point==-1 or point==len(arr)):
 		print("split cannot be done") 
 	else:
 		for i in range(len(arr)):
 			if i==point:
 				print("\n")
 			print(arr[i])