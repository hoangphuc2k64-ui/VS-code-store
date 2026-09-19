class MayTinh:
    def __init__(self, ten, thoi_gian_su_dung, tinh_trang):
        self.ten = ten
        self.thoi_gian_su_dung = thoi_gian_su_dung
        self.tinh_trang = tinh_trang
    def thanhly_or_not(self):
        if self.thoi_gian_su_dung >= 5: 
            return True
        elif self.thoi_gian_su_dung > 3 and self.tinh_trang.lower() == "hong":
            return True
        else:
            return False

# =========================================================
ds_mt = []
while True:
    try:
        n = int(input("Nhap so luong may tinh: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so lon hon 0 !")
    except ValueError:
        print("Vui long nhap so !")

print("\n====== Nhap danh sach may tinh ======")
for i in range(n):
    print(f"\nNhap may tinh thu {i+1}: ")
    ten = input("Nhap ten may tinh: ")

    while True:
        try:
            thoi_gian_su_dung = float(input("Nhap thoi gian su dung (nam): "))
            if thoi_gian_su_dung > 0:
                break
            else:
                print("Vui long nhap thoi gian > 0 !")
        except ValueError:
            print("Vui long nhap so nam !")

    while True:
        tinh_trang = input("Nhap tinh trang may tinh: ")
        if tinh_trang.lower() == "tot" or tinh_trang.lower() == "hong":
            break
        else:
            print("Vui long nhap dung tinh trang !")

    # add list
    ds_mt.append(MayTinh(ten, thoi_gian_su_dung, tinh_trang))

# ==============================================================
print("\n====== Danh sach may tinh ======")
for i, mt in enumerate(ds_mt):
    print(f"\nMay tinh thu {i+1}: ")
    print("Ten: ", mt.ten)
    print("Thoi gian da su dung: ", mt.thoi_gian_su_dung)
    print("Tinh trang: ", mt.tinh_trang)
    print("Thanh ly khong(True = Yes, False = No): ", mt.thanhly_or_not())

# ==============================================================
#tao tuple chua may tinh chua thanh ly
ds_mt_chua_thanhly = []
for mt in ds_mt:
    if mt.thanhly_or_not() is False:
        ds_mt_chua_thanhly.append(mt)
tuple_mt_chua_thanhly = tuple(ds_mt_chua_thanhly)

print("\n====== Danh sach may tinh chua thanh ly ======")
for i, mt in enumerate(tuple_mt_chua_thanhly):
    print(f"\nMay tinh thu {i+1}: ")
    print("Ten: ", mt.ten)
    print("Thoi gian da su dung: ", mt.thoi_gian_su_dung)
    print("Tinh trang: ", mt.tinh_trang)
    print("Thanh ly khong(True = Yes, False = No)", mt.thanhly_or_not())

# ==============================================================
# remove 
ds_mt_thanhly = []
for mt in ds_mt:
    if mt.thanhly_or_not() is True:
        ds_mt_thanhly.append(mt)

print("\n====== Danh sach may tinh sau khi xoa may tinh thanh ly ======")

print("\n=> So may tinh bi thanh ly: ", len(ds_mt_thanhly))
for mt in ds_mt_thanhly:
    ds_mt.remove(mt)

for i, mt in enumerate(ds_mt):
    print(f"\nMay tinh thu {i+1}: ")
    print("Ten: ", mt.ten)
    print("Thoi gian da su dung: ", mt.thoi_gian_su_dung)
    print("Tinh trang: ", mt.tinh_trang)
    print("Thanh ly khong(True = Yes, False = No)", mt.thanhly_or_not())
