class CongNhan:
    def __init__(self, ten, cs, tg, tien_cong):
        self.ten = ten
        self.cs = cs
        self.tg = tg
        self.tien_cong = tien_cong

    def tong_tien_cong(self):
        return self.cs * self.tg * self.tien_cong


# =========================================================
while True:
    try:
        n = int(input("Nhap so luong cong nhan: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so lon hon 0")
    except ValueError:
        print("Vui long nhap so nguyen")

# =========================================================
ds_cn = []
for i in range(n):
    print(f"\nNhap cong nhan thu {i + 1}: ")
    ten = input("Nhap ten cong nhan: ")

    while True:
        try:
            cs = float(input("Nhap cong suat dao (met/gio): "))
            if cs > 0:
                break
            else:
                print("Cong suat phai lon hon 0")
        except ValueError:
            print("Vui long nhap so")

    while True:
        try:
            tg = float(input("Nhap thoi gian lam viec (gio): "))
            if tg > 0:
                break
            else:
                print("Thoi gian phai lon hon 0")
        except ValueError:
            print("Vui long nhap so")

    while True:
        try:
            tien_cong = float(input("Nhap tien cong cho 1 met: "))
            if tien_cong > 0:
                break
            else:
                print("Tien cong phai lon hon 0")
        except ValueError:
            print("Vui long nhap so")

    ds_cn.append(CongNhan(ten, cs, tg, tien_cong))

# =========================================================
print("\n========== DANH SACH CONG NHAN ==========")
for i, cong_nhan in enumerate(ds_cn):
    print(f"\nCong nhan thu {i + 1}:")
    print("Ten:", cong_nhan.ten)
    print("Tong tien cong:", cong_nhan.tong_tien_cong(), "dong")

# =========================================================
obj_max = max(ds_cn, key=lambda x: x.tong_tien_cong())
tien_cong_max = obj_max.tong_tien_cong()

print("\n========== CONG NHAN CO TIEN CONG CAO NHAT ==========")
print("Tien cong cao nhat:", tien_cong_max, "dong")

for cong_nhan in ds_cn:
    if cong_nhan.tong_tien_cong() == tien_cong_max:
        print("Ten:", cong_nhan.ten)

# =========================================================
tong_tien_luong = 0
for cong_nhan in ds_cn:
    tong_tien_luong += cong_nhan.tong_tien_cong()

print("\nTong tien luong cua ca danh sach:", tong_tien_luong, "dong")