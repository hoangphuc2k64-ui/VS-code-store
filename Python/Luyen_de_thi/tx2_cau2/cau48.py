class MayTinh:
    def __init__(self, ten_loai, dung_luong_RAM, dung_luong_o_cung):
        self.ten_loai = ten_loai
        self.dung_luong_RAM = dung_luong_RAM
        self.dung_luong_o_cung = dung_luong_o_cung

    def tong_dung_luong(self):
        # Doi RAM tu MB sang GB roi cong voi o cung
        return (self.dung_luong_RAM / 1024) + self.dung_luong_o_cung

# =================================================================
# Nhap so luong may tinh
while True:
    try:
        n = int(input("Nhap so luong may tinh: "))

        if n > 0:
            break
        else:
            print("Vui long nhap so lon hon 0")

    except ValueError:
        print("Vui long nhap so nguyen")

# =================================================================
# Nhap danh sach may tinh
ds_mt = []
print("\n========== NHAP DANH SACH MAY TINH ==========")

for i in range(n):
    print(f"\nNhap may tinh thu {i + 1}:")

    ten_loai = input("Nhap ten loai chip: ")

    while True:
        try:
            dung_luong_RAM = float(
                input("Nhap dung luong RAM (MB): ")
            )

            if dung_luong_RAM > 0:
                break
            else:
                print("Vui long nhap dung luong lon hon 0")

        except ValueError:
            print("Vui long nhap so")

    while True:
        try:
            dung_luong_o_cung = float(
                input("Nhap dung luong o cung (GB): ")
            )

            if dung_luong_o_cung > 0:
                break
            else:
                print("Vui long nhap dung luong lon hon 0")

        except ValueError:
            print("Vui long nhap so")

    may_tinh = MayTinh(
        ten_loai,
        dung_luong_RAM,
        dung_luong_o_cung
    )

    ds_mt.append(may_tinh)

# =================================================================
# In danh sach may tinh vua nhap
print("\n========== DANH SACH MAY TINH ==========")

for i, may_tinh in enumerate(ds_mt):
    print(f"\nMay tinh thu {i + 1}:")
    print("Loai chip:", may_tinh.ten_loai)
    print("Dung luong RAM:", may_tinh.dung_luong_RAM, "MB")
    print("Dung luong o cung:", may_tinh.dung_luong_o_cung, "GB")
    print("Tong dung luong:",round(may_tinh.tong_dung_luong(), 2), "GB") 
# =================================================================
# Tach thanh 2 danh sach:
# - May tinh dung chip Intel
# - May tinh khong dung chip Intel
ds_intel = []
ds_khong_intel = []

for may_tinh in ds_mt:
    if "intel" in may_tinh.ten_loai.lower():
        ds_intel.append(may_tinh)
    else:
        ds_khong_intel.append(may_tinh)

# =================================================================
# In danh sach may tinh dung chip Intel
print("\n========== MAY TINH DUNG CHIP INTEL ==========")

if len(ds_intel) == 0:
    print("Khong co may tinh dung chip Intel")
else:
    for i, may_tinh in enumerate(ds_intel):
        print(f"\nMay tinh thu {i + 1}:")
        print("Loai chip:", may_tinh.ten_loai)
        print("Dung luong RAM:", may_tinh.dung_luong_RAM, "MB")
        print("Dung luong o cung:", may_tinh.dung_luong_o_cung, "GB")

# =================================================================
# In danh sach may tinh khong dung chip Intel
print("\n========== MAY TINH KHONG DUNG CHIP INTEL ==========")
if len(ds_khong_intel) == 0:
    print("Khong co may tinh khong dung chip Intel")
else:
    for i, may_tinh in enumerate(ds_khong_intel):
        print(f"\nMay tinh thu {i + 1}:")
        print("Loai chip:", may_tinh.ten_loai)
        print("Dung luong RAM:", may_tinh.dung_luong_RAM, "MB")
        print("Dung luong o cung:", may_tinh.dung_luong_o_cung, "GB")

# =================================================================
# Tim dung luong RAM nho nhat
obj_ram_min = min(ds_mt, key=lambda x: x.dung_luong_RAM)
ram_min = obj_ram_min.dung_luong_RAM

# In truc tiep cac may tinh co RAM nho nhat
print("\n========== MAY TINH CO RAM NHO NHAT ==========")
print("Dung luong RAM nho nhat:", ram_min, "MB")

for i, may_tinh in enumerate(ds_mt):
    if may_tinh.dung_luong_RAM == ram_min:
        print(f"\nMay tinh thu {i+1}:")
        print("Loai chip:", may_tinh.ten_loai)
        print("Dung luong RAM:", may_tinh.dung_luong_RAM, "MB")
        print("Dung luong o cung:", may_tinh.dung_luong_o_cung, "GB")
