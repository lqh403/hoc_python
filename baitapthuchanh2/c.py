
# nhap so phan tu list n =
#  nhap list
# kiem tra trong list



n = int(input(' n = '))

while n <= 0 :
	print('Nhap lai' , end = '')
	n = int(input(' n = '))

	# nhap vao list cac so thuc
	# cach 1: append


lst = []
for i in range(n) :
	so = float(input('so = '))
	lst.append(so)
print('list vua nhap la')	
print(lst)

		
		# cach 2: list(map)
	# lst1 = list(map(float, input('moi nhap gia tri: so = ').split()))
	# print(' list vua nhap la')
	# print(list1)


dd=0

for i in lst :
	if i > 0 :
		dd+=1 
print('so cac so duong trong list la ', dd)		
 

tongduong=0
for i in lst :
	if i > 0 :
		tongduong = tongduong + i
print(' tong cac so duong trong list la', tongduong)		

# tinh trung binh cong duong

if dd > 0 :
	print('trung binh cong so duong = ', tongduong/dd)	
else:
	print('khong co so duong trong list')	





	# dem so am trong list

da=0

for i in lst :
	if i < 0 :
		da+=1 
print('so cac so am trong list la ', da)


		# sap xep tang dan so am
for i in range(len(lst)-1):
	for j in range(i+1, len(lst)):
		if lst[i] < 0 and lst[j] < 0 and lst[i]	> lst[j]:
			lst[i],lst[j] = lst[j],lst[i]
print(' so am trong list')
print(lst)










