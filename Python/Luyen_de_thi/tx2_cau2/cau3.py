import math

class HinhVuong:
    def __init__(self, a):
        self.a = a

    def tinh_chu_vi(self):
        return (4 *self.a)

    def tinh_dien_tich(self):
        return (self.a **2)

    def tinh_duong_cheo(self):
        return (math.sqrt(2) *self.a)

while True:
    try:
        n = int(input("Nhap so luong hinh vuong: "))
        if n > 0:
            break
        else:
            print("Nhap so lon hon 0 !")
    except ValueError:
        print("Vui long nhap so nguyen !")

# =====================================
ds_hv = []
for i in range(n):
    print(f"\nNhap canh hinh vuong thu {i+1}: ")
    while True:
        try:
            x = float(input("Nhap canh a = "))
            if x > 0:
                break
            else:
                print("Nhap so lon hon 0 !")
        except ValueError:
            print("Vui long nhap so !")
    ds_hv.append(HinhVuong(x))

# ==========================================================
# in 1
for i, hv in enumerate(ds_hv):
    print(f"\nHinh vuong thu {i+1}: ")
    print("4 canh = ", hv.a)
    print("=> Chu vi: ", hv.tinh_chu_vi())

# in 2
tong_dt = 0
for hv in ds_hv:
    tong_dt = tong_dt + hv.tinh_dien_tich()
print("\n=> Tong dien tich: ", tong_dt)

# in 3
hv_min = ds_hv[0]
for hv in ds_hv:
    if hv_min.tinh_duong_cheo() > hv.tinh_duong_cheo():
        hv_min = hv

print("\n ==== Hinh vuong co duong cheo min ====")
print("4 canh = ", hv_min.a)
print("=> Chu vi: ", hv_min.tinh_chu_vi())
print("=> Dien tich: ", hv_min.tinh_dien_tich())



    