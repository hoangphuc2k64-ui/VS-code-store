class TuGiac:
    def __init__(self, a, b, c, d):
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def chu_vi(self):
        return self.a + self.b + self.c + self.d

    def canh_max(self):
        return max(self.a, self.b, self.c, self.d)

# ==========================================================
while True:
    try:
        n = int(input("Nhap so luong tu giac"))
        if n > 0:
            break
        else:
            print("Vui long nhap so luong > 0 !")
    except ValueError:
        print("Vui long nhap so nguyen !")

ds_tg = []
print("\n======= Nhap thong tin tu giac =======")
for i in range(n):
    print(f"\nNhap canh cua tu giac thu {i+1}: ")

    while True:
        try:
            a = float(input("Nhap canh a: "))
            if a > 0:
                break
            else:
                print("Nhap canh > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    while True:
        try:
            b = float(input("Nhap canh b: "))
            if b > 0:
                break
            else:
                print("Nhap canh > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    while True:
        try:
            c = float(input("Nhap canh c: "))
            if c > 0:
                break
            else:
                print("Nhap canh > 0 !")
        except ValueError:
            print("Vui long nhap so !")   

    while True:
        try:
            d = float(input("Nhap canh d: "))
            if d > 0:
                break
            else:
                print("Nhap canh > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    # add list
    ds_tg.append(TuGiac(a, b, c, d))

# ==========================================================
print("\n======= Danh sach tu giac =======")
for i, tg in enumerate(ds_tg):
    print(f"\nTu giac thu {i+1}: ")
    print("Canh a: ", tg.a)
    print("Canh b: ", tg.b)
    print("Canh c: ", tg.c)
    print("Canh d: ", tg.d)
    print("Chu vi: ", tg.chu_vi())
    print("Canh lon nhat: ", tg.canh_max())

# Canh lon nhat cua moi tu giac
print("\n======= Canh lon nhat cua moi tu giac =======")
for i, tg in enumerate(ds_tg):
    print(f"Tu giac thu {i+1}: {tg.canh_max()}")

# Hinh co chu vi nho nhat
tg_min = min(ds_tg, key = lambda tg: tg.chu_vi())
print("\n======= Tu giac co chu vi nho nhat =======")
print("Canh a: ", tg_min.a)
print("Canh b: ", tg_min.b)
print("Canh c: ", tg_min.c)
print("Canh d: ", tg_min.d)
print("Chu vi: ", tg_min.chu_vi())