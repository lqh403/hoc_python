#sdt 0974532173
from math import sqrt
print("Giải phương trình bậc 2 một ẩn:")
a=int(input("Mời nhập số a:"))
b=int(input("Mời nhập số b:"))
c=int(input("Mời nhập số c:"))
delta = b*b - 4*a*c

if a==0:
	if b==0:
		if c==0: 
			print("phương trình vô số nghiệm")
		else:
			print("phương trình vô nghiệm")
	else:
		print("phương trình có nghiệm x =" , -c/b)		
else:
	if (delta == 0):
		print("phương trình có nghiệm kép x1 = x2" , -b/2*a)
	elif delta	> 0:
		print("phương trình có nghiêm x1 =" , (-(b)+sqrt(delta))/(2*a))
		print("phương trình có nghiêm x2 =" , (-(b)-sqrt(delta))/(2*a))
	else:
		print("phương trình vô nghiệm")		


