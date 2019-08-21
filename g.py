import random
print("Guess the number between 1 and 100")
#randomNumber=35
num=random.randint(1,100)
found=False
while not found:
	Guess = input("your Guess: ")
	i=int(Guess)
	if i  == num:
		print("you got it")
		found=True
	elif i < num :
		print("Guess higher")

	else:	
		print("Guess lower")




