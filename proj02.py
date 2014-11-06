print("Guess a solution for one of the following puzzles")
print("Puzzle #1 SLAYER + SLAYER + SLAYER = LAYER")
print("Puzzle #2 PEEP = P**E")

usr_inpt = input("Enter the number of a puzzle:  ")

if int(usr_inpt) == 1:
	slayer_int = int(input("Enter your guess for SLAYER:   "))
	if len(str(slayer_int)) == 6:
		slayer_list = [i for i in str(slayer_int)]
		layers_list = []
		layers_list.append(slayer_list.pop(0))
		slayer_list.extend(layers_list)
		
		if int("".join(map(str,slayer_list))) == slayer_int*3:
			print("Your guess is correct!")
		else:
			print("Your guess is incorrect")
	else:
		print("Number is not the correct length")
	
elif int(usr_inpt) == 2:
	peep_int = int(input("Enter your guess for PEEP:  "))
	if len(str(peep_int)) == 4:
		p = (peep_int//1000)%10
		e = (peep_int//100)%10
		if p*e*e*p == p**e:
			print("Your guess is correct!")
		else:
			print("Your guess is incorrect!")
			
	else:
		print("Number is not the correct length")
		
else:
	print("That is not a valid input")
	
print("Thanks for playing")