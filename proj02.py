print("Guess a solution for one of the following puzzles")
print("Puzzle #1 SLAYER + SLAYER + SLAYER = LAYER")
print("Puzzle #2 PEEP = P**E")

usr_inpt = input("Enter the number of a puzzle:  ")

if int(usr_inpt) == 1:
	slayer_int = int(input("Enter your guess for SLAYER:   "))
	if len(str(slayer_int)) == 6:
		pass#Code here for finding whether SLAYER value equals LAYERS
	else:
		print("Number is not the correct length")
	
elif int(usr_inpt) == 2:
	peep_int = int(input("Enter your guess for PEEP:  "))
	if len(str(peep_int)) == 4:
		pass#Code here for finding whether PEEP equals P**EOFError
	else:
		print("Number is not the correct length")
		
else:
	print("That is not a valid input")
	
print("Thanks for playing")