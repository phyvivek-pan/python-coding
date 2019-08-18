command=""
while True:
	command=input("-").lower()
	if command =="start":
		print("start the car...")
	elif command =="stop":
		print("stop the car...")
	elif command== "help":
		print("""
start--start the car
stop--stop thecar
quit--quit""")
	elif command == "quit":
		break
	else:
		print("not understand")
