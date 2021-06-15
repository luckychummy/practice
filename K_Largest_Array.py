
import random
def quickSort(arr, low, high):
	if (low<high):

		pivotIndex = partitionRand(arr, low, high)

		quickSort(arr, low, pivotIndex-1)
		quickSort(arr, pivotIndex+1, high)

# This function generates random pivot, swaps the first 
# element with the pivot and calls the partition fucntion. 
def partitionRand(arr, low, high):

	# Generating a random number between the  
    # starting index of the array and the 
    # ending index of the array. 
	randPivot = random.randrange(low, high)

	# Swapping the starting element of the array and the pivot
	arr[low],arr[randPivot] = arr[randPivot], arr[low]

	return partition(arr, low, high)

''' 
This function takes the first element as pivot,  
places the pivot element at the correct position  
in the sorted array. All the elements are re-arranged  
according to the pivot, the elements smaller than the 
pivot is places on the left and the elements 
greater than the pivot is placed to the right of pivot. 
'''
def partition(arr, low, high):
	pivot=low
	i=low+1 # a variable to memorize where the partition in the array starts from.

	for j in range(low+1, high+1):
		
		if arr[j]<=arr[pivot]:
			arr[i],arr[j]=arr[j],arr[i]
			i+=1

	arr[pivot],arr[i-1]=arr[i-1],arr[pivot]
	pivot=i-1

	return pivot

a=[23, 2, 11, 51, 13]
quickSort(a, 0, 4)
print(a)
