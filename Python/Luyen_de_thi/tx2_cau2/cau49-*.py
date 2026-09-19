import math
class MachDaoDongLC:
    def __init__(self, ten, l, c):
        self.ten = ten
        self.l = l
        self.c = c
    def tan_so_dao_dong(self):
        return 1/(2 *3.14 *math.sqrt(self.l * self.c))

# =========================================================
while True:
    try:
        n = int(input("Nhap so luong mach: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so lon hon 0")
    except ValueError:
        print("Vui long nhap so")

ds_mach_dd = []
print("\n===============================================")
for i in range(n):
    print(f"\nNhap thong tin mach dao dong LC thu {i+1}:")

    ten = input("Nhap ten mach dao dong: ")

    while True:
        try:
            l = float(input("Nhap gia tri L: "))
            if l > 0:
                break
            else:
                print("Vui long nhap gia tri lon hon 0")
        except ValueError:
            print("Vui long nhap so")

    while True:
        try:
            c = float(input("Nhap gia tri C: "))
            if c > 0:
                break
            else:
                print("Vui long nhap gia tri lon hon 0")
        except ValueError:
            print("Vui long nhap so")

    # add list
    ds_mach_dd.append(MachDaoDongLC(ten, l , c))

# =========================================================
print("\n ==============================================")
print("\n======= Thong tin mach =======")
for i, mach in enumerate(ds_mach_dd):
    print(f"\nMach dao dong LC thu {i+1}: ")
    print("Ten: ", mach.ten)
    print(f"L = {mach.l} (H)")
    print(f"C = {mach.c} (F)")
    print(f"Tan so dao dong = {mach.tan_so_dao_dong()}")

# =========================================================
print("\n======= Danh sach sau khi sap xep =======")
ds_mach_dd.sort(key= lambda mach : mach.tan_so_dao_dong(), reverse= True)
for i, mach in enumerate(ds_mach_dd):
    print(f"\nMach dao dong LC thu {i+1}: ")
    print("Ten: ", mach.ten)
    print(f"L = {mach.l} (H)")
    print(f"C = {mach.c} (C)")
    print(f"Tan so dao dong = {mach.tan_so_dao_dong()}")

# =========================================================
max_obj_f = max(ds_mach_dd, key= lambda mach : mach.tan_so_dao_dong())
max_f = max_obj_f.tan_so_dao_dong()

print("\n=> Max tan so = ", max_f)
for i, mach in enumerate(ds_mach_dd):
    if mach.tan_so_dao_dong() == max_f:
        print(f"\nMach dao dong LC thu {i+1}: ")
        print("Ten: ", mach.ten)
        print(f"L = {mach.l} (H)")
        print(f"C = {mach.c} (C)")
        print(f"Tan so dao dong = {mach.tan_so_dao_dong()}")

