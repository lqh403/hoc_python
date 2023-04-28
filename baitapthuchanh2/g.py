class SinhVien:
    def __init__(self, ho_ten, nam_sinh, diem_toan, diem_van, diem_ngoai_ngu):
        self.ho_ten = ho_ten
        self.nam_sinh = nam_sinh
        self.diem_toan = diem_toan
        self.diem_van = diem_van
        self.diem_ngoai_ngu = diem_ngoai_ngu
    
    def tong_diem(self):
        return self.diem_toan + self.diem_van + self.diem_ngoai_ngu

# Nhập danh sách sinh viên
danh_sach_sinh_vien = [
    SinhVien('Nguyen Van A', 2001, 8, 7, 6),
    SinhVien('Tran Thi B', 2002, 7, 8, 9),
    SinhVien('Le Van C', 2000, 9, 9, 8),
    SinhVien('Pham Thi D', 2001, 6, 7, 8),
    SinhVien('Hoang Van E', 2003, 9, 8, 7)
]

# Sắp xếp danh sách sinh viên theo thứ tự giảm dần của tổng điểm 3 môn
danh_sach_sinh_vien.sort(key=lambda sv: sv.tong_diem(), reverse=True)

# Tính trung bình cộng điểm toán
tbc_diem_toan = sum(sv.diem_toan for sv in danh_sach_sinh_vien) / len(danh_sach_sinh_vien)

# Tính trung bình cộng điểm văn
tbc_diem_van = sum(sv.diem_van for sv in danh_sach_sinh_vien) / len(danh_sach_sinh_vien)

# Tính trung bình cộng điểm ngoại ngữ
tbc_diem_ngoai_ngu = sum(sv.diem_ngoai_ngu for sv in danh_sach_sinh_vien) / len(danh_sach_sinh_vien)

# In ra kết quả
print('Danh sách sinh viên:')
for sv in danh_sach_sinh_vien:
    print(f'{sv.ho_ten}, {sv.nam_sinh}, {sv.diem_toan}, {sv.diem_van}, {sv.diem_ngoai_ngu}, {sv.tong_diem()}')

print(f'Trung bình cộng điểm toán: {tbc_diem_toan:.2f}')
print(f'Trung bình cộng điểm văn: {tbc_diem_van:.2f}')
print(f'Trung bình cộng điểm ngoại ngữ: {tbc_diem_ngoai_ngu:.2f}')
