Problem Statement #
Given an array of characters where each character represents a fruit tree, you are given two baskets, and your goal is to put maximum number of fruits in each basket. The only restriction is that each basket can have only one type of fruit.

You can start with any tree, but you can’t skip a tree once you have started. You will pick one fruit from each tree until you cannot, i.e., you will stop when you have to pick from a third fruit type.

Write a function to return the maximum number of fruits in both the baskets.

Example 1:

Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']


def fruits_into_baskets(fruits):
  start=0
  maxLen=0
  charFreq={}
  for end in range(len(fruits)):
    rightFruit=fruits[end]
    if rightFruit not in charFreq:
      charFreq[rightFruit]=0
    charFreq[rightFruit]+=1
    print(charFreq)
    while len(charFreq)>2:
      leftFruit=fruits[start]
      charFreq[leftFruit]-=1

      if charFreq[leftFruit]==0:
        del charFreq[leftFruit]
      start+=1
    maxLen = max(maxLen, end-start+1)
  return maxLen



def main():
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'A', 'C'])))
  print("Maximum number of fruits: " + str(fruits_into_baskets(['A', 'B', 'C', 'B', 'B', 'C'])))


main()