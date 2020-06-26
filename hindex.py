def hindex(citationList): 
	citationList.sort(reverse=True)
	n= len(citationList)
	for i in range(1,n):
		if citationList[i]<i:
			print "Your H-index is %d" % (i-1)
			break

