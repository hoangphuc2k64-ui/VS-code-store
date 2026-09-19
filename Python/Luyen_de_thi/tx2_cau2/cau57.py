class LoApTrung:
    def __init__(self, k, t, x, y):
        self.k = k
        self.t = t
        self.x = x
        self.y = y

    def tien_thu_ve(self):
        so_trung_no = self.k * self.t / 100
        so_trung_hong = self.k - so_trung_no
        return so_trung_no * self.x + so_trung_hong * self.y

# ===============================================
while True:
    try:
        n = int(input("Nhap so luong lo ap trung: "))
        if n > 0:
            break
        else:
            print("Vui long nhap n > 0")
    except ValueError:
        print("Vui long nhap so")

ds_lo = []
for i in range(n):
    print(f"\nNhap lo ap trung thu {i+1}:")
    k = int(input("Nhap so trung ap: "))
    t = float(input("Nhap ti le trung no (%): "))
    x = float(input("Nhap gia ban 1 con vit: "))
    y = float(input("Nhap gia ban 1 trung hong: "))

    ds_lo.append(LoApTrung(k, t, x, y))

# =============================================
# In danh sach
print("\n========== DANH SACH ==========")
for i, lo in enumerate(ds_lo):
    print(f"\nLo ap thu {i+1}:")
    print("k =", lo.k)
    print("t =", lo.t)
    print("x =", lo.x)
    print("y =", lo.y)
    print("So tien thu ve =", lo.tien_thu_ve())

# Tao tuple chua so tien thu ve
tuple_tien = tuple(lo.tien_thu_ve() for lo in ds_lo)

print("\nTuple so tien thu ve:")
print(tuple_tien)

# Sap xep giam dan theo so trung hong
ds_lo.sort(key=lambda lo: lo.k - lo.k * lo.t / 100, reverse=True)

print("\n===== GIAM DAN THEO SO TRUNG HONG =====")
for lo in ds_lo:
    print("k =", lo.k,
          "- So trung hong =", lo.k - lo.k * lo.t / 100,
          "- Tien =", lo.tien_thu_ve())