class MonHoc:
    def __init__(self, ma_mon, ten_mon, so_tiet):
        self.ma_mon = ma_mon
        self.ten_mon = ten_mon
        self.so_tiet = so_tiet

    def hien_thi(self):
        print(f"  Mã môn: {self.ma_mon}, Tên môn: {self.ten_mon}, Số tiết: {self.so_tiet}")

class HocVien:
    def __init__(self, ma_dinh_danh, ten, nam_sinh):
        self.ma_dinh_danh = ma_dinh_danh
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.ds_mon = []   # danh sách môn học

    def them_mon(self, mon):
        self.ds_mon.append(mon)

    def so_luong_mon(self):
        return len(self.ds_mon)

    def hien_thi(self):
        print(f"Mã: {self.ma_dinh_danh}, Tên: {self.ten}, Năm sinh: {self.nam_sinh}")
        for mon in self.ds_mon:
            mon.hien_thi()

def nhap_hoc_vien():
    ma = input("Nhập CCCD / mã giấy khai sinh: ")
    ten = input("Nhập tên học viên: ")
    nam_sinh = int(input("Nhập năm sinh: "))

    hv = HocVien(ma, ten, nam_sinh)

    so_mon = int(input("Số môn đăng ký: "))
    for _ in range(so_mon):
        ma_mon = input("  Mã môn: ")
        ten_mon = input("  Tên môn: ")
        so_tiet = int(input("  Số tiết: "))
        hv.them_mon(MonHoc(ma_mon, ten_mon, so_tiet))

    return hv

def ghi_file(ds_hoc_vien, filename="DSHV.txt"):
    with open(filename, "w", encoding="utf-8") as f:
        for hv in ds_hoc_vien:
            f.write(f"{hv.ma_dinh_danh}|{hv.ten}|{hv.nam_sinh}|{hv.so_luong_mon()}\n")
            for mon in hv.ds_mon:
                f.write(f"{mon.ma_mon}|{mon.ten_mon}|{mon.so_tiet}\n")

def hien_thi_tat_ca(ds_hoc_vien):
    print("\nDANH SÁCH HỌC VIÊN")
    for hv in ds_hoc_vien:
        hv.hien_thi()
        print("-" * 30)

def hoc_vien_it_nhat_2_mon(ds_hoc_vien):
    print("\nHỌC VIÊN ĐĂNG KÝ ÍT NHẤT 2 MÔN")
    for hv in ds_hoc_vien:
        if hv.so_luong_mon() >= 2:
            hv.hien_thi()
            print("-" * 30)

def main():
    ds_hoc_vien = []

    while True:
        print("\n1. Nhập học viên")
        print("2. Hiển thị tất cả")
        print("3. Học viên đăng ký ≥ 2 môn")
        print("0. Thoát")

        chon = input("Chọn: ")

        if chon == "1":
            hv = nhap_hoc_vien()
            ds_hoc_vien.append(hv)
            ghi_file(ds_hoc_vien)
        elif chon == "2":
            hien_thi_tat_ca(ds_hoc_vien)
        elif chon == "3":
            hoc_vien_it_nhat_2_mon(ds_hoc_vien)
        elif chon == "0":
            break
        else:
            print("Chọn sai!")

main()
