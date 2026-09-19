class ThongThap:
    def __init__(self, ten, r, c):
        self.ten = ten
        self.r = r
        self.c = c
    def tan_so_cat(self):
        return 1/(2 *3.14 *self.r *self.c)

# ==========================================================
while True:
    try:
        n = int(input("Nhap so luong mach thong thap: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so luong > 0 !")
    except ValueError:
        print("Vui long nhap so !")

ds_thongthap = []
print("\n========= Nhap thong tin mach thong thap ==========")
for i in range(n):
    print(f"\nNhap thong tin mach thong thap thu {i+1}: ")

    ten = input("Nhap ten mach thong thap: ")

    while True:
        try:
            r = float(input("Nhap gia tri dien tro (Ohm): "))
            if r > 0:
                break
            else:
                print("Dien tro hong, vui long nhap gia tri > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    while True:
        try:
            c = float(input("Nhap gia tri dien tich (F): "))
            if c > 0:
                break
            else:
                print("Vui long nhap gia tri > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    # add list
    ds_thongthap.append(ThongThap(ten, r, c))

# ==========================================================
print("\n========= Danh sach mach thong thap ==========")
for i, tt in enumerate(ds_thongthap):
    print(f"\nMach thong thap thu {i+1}: ")
    print("Ten: ", tt.ten)
    print(f"Dien tro: {tt.r} (Ohm)")
    print(f"Dien tich: {tt.c} (F)")
    print("Tan so cat: ", tt.tan_so_cat())

# ===========================================================
ds_thongthap.sort(key= lambda tt: tt.r, reverse= True)
print("\n========= Danh sach mach thong thap sau khi sap xep ==========")
for i, tt in enumerate(ds_thongthap):
    print(f"\nMach thong thap thu {i+1}: ")
    print("Ten: ", tt.ten)
    print(f"Dien tro: {tt.r} (Ohm)")
    print(f"Dien tich: {tt.c} (F)")
    print("Tan so cat: ", tt.tan_so_cat())

# ==========================================================
# Tim mach co dai thong lon nhat
td_max = max(ds_thongthap, key=lambda tt: tt.tan_so_cat())

print("\n========= Mach co dai thong lon nhat ==========")
print("Ten: ", td_max.ten)
print(f"Dien tro: {td_max.r} (Ohm)")
print(f"Dien dung: {td_max.c} (F)")
print("Tan so cat: ", td_max.tan_so_cat(), "Hz")

