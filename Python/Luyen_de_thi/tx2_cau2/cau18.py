class NhanVien:
    def __init__(self, ho_ten, so_nam_ct, luong_cb, he_so_luong):
        self.ho_ten = ho_ten
        self.so_nam_ct = so_nam_ct
        self.luong_cb = luong_cb
        self.he_so_luong = he_so_luong

    # Tinh luong
    def tinh_luong(self):
        return self.luong_cb * self.he_so_luong + self.so_nam_ct * 0.1 * self.luong_cb


# =====================================================
# Nhap so luong nhan vien

while True:
    try:
        n = int(input("Nhap so luong nhan vien: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so lon hon 0 !")
    except ValueError:
        print("Vui long nhap so nguyen !")


# =====================================================
# Tao list nhan vien

ds_nv = []

for i in range(n):
    print(f"\n=== Nhap nhan vien thu {i+1} ===")

    ho_ten = input("Nhap ho ten: ")

    while True:
        try:
            so_nam_ct = int(input("Nhap so nam cong tac: "))
            if so_nam_ct >= 0:
                break
            else:
                print("So nam cong tac phai >= 0 !")
        except ValueError:
            print("Vui long nhap so nguyen !")

    while True:
        try:
            luong_cb = float(input("Nhap luong co ban: "))
            he_so_luong = float(input("Nhap he so luong: "))

            if luong_cb > 0 and he_so_luong > 0:
                break
            else:
                print("Luong va he so luong phai > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    nv = NhanVien(ho_ten, so_nam_ct, luong_cb, he_so_luong)
    ds_nv.append(nv)

# =====================================================
# In danh sach nhan vien

print("\n===== DANH SACH NHAN VIEN =====")

for i, nv in enumerate(ds_nv):
    print(f"\nNhan vien thu {i+1}:")
    print("Ho ten:", nv.ho_ten)
    print("So nam cong tac:", nv.so_nam_ct)
    print("Luong co ban:", nv.luong_cb)
    print("He so luong:", nv.he_so_luong)
    print("Luong:", nv.tinh_luong())

# =====================================================
# Tim nhan vien co so nam cong tac lon nhat
nv_max = ds_nv[0]
for nv in ds_nv:
    if nv.so_nam_ct > nv_max.so_nam_ct:
        nv_max = nv

print("\n===== NHAN VIEN CONG TAC LAU NHAT =====")
print("Ho ten:", nv_max.ho_ten)
print("So nam cong tac:", nv_max.so_nam_ct)

# =====================================================
# Tinh tong luong
tong_luong = 0
for nv in ds_nv:
    tong_luong = tong_luong + nv.tinh_luong()

print("\nTong luong =", tong_luong)