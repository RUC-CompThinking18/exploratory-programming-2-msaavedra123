def positive(sequence):
	if type(sequence) != list:
		raise TypeError("Not a list")	#Will print error message if input is not a list
	count = 0							#Variable will be used to keep track of positive numbers
	for i in range(len(sequence)):
		if sequence[i] > 0:				#If number is greater than 0, will add 1 to count
			count += 1
	print count

y = [3, -5, 0, -5, -6, -3, 2, -6, 8, -9, -3, -1, -5]    #3 Positive numbers
positive(y)
positive('[-1, -2, 4]') 		#String, should print type error message
#Please work
