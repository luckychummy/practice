def longest_substring_with_k_distinct(str, k):
  start=0
  charFreq={}
  maxLen=0
  for end in range(len(str)):
    rightChar=str[end]
    if rightChar not in charFreq:
      charFreq[rightChar]=0
    charFreq[rightChar]+=1
    print(charFreq)

    # shrink the sliding window, until we are left with 'k' distinct characters in the charFreq
    while len(charFreq) > k:
      leftChar=str[start]
      charFreq[leftChar]-=1
      if charFreq[leftChar]==0:
        del charFreq[leftChar]
      start+=1
      # remember the maximum length so far
    maxLen = max(maxLen, end-start+1)

  return maxLen


def main():
  print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 2)))
  #print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("araaci", 1)))
  #print("Length of the longest substr1ing: " + str(longest_substring_with_k_distinct("cbbebi", 3)))


main()