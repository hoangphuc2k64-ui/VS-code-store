class SoThuc:
    def __init__(self, x):
        self.x = x

    # Kiem tra so am
    def check_so_am(self):
        if self.x < 0:
            return True
        return False

    # Kiem tra so duong
    def check_so_duong(self):
        if self.x > 0:
            return True
        return False

    # Dem so chu so sau dau phay
    def dem_sau_dau_phay(self):
        s = str(self.x)

        if "." in s:
            phan_nguyen, phan_tp = s.split(".")
            return len(phan_tp)
        return 0


# =====================================================
# Nhap so luong
while True:
    try:
        n = int(input("Nhap so luong so thuc: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so lon hon 0 !")
    except ValueError:
        print("Vui long nhap so nguyen !")


# =====================================================
# Tao tuple chua cac object SoThuc
ds = []
for i in range(n):
    while True:
        try:
            x = float(input(f"Nhap so thuc thu {i + 1}: "))
            ds.append(SoThuc(x))
            break
        except ValueError:
            print("Vui long nhap so !")

tuple_so_thuc = tuple(ds)


# =====================================================
# In ra cac so duong
print("\n=== CAC SO DUONG ===")
for so in tuple_so_thuc:
    if so.check_so_duong():
        print(so.x)


# =====================================================
# Tinh tong cac so am
tong_am = 0

for so in tuple_so_thuc:
    if so.check_so_am():
        tong_am = tong_am + so.x

print("\nTong cac so am =", tong_am)


# =====================================================
# Tim so co nhieu chu so sau dau phay nhat
so_max = tuple_so_thuc[0]

for so in tuple_so_thuc:
    if so.dem_sau_dau_phay() > so_max.dem_sau_dau_phay():
        so_max = so

print("\nSo co nhieu chu so sau dau phay nhat:", so_max.x)
print("So chu so sau dau phay:", so_max.dem_sau_dau_phay())