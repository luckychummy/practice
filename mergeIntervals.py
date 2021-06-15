def mergeIntervals(intervals):
	intervals.sort(key=lambda x:x[0])
	stack=[]
	#print(intervals) [[1,3],[2,4],[4,7],[6,8]]

	n = len(intervals)
	stack.append(intervals[0])
	#print(stack) [1,3]


	for i in range(1,n):
		top = stack[-1]

		print(top,"top") #[1,3]

		print(intervals[i][0],"hi")
		print(intervals[i][1],"Jai ho")
		if(top[1]<=intervals[i][0]):
			print(intervals[i][0],"hi")
			stack.append(intervals[i])

		elif(top[1]<intervals[i][1]):
			top[1]=intervals[i][1]
			stack.pop()
			stack.append(top)
			print(top,"new top")

	for i in range(len(stack)):
		top=stack[-1]
		print(top[0],top[1])
		stack.pop()


if __name__ == '__main__':
	l= [[6,8],[1,3],[2,4],[4,7]]
	mergeIntervals(l)