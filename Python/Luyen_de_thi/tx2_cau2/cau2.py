import math

class HinhChuNhat:
    def __init__(self, dai, rong):
        self.dai = dai
        self.rong = rong

    def tinh_chu_vi(self):
        return ((self.dai + self.rong)*2)
    
    def tinh_dien_tich(self):
        return (self.dai * self.rong)
    
    def tinh_duong_cheo(self):
        return (math.sqrt(self.dai **2 + self.rong **2))

# ================ Nhap thong tin ===================
while True:
    n = int(input("Nhap so luong hinh chu nhat:" ))
    try:
        if n > 0:
            break
        else:
            print("Nhap so > 0 !")
    except ValueError:
        print("Vui long nhap chinh xac !")

ds_hcn = []
for i in range(n):
    canh = []
    print(f"\nNhap canh hinh chu nhat thu {i+1}: ")
    for ten in ["dai", "rong"]:
        while True:
            try:
                x = float(input(f"Nhap canh {ten} cua hcn thu {i+1}: "))
                if x > 0: 
                    canh.append(x)
                    break
                else:
                    print("Nhap canh > 0 !")
            except ValueError:
                print("Vui long nhap chinh xac !")
    dai, rong = canh
    ds_hcn.append(HinhChuNhat(dai, rong))

# ====================================
# in 
for i, hcn in enumerate(ds_hcn):        # enum return index and value, so we need 'i' and 'hcn'
    print(f"\nHinh chu nhat {i+1}: ")
    print("canh dai = ", hcn.dai)
    print("canh rong = ", hcn.rong)
    print("=> Chu vi: ", hcn.tinh_chu_vi())

# in 2
tong_dt = 0
for hcn in ds_hcn:
    tong_dt = tong_dt + hcn.tinh_dien_tich()
print("\n=> Tong dien tich: ", tong_dt)

# in 3
hcn_min = ds_hcn[0]
for hcn in ds_hcn:
    if hcn.tinh_duong_cheo() < hcn_min.tinh_duong_cheo():
        hcn_min = hcn

print("\nHinh chu nhat co duong cheo min: ")
print(f"Canh dai = {hcn_min.dai}, canh rong = {hcn_min.rong}")
print("=> Chu vi: ", hcn_min.tinh_chu_vi())
print("=> Dien tich: ", hcn_min.tinh_dien_tich())


