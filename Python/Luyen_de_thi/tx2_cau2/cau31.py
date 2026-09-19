class ConKien:
    def __init__(self, loai, nang_suat, thoi_gian):
        self.loai = loai
        self.nang_suat = nang_suat
        self.thoi_gian = thoi_gian

    def so_gram_tha_duoc(self):
        return self.nang_suat * self.thoi_gian

# ===================================================
while True:
    try:
        n = int(input("Nhap so luong con kien: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so luong > 0")
    except ValueError:
        print("Vui long nhap so")

ds_con_kien = []
print("\n========== NHAP DANH SACH CON KIEN ==========")
for i in range(n):
    print(f"\nNhap con kien thu {i+1}:")
    loai = input("Nhap loai: ")

    while True:
        try:
            nang_suat = float(input("Nhap nang suat (gram/phut): "))
            if nang_suat > 0:
                break
            else:
                print("Nang suat phai > 0")
        except ValueError:
            print("Vui long nhap so")

    while True:
        try:
            thoi_gian = float(input("Nhap thoi gian (phut): "))
            if thoi_gian > 0:
                break
            else:
                print("Thoi gian phai > 0")
        except ValueError:
            print("Vui long nhap so")

    ds_con_kien.append(ConKien(loai, nang_suat, thoi_gian))

# ========================================
print("\n========== DANH SACH CON KIEN ==========")
for i, con_kien in enumerate(ds_con_kien):
    print(f"\nCon kien thu {i+1}:")
    print(f"Loai: {con_kien.loai}")
    print(f"Nang suat: {con_kien.nang_suat} gram/phut")
    print(f"Thoi gian: {con_kien.thoi_gian} phut")
    print(f"So gram tha duoc: {con_kien.so_gram_tha_duoc()} gram")  

# Tim kien co nang suat kem nhat
con_kien_kem_nhat = min(ds_con_kien, key=lambda x: x.nang_suat)
for i, con_kien in enumerate(ds_con_kien):
    if con_kien.nang_suat == con_kien_kem_nhat.nang_suat:
        print(f"\nCon kien co nang suat kem nhat thu {i+1}:")
        print(f"Loai: {con_kien.loai}")
        print(f"Nang suat: {con_kien.nang_suat} gram/phut")
        print(f"Thoi gian: {con_kien.thoi_gian} phut")
        print(f"So gram tha duoc: {con_kien.so_gram_tha_duoc()} gram")

# Tinh tong so gram tha duoc
tong_gram = 0
for con_kien in ds_con_kien:
    tong_gram += con_kien.so_gram_tha_duoc()
print(f"\nTong so gram tha duoc cua tat ca con kien: {tong_gram} gram")
