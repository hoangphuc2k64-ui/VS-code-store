import math

class HinhTron:
    def __init__(self, r):
        self.r = r

    # Tinh chu vi
    def tinh_chu_vi(self):
        return 2 * math.pi * self.r

    # Tinh dien tich
    def tinh_dien_tich(self):
        return math.pi * self.r**2


# =====================================================
# Nhap so luong hinh tron
while True:
    try:
        n = int(input("Nhap so luong hinh tron: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so lon hon 0 !")
    except ValueError:
        print("Vui long nhap so nguyen !")


# =====================================================
# Tao list cac object HinhTron
ds_ht = []

for i in range(n):
    while True:
        try:
            r = float(input(f"Nhap ban kinh hinh tron thu {i+1}: "))

            if r > 0:
                ds_ht.append(HinhTron(r))
                break
            else:
                print("Ban kinh phai lon hon 0 !")

        except ValueError:
            print("Vui long nhap so !")


# =====================================================
# Tinh chu vi cua n hinh tron
print("\n===== CHU VI CAC HINH TRON =====")

for i, ht in enumerate(ds_ht):
    print(f"Hinh tron thu {i+1}:")
    print("Ban kinh =", ht.r)
    print("Chu vi =", ht.tinh_chu_vi())


# =====================================================
# Tinh tong dien tich cac hinh tron
tong_dien_tich = 0

for ht in ds_ht:
    tong_dien_tich = tong_dien_tich + ht.tinh_dien_tich()

print("\nTong dien tich =", tong_dien_tich)


# =====================================================
# Tim hinh tron nho nhat
ht_min = ds_ht[0]

for ht in ds_ht:
    if ht.r < ht_min.r:
        ht_min = ht

print("\n===== HINH TRON NHO NHAT =====")
print("Ban kinh =", ht_min.r)
print("Chu vi =", ht_min.tinh_chu_vi())
print("Dien tich =", ht_min.tinh_dien_tich())