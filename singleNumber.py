# Problem Statement:

# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]

# Output: 1

# Logic: Use XOR
# https://leetcode.com/problems/single-number/submissions/

def getOddOccurence(arr):
	ans=0
	for i in arr:
		ans = ans^i
	return ans

if __name__ == '__main__':
	arr = [2,3,5,4,5,2,4,3,5,2,4,4,2]
	print(getOddOccurence(arr))
