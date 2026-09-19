class SinhVien:
    def __init__(self, ten, diem_tich_luy, so_tin_no):
        self.ten = ten
        self.diem_tich_luy = diem_tich_luy
        self.so_tin_no = so_tin_no

    def tinh_trang(self):
        if self.diem_tich_luy < 0.8 or self.so_tin_no > 20:
            return "Bi duoi hoc"
        elif 0.8 <= self.diem_tich_luy <= 1.0 and self.so_tin_no <= 20:
            return "Canh cao"
        else:
            return "Tiep tuc hoc"

# ===================================================================
ds_sv = []
# nhap list
while True:
    try:
        n = int(input("Nhap so luong sinh vien: "))
        if n > 0:
            break
        else:
            print("Nhap so luong lon hon 0 !")
    except ValueError:
        print("Vui long nhap so nguyen !")

for i in range(n):
    print(f"\n=== Nhap sinh vien thu {i+1} ===")
    # ten
    ten = input("Nhap ten sinh vien: ")

    # diem tich luy
    while True:
        try:
            diem_tich_luy = float(input("Nhap diem tich luy: "))
            if 0 <= diem_tich_luy <= 4:
                break
            else:
                print("Nhap 0 <= diem <= 4")
        except ValueError:
            print("Vui long nhap so !")

    # so tin no
    while True:
        try:
            so_tin_no = int(input("Nhap so tin no: "))
            if so_tin_no >= 0:
                break
            else:
                print("Nhap so tin no >= 0 !")
        except ValueError:
            print("Vui long nhap so !")

    # add list
    ds_sv.append(SinhVien(ten, diem_tich_luy, so_tin_no))

# ===================================================================
print("\n==== Danh sach sinh vien ====")
for i, sv in enumerate(ds_sv):
    print(f"\nSinh vien thu {i+1}: ")
    print("Ten: ", sv.ten)
    print("Diem tich luy: ", sv.diem_tich_luy)
    print("So tin no: ", sv.so_tin_no)
    print("Tinh trang:", sv.tinh_trang())

# ===================================================================
dict_sv = {}
for sv in ds_sv:
    if sv.tinh_trang() == "Bi duoi hoc" or sv.tinh_trang() == "Canh cao":
        dict_sv[sv.ten] = sv.tinh_trang()
print("\nDictionary: ", dict_sv)

# ===================================================================
ds_sv.sort(key = lambda sv: sv.diem_tich_luy, reverse = True)       # reverse dao chieu sx (giam)
print("\n==== Danh sach sinh vien sau khi xep giam dan ====")
for i, sv in enumerate(ds_sv):
    print(f"\nSinh vien thu {i+1}: ")
    print("Ten: ", sv.ten)
    print("Diem tich luy: ", sv.diem_tich_luy)
    print("So tin no: ", sv.so_tin_no)
    print("Tinh trang:", sv.tinh_trang())

