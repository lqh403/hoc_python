
# dic = []
# n = int(input( ' n = '))
# while n <= 0 :
# 	print('Nhap lai' , end = '')
# 	n = int(input(' n = '))

# for i in range(i, n+1):
# 	dic()


# print(dic)
# print()

d = []
lst1 = []
lst2 = []

n = int(input('Nhap cac phan tu cho cac list '))
 while n <= 0:
	print('Nhap lai' , end = '')
		n = int(input())
print('Nhap cac gia tri cho list 1')
# for i in range(n):
# 	so = int(input(' so = ')
# 	lst1.append(so)
# key1 = tuple(lst1)
# print(key1)





def kiemtrachan(n):
    """Kiểm tra xem một số có phải là số chan hay không"""
    if n <%2 =0
    n False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True






def find_primes(lst):
    """Tìm tất cả các số nguyên tố trong một dãy số"""
    primes = []
    for num in lst:
        if is_prime(num):
            primes.append(num)
    return primes