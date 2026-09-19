class TauCa:
    def __init__(self, ten, dau_tieu_thu, gia_dau, tien_ban_ca, k = 5):
        self.ten = ten
        self.dau_tieu_thu = dau_tieu_thu
        self.gia_dau = gia_dau
        self.tien_ban_ca = tien_ban_ca
        self.k = k
    def lai_or_not(self):
        if (self.tien_ban_ca) >= self.k * (self.dau_tieu_thu * self.gia_dau):
            return "Lai"
        else:
            return "Lo"

# =========================================================
ds_tauca = []
while True:
    try:
        n = int(input("Nhap so luong tau ca: "))
        if n > 0:
            break
        else:
            print("Nhap so luong tau > 0 !")
    except ValueError:
        print("Vui long nhap so nguyen !")

print("\n======= Nhap danh sach tau ca =======")
for i in range(n):
    print(f"\nTau ca thu {i+1}: ")
    ten = input("Nhap ten tau: ")
    while True:
        try:
            dau_tieu_thu = float(input("Nhap luong dau tieu thu: "))
            if dau_tieu_thu > 0:
                break
            else:
                print("Vui long nhap so > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    while True:
        try:
            gia_dau = float(input("Nhap gia dau: "))
            if gia_dau > 0:
                break
            else:
                print("Nhap so > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    while True:
        try:
            tien_ban_ca = float(input("Nhap so tien ban ca duoc: "))
            if tien_ban_ca > 0:
                break
            else:
                print("Nhap so tien > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    ds_tauca.append(TauCa(ten, dau_tieu_thu, gia_dau, tien_ban_ca))

# =========================================================
print("\n====== Danh sach  tau ca ban dau ======")
for i, tauca in enumerate(ds_tauca):
    print(f"Tau ca thu {i+1}: ")
    print("Ten: ", tauca.ten)
    print("Luong dau tieu thu (l): ", tauca.dau_tieu_thu)
    print("Gia dau: ", tauca.gia_dau)
    print("Tien ban ca thu duoc: ", tauca.tien_ban_ca)
    print(f"Trang thai tau {i+1}: ", tauca.lai_or_not())

# =========================================================
# tao tuple chua cac tau ca co lai
ds_tau_colai = []
for tauca in ds_tauca:
    if tauca.lai_or_not() == "Lai":
        ds_tau_colai.append(tauca)
tuple_tau_colai = tuple(ds_tau_colai)

print("\n====== Danh sach tau ca co lai======")
for i, tauca in enumerate(tuple_tau_colai):
    print(f"Tau ca thu {i+1}: ")
    print("Ten: ", tauca.ten)
    print("Luong dau tieu thu (l): ", tauca.dau_tieu_thu)
    print("Gia dau: ", tauca.gia_dau)
    print(f"Trang thai tau {i+1}: ", tauca.lai_or_not())

# =========================================================
ds_tauca.sort(key = lambda tauca: tauca.lai_or_not())
print("\n====== Danh sach sap xep tau ca theo lai ======")
for i, tauca in enumerate(ds_tauca):
    print(f"\nTau ca thu {i+1}: ")
    print("Ten: ", tauca.ten)
    print("Luong dau tieu thu (l): ", tauca.dau_tieu_thu)
    print("Gia dau: ", tauca.gia_dau)
    print("Tien ban ca thu duoc: ", tauca.tien_ban_ca)
    print(f"Trang thai tau {i+1}: ", tauca.lai_or_not())




