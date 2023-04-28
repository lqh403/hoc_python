def is_prime(n):
    """Kiểm tra xem một số có phải là số nguyên tố hay không"""
    if n < 2:
        return False
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

# Sử dụng hàm find_primes để tìm tất cả các số nguyên tố trong một dãy số:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
print(find_primes(numbers))
 
print('anhdanchoi')


  # Kết quả: [2, 3, 5, 7]

    #kiểm tra chan lẻ

num = int(input("Nhập một số nguyên: "))

if num % 2 == 0:
    print(num, "là số chẵn")
else:
    print(num, "là số lẻ")



num = int(input("Nhập một số nguyên: "))

# chuyển đổi số thành chuỗi để đếm số ký tự
num_str = str(num)

# loại bỏ dấu trừ nếu có
if num_str[0] == "-":
    num_str = num_str[1:]

# đếm số chữ số
num_digits = len(num_str)

print("Số", num, "có", num_digits, "chữ số.")

\

num = int(input("Nhập một số nguyên: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "không phải là số nguyên tố")
            break
    else:
        print(num, "là số nguyên tố")
else:
    print(num, "không phải là số nguyên tố")



    # tính tổng
    n = int(input("Nhập n: "))
S = 0

for i in range(1, n+1):
    S += 1/i

print("Tổng S =", S)




