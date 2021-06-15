# Problem Statement:

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1:

# Input: [1,2,3,4,5,6,7] and k = 3

# Output: [5,6,7,1,2,3,4]

# Logic: 3 reversals required - 1st 0 to n-k-1, 2nd n-k to n-1, 3rd 0 to n-1

# https://leetcode.com/problems/rotate-array/solution/


def reverse(arr, a, b):
	while(a<=b):
		temp=arr[a]
		arr[a]=arr[b]
		arr[b]=temp
		a+=1
		b-=1

def rotateKTimes(arr, n, k):
	reverse(arr, n-k, n-1)
	reverse(arr, 0, n-k-1)
	reverse(arr, 0, n-1)
	print(arr)

if __name__ == '__main__':
	arr = [1,2,3,4,5,6,7]
	rotateKTimes(arr, len(arr), 3)