def merge(arr, low, temp, high):
	inv_count=0
	if low<high:
		mid=(low+high)//2
		inv_count+=merge(arr, low, temp, mid)
		inv_count+=merge(arr, mid+1, temp, high)
		inv_count+=mergeAndCount(arr, low, mid+1, high, temp)

	return inv_count

def mergeAndCount(arr, low, mid, high, temp):

	i = low
	j = mid+1
	k = low
	inv_count=0

	while i<=mid and j<=high:

		if(arr[i]>arr[j]):
			temp[k]=arr[j]
			inv_count+=(mid-i+1)
			k+=1
			j+=1
		else:
			temp[k]=arr[i]
			k+=1
			i+=1

	while i<=mid:
		temp[k]=arr[i]
		k+=1
		i+=1

	while j<=high:
		temp[k]=arr[j]
		k+=1
		j+=1

	for i in range(low, high+1):
		arr[i]=temp[i]

	return inv_count

if __name__ == '__main__':
	arr=[1,2,6,4,5]
	n=len(arr)
	temp=[None]*10
	count=merge(arr, 0, temp, n-1)
	print(count)

