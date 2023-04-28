# age = 16
# if age < 10:
# 	print("con nít")
# elif age < 18:
# 	print("trẻ trâu")
# 	if age >= 15 and age <= 17:
# 		print("siêu trẻ trâu")
# else:
# 	print('người lớn')	
from random import randint
print("Mời bạn nhập:")
player = input()
computer = randint(0,2)

if computer == 0:
	computer = "Dam"
if computer	== 1:
	computer = "La"	
if computer == 2:
	computer = "Keo"

print("---")
print("You choose: "+ player)
print("Computer choose: " + computer)
print("---")
if player == computer:
	print("Draw")
else:
	if player == "Keo":
		if computer == "Dam":
			print("Lose")	
		else:
			print("Win")	

	elif player == "Dam":
		if computer == "Keo":
			print("Win")
		else:
			print("Lose")	
			
	elif player == "La":
		if computer == "Keo":
			print("Lose")
		else:
			print("Win")	
	else:
		print("Nhap sai")	
		