class DienTro:
    def __init__(self, v1, v2, v3):
        self.v1 = v1
        self.v2 = v2
        self.v3 = v3

    def gia_tri_dien_tro(self):
        bang_mau = {
            "den": 0,
            "nau": 1,
            "do": 2,
            "cam": 3,
            "vang": 4,
            "luc": 5,
            "lam": 6,
            "tim": 7,
            "xam": 8,
            "trang": 9
        }
        return (bang_mau[self.v1] * 10 + bang_mau[self.v2]) * (10 ** bang_mau[self.v3])

# ===========================================
while True:
    try:
        n = int(input("Nhap so luong dien tro: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so luong > 0")
    except ValueError:
        print("Vui long nhap so")

bang_mau = {
    "den": 0,
    "nau": 1,
    "do": 2,
    "cam": 3,
    "vang": 4,
    "luc": 5,
    "lam": 6,
    "tim": 7,
    "xam": 8,
    "trang": 9
}

ds_dien_tro = []
print("\n========== NHAP DANH SACH DIEN TRO ==========")
for i in range(n):
    while True:
        print(f"\nNhap dien tro thu {i+1}:")
        v1 = input("Nhap mau vong 1: ").lower()
        v2 = input("Nhap mau vong 2: ").lower()
        v3 = input("Nhap mau vong 3: ").lower()
        if v1 in bang_mau and v2 in bang_mau and v3 in bang_mau:
            break
        else:
            print("Vui long nhap mau hop le (den, nau, do, cam, vang, luc, lam, tim, xam, trang)!")
    ds_dien_tro.append(DienTro(v1, v2, v3))

# ===========================================
print("\n========== DANH SACH DIEN TRO ==========")
for i, dien_tro in enumerate(ds_dien_tro):
    print(f"\nDien tro thu {i+1}:")
    print("Mau vong 1:", dien_tro.v1)
    print("Mau vong 2:", dien_tro.v2)
    print("Mau vong 3:", dien_tro.v3)
    print("Gia tri dien tro:", dien_tro.gia_tri_dien_tro(), "ohm")

# ===========================================
# Tao tuple chua gia tri cua n dien tro
ds_gia_tri_dien_tro = []
for dien_tro in ds_dien_tro:
    ds_gia_tri_dien_tro.append(dien_tro.gia_tri_dien_tro())

tuple_gia_tri_dien_tro = tuple(ds_gia_tri_dien_tro)
print("\nTuple gia tri dien tro:", tuple_gia_tri_dien_tro)

# ===========================================
# Tim dien tro co gia tri nho nhat
dien_tro_nho_nhat = min(ds_dien_tro, key=lambda x: x.gia_tri_dien_tro())

print("\n========== DIEN TRO CO GIA TRI NHO NHAT ==========")
for i, dien_tro in enumerate(ds_dien_tro):
    if dien_tro.gia_tri_dien_tro() == dien_tro_nho_nhat.gia_tri_dien_tro():
        print(f"\nDien tro thu {i+1}:")
        print("Mau vong 1:", dien_tro.v1)
        print("Mau vong 2:", dien_tro.v2)
        print("Mau vong 3:", dien_tro.v3)
        print("Gia tri dien tro:", dien_tro.gia_tri_dien_tro(), "ohm")