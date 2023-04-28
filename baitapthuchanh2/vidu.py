# # Trong code này, nhập vào một số
# # Kiểm tra xem số âm hay dương
# # hay bằng không và hiển thị
# # thông báo thích hợp
# # Sử dụng hàm if lồng nhau
# # num = float(input("Nhập một số: "))

# # if num >= 0:
# #    if num == 0:
# #        print("Số Không")
# #    else:
# #        print("Số dương")
# # else:
# #    print("Số âm")


# # n = int(input("Nhập n: ")) #Nhập số n tùy ý
# # tong = 0 #khai báo và gán giá trị cho tong
# # i = 1 #khai báo và gán giá trị cho biến đếm i
# # while i <= n:
# #     tong = tong + i

# # print("Tổng là", tong)

# # n = int(input("Nhập n: ")) #Nhập số n tùy ý
# # tong = 0 #khai báo và gán giá trị cho tong
# # i = 1 #khai báo và gán giá trị cho biến đếm i

# # while i <= n:
# #     tong = tong + i
# #     i = i+1 # cập nhật biến đếm

# # print("Tổng là", tong)


# # Tính tổng tất cả các số trong danh sách A
# # Danh sách A





# A = [1, 3, 5, 9, 11, 2, 6, 8, 10]
# # Biến để lưu trữ tổng các số là tong, gán giá trị ban đầu bằng 0
# tong = 0
# # Vòng lặp for, a là biến lặp
# for a in A:
#      tong = tong+a
# # Đầu ra: Tổng các số là 55
# print("Tổng các số là", tong)




# 



import math
 
print("Giải phương trình bậc 2: ax2 + bx + c = 0 (a, b khác 0)")
print("============")

a = float(input("Mời bạn nhập số a: "))
b = float(input("Mời bạn nhập số b: "))
c = float(input("Mời bạn nhập số c: "))
while True:
    if a == 0 and b == 0:
        print("Một trong hai hệ số a, b phải khác 0: ")
        a = float(input("Mời nhập lại số a: "))
        b = float(input("Mời nhập lại số b: "))
    else:
        break
delta = b**2 - 4 * a * c
# Tìm nghiệm của phương trình
if delta < 0:
    print("Phương trình vô nghiệm")
elif delta == 0:
    print("Phương trình có nghiệm kép x1 = x2 = ", -(b / (2 * a)) )
else:
    print("Phương trình có hai nghiệm phân biệt:")
    print("x1 = ", (-(b) + math.sqrt(delta))/(2*a) )
    print("x1 = ", (-(b) - math.sqrt(delta))/(2*a) )


