guess_me = 7
start = 1
while True:
	if(start < guess_me):
		print("too low")
	if(start == guess_me):
		print("found it")
		break
	if(start > guess_me):
		print("oops")
		break
	start += 1	 