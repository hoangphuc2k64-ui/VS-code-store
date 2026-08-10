import math

class DuongThang:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def tinh_do_dai(self):
        return math.sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1) **2)

# ==================================================================
ds_duong_thang = []
for i in range(3):
    print(f"\nNhap toa do 2 diem cua duong thang thu {i+1}:")
    toa_do = []
    for ten in ["x1", "y1", "x2", "y2"]:
        while True:
            try:
                x = float(input(f"Nhap toa do diem {ten} = "))
                toa_do.append(x)
                break
            except ValueError:
                print("Vui long nhap so !")
    x1, y1, x2, y2 = toa_do
    ds_duong_thang.append(DuongThang(x1, y1, x2, y2))

# ==================================================================
for i, dt in enumerate(ds_duong_thang):
    print(f"\nDuong thang thu {i+1}: ")
    print(f"Toa do: A({dt.x1} , {dt.y1}) va B({dt.x2} , {dt.y2})")
    print("Do dai dt = ", dt.tinh_do_dai())

# in 2: check 3 doan thang co tao thanh tam giac khong ?
a = ds_duong_thang[0].tinh_do_dai()
b = ds_duong_thang[1].tinh_do_dai()
c = ds_duong_thang[2].tinh_do_dai()
if a+b>c and a+c>b and b+c>a:
    print("\n=> 3 doan thang co the lap thanh tam giac.")
else:
    print("\n=> 3 doan thang khong the lap thanh tam giac.")

# in 3: 
dt_max = ds_duong_thang[0]
for dt in ds_duong_thang:
    if dt_max.tinh_do_dai() < dt.tinh_do_dai():
        dt_max = dt
print("\n=> Doan co do dai lon nhat = ", dt_max.tinh_do_dai())


