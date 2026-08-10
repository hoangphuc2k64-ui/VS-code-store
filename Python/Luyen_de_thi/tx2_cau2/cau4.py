import math 
class HinhThangVuong:
    def __init__(self, day_lon, day_nho, chieu_cao):
        self.day_lon = day_lon
        self.day_nho = day_nho
        self.chieu_cao = chieu_cao
        # suy ra
        self.canh_ben = math.sqrt((self.day_lon - self.day_nho)**2 + self.chieu_cao **2)

    def tinh_chu_vi(self):
        return (self.day_lon + self.day_nho + self.chieu_cao + self.canh_ben)

    def tinh_dien_tich(self):
        return ((self.day_lon + self.day_nho) * self.chieu_cao /2)

# =====
while True:
    try:
        n = int(input("Nhap so luong hinh: "))
        if n > 0:
            break
        else:
            print("Nhap so luong > 0 !")
    except ValueError:
        print("Vui long nhap so nguyen !")

ds_htv = []
for i in range(n):
    canh = []
    print(f"\nNhap hinh thang vuong thu {i+1}: ")
    for ten in ["day_lon", "day_nho", "chieu_cao"]:
        while True:
            try:
                x = float(input(f"Nhap {ten} cua hinh thang vuong thu {i+1}: "))
                if x > 0:
                    canh.append(x)
                    break
                else:
                    print("Nhap so lon hon 0 !")
            except ValueError:
                print("Vui long nhap so !")
    day_lon, day_nho, chieu_cao = canh
    # check day lon nho
    if day_lon < day_nho:
        day_lon, day_nho = day_nho, day_lon

    ds_htv.append(HinhThangVuong(day_lon, day_nho, chieu_cao))

# ====
for i, htv in enumerate(ds_htv):
    print(f"\nHinh thang thu {i+1}: ")
    print("Day lon = ", htv.day_lon)
    print("Day_nho = ", htv.day_nho)
    print("Chieu cao = ", htv.chieu_cao)
    print("Canh ben = ", htv.canh_ben)
    print("=> Chu vi = ", htv.tinh_chu_vi())

sum_s = 0
for htv in ds_htv:
    sum_s = sum_s + htv.tinh_dien_tich()
print(f"\n=> Tong dien tich cua {n} hinh = ", sum_s)

htv_max = ds_htv[0]
for htv in ds_htv:
    if htv_max.tinh_dien_tich() < htv.tinh_dien_tich():
        htv_max = htv
print(f"\nHinh co dien tich lon nhat {htv_max.day_lon}, {htv_max.day_nho}, {htv_max.chieu_cao}, {htv_max.canh_ben}:", htv_max.tinh_dien_tich())


