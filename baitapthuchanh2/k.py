import math
from abc import ABC, abstractmethod

class HinhTamGiac(ABC):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
    
    def chu_vi(self):
        return self.a + self.b + self.c
    
    @abstractmethod
    def dien_tich(self):
        pass

class TamGiacVuong(HinhTamGiac):
    def dien_tich(self):
        p = self.chu_vi() / 2
        return self.a * self.b / 2

class TamGiacDeu(HinhTamGiac):
    def dien_tich(self):
        return math.sqrt(3) / 4 * self.a ** 2

# Thiết kế giao diện
while True:
    print('Chọn loại tam giác để nhập:')
    print('1. Tam giác vuông')
    print('2. Tam giác đều')
    choice = input('Chọn (1 hoặc 2): ')

    if choice == '1':
        a = float(input('Nhập độ dài cạnh góc vuông: '))
        b = float(input('Nhập độ dài cạnh kề góc vuông: '))
        c = math.sqrt(a ** 2 + b ** 2)
        tam_giac = TamGiacVuong(a, b, c)
        break
    elif choice == '2':
        a = float(input('Nhập độ dài cạnh: '))
        tam_giac = TamGiacDeu(a, a, a)
        break
    else:
        print('Lựa chọn không hợp lệ. Vui lòng nhập lại.')

# Tính chu vi và diện tích
chu_vi = tam_giac.chu_vi()
dien_tich = tam_giac.dien_tich()

# In ra kết quả
if isinstance(tam_giac, TamGiacVuong):
    print(f'Tam giác vuông có cạnh góc vuông là {tam_giac.a:.2f} và cạnh kề góc vuông là {tam_giac.b:.2f}:')
else:
    print(f'Tam giác đều có cạnh là {tam_giac.a:.2f}:')
print(f'Chu vi là {chu_vi:.2f}')
print(f'Diện tích là {dien_tich:.2f}')
