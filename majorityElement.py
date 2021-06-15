# Problem Statement:

# Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

# You may assume that the array is non-empty and the majority element always exist in the array.

# Example 1:

# Input: [3,2,3]

# Output: 3

# Logic : Find element with max count and then check count to be greate than half of the size.

# https://leetcode.com/problems/majority-element-ii/submissions/

def findMajority(arr, n):
	m_element=0;
	count=1;
	for i in range(n):
		if(arr[i]==m_element):
			count+=1;
		else:
			count-=1;
		if(count==0):
			m_element=arr[i];
			count+=1;
	return m_element

def isMajority(arr, n, m_element):
	count=0;
	for i in range(n):
		if(arr[i]==m_element):
			count+=1;
	if count>n/2:
		return True;
	else:
		return False;

if __name__ == '__main__':
	arr=[3,3,4,4,4,2,4,2,4,4];
	value=findMajority(arr, len(arr));
	if(isMajority(arr, len(arr), value)):
		print(value)
	else:
		print("No majority element found")