n = 25
d = 25
q = 25
o = 0
f = 0

usr_inpt = input("Please enter the price of the object in the from xx.xx:  ")

while usr_inpt != 'q':
	price = round(float(usr_inpt)*100)
	print("n = %d" % n)
	print("d = %d" % d)
	print("q = %d" % q)
	print("o = %d" % o)
	print("f = %d" % f)
	print(price/100)
	usr_inpt = input("Please enter the price of the object in the from xx.xx:  ")
else:
	print("bye")