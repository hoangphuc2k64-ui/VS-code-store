class HinhTru:
    def __init__(self, ten, d, h):
        self.ten = ten
        self.d = d
        self.h = h

    def dientich_xq(self):
        return 2 *3.14 *(self.d /2) * self.h 
    def thetich(self):
        return 3.14 *(self.d /2)**2 * self.h

# ====================================================
ds_ht = []
while True:
    try:
        n= int(input("Nhap so luong hinh tru: "))
        if n > 0:
            break
        else:
            print("Nhap so luong > 0 !")
    except ValueError:
        print("Vui long nhap so !")

for i in range(n):
    print(f"\n- Nhap hinh tru thu {i+1}: ")
    ten = input("Nhap ten: ")

    while True:
        try:
            d = float(input("Nhap duong kinh: "))
            if d > 0:
                break
            else:
                print("Vui long nhap duong kinh > 0 !")
        except ValueError:
            print("Vui long nhap so!")

    while True:
        try:
            h = float(input("Nhap duong cao: "))
            if h > 0:
                break
            else:
                print("Vui long nhap duong cao > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    ds_ht.append(HinhTru(ten, d, h))

# ====================================================
print("\n======================================================================")
print("========== 1. Danh sach hinh tru =========")
for i, ht in enumerate(ds_ht):
    print(f"\nHinh tru thu {i+1}: ")
    print("Duong kinh: ", ht.d)
    print("Chieu cao: ", ht.h)
    print("Dien tich xung quanh: ", ht.dientich_xq())
    print("The tich: ", ht.thetich())

# ====================================================
print("\n=========== 2. Max / min the tich ===============")
max_thetich = max(ds_ht, key= lambda ht: ht.thetich())
min_thetich = min(ds_ht, key= lambda ht: ht.thetich())
print("\n=> Max the tich: ", max_thetich.thetich())
print("\n=> Min the tich: ", min_thetich.thetich())

# bonus in ra
for i, ht in enumerate(ds_ht):
    if ht.thetich() == max_thetich.thetich():
        print(f"\nHinh tru co the tich max la hinh thu {i+1}: ")
        print("Duong kinh: ", ht.d)
        print("Chieu cao: ", ht.h)
        print("Dien tich xung quanh: ", ht.dientich_xq())
        print("The tich: ", ht.thetich())
    if ht.thetich() == min_thetich.thetich():
        print(f"\nHinh tru co the tich min la hinh thu {i+1}: ")
        print("Duong kinh: ", ht.d)
        print("Chieu cao: ", ht.h)
        print("Dien tich xung quanh: ", ht.dientich_xq())
        print("The tich: ", ht.thetich())

# ====================================================
print("\n======== 3. Tong dien tich xung quanh =========")
tong_dt_xq = 0
for ht in ds_ht:
    tong_dt_xq = tong_dt_xq + ht.dientich_xq()
print("\n=> Tong dien tich xung quanh: ", tong_dt_xq)