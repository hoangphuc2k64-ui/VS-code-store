import datetime
class ThiSinh:
    def __init__(self, ten, nam_sinh, diem_toan, diem_van, diem_ngoai_ngu):
        self.ten = ten
        self.nam_sinh = nam_sinh
        self.diem_toan = diem_toan
        self.diem_van = diem_van
        self.diem_ngoai_ngu = diem_ngoai_ngu

    def tinh_tuoi(self):
        nam_hien_tai = datetime.datetime.now().year
        return nam_hien_tai - self.nam_sinh

    def tinh_tong_diem(self):
        return self.diem_toan + self.diem_van + self.diem_ngoai_ngu

# ===============================================================================
while True:
    try:
        n = int(input("Nhap so luong thi sinh: "))
        if n > 0:
            break
        else:
            print("Nhap so luong lon hon 0")
    except ValueError:
        print("Vui long nhap so nguyen !")

# ===============================================================================
ds_thisinh = []
for i in range(n):
    print(f"\nNhap thong tin thi sinh thu {i+1}:")

    # ten ====
    ten = input("Nhap ten thi sinh: ")
    # nam sinh =====
    while True:
        try:
            nam_sinh = int(input("Nhap nam sinh: "))
            if nam_sinh > 0:
                break
            else:
                print("Nhap nam sinh lon hon 0 !")
        except ValueError:
            print("Vui long nhap so nguyen !")
    # diem toan ===
    while True:
        try:
            diem_toan = float(input("Nhap diem toan: "))
            if 0 < diem_toan <= 10:
                break
            else:
                print("Diem tu 0 den 10")
        except ValueError:
            print("Vui long nhap so !")
    # diem van ====
    while True:
        try:
            diem_van = float(input("Nhap diem van: "))
            if 0 < diem_van <= 10:
                break
            else:
                print("Diem tu 0 den 10")
        except ValueError:
            print("Vui long nhap so !")
    # diem ngoai ngu ====
    while True:
        try:
            diem_ngoai_ngu = float(input("Nhap diem ngoai ngu: "))
            if 0 < diem_ngoai_ngu <= 10:
                break
            else:
                print("Diem tu 0 den 10")
        except ValueError:
            print("Vui long nhap so !")

    ds_thisinh.append(ThiSinh(ten, nam_sinh, diem_toan, diem_van, diem_ngoai_ngu))

# =========================================================================
for i, ts in enumerate(ds_thisinh):
    print(f"\nThi sinh thu {i+1}: ")
    print("Ten: ", ts.ten)
    print("Tuoi: ", ts.tinh_tuoi())
    print("Diem toan: ", ts.diem_toan)
    print("Diem van: ", ts.diem_van)
    print("Diem ngoai ngu: ", ts.diem_ngoai_ngu)
    print(f"=> Tong diem cua sinh vien thu {i+1}: ", ts.tinh_tong_diem())

# in 2: tim thi sinh it tuoi nhat
ts_tuoi_min = ds_thisinh[0]
for ts in ds_thisinh:
    if ts_tuoi_min.tinh_tuoi() > ts.tinh_tuoi():
        ts_tuoi_min = ts
print(f"\n=> Thi sinh co tuoi it nhat la {ts_tuoi_min.ten}: ", ts_tuoi_min.tinh_tuoi())

# in 3: thi sinh co diem toan cao nhat
ts_toan_max = ds_thisinh[0]
for ts in ds_thisinh:
    if ts_toan_max.diem_toan < ts.diem_toan:
        ts_toan_max = ts
print(f"\n=> Thi sinh co diem toan cao nhat la {ts_toan_max.ten}: ", ts_toan_max.diem_toan)




