def find_averages_of_subarrays(k, arr):
	sum=0
	avg=[]
	start=0
	for end in range(len(arr)):
		sum+=arr[end]
		if end >=k-1:
			avg.append(sum/k)
			sum-=arr[start]
			start+=1
	return avg


def main():
  result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2])
  print("Averages of subarrays of size K: " + str(result))


main()