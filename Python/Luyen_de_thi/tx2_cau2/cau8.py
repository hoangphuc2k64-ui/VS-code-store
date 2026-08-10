class HinhHopChuNhat:
    def __init__(self, a, b, h):
        self.a = a
        self.b = b
        self.h = h

    def tinh_S_xung_quanh(self):
        return (2 *(self.a + self.b) *self.h)

    def tinh_the_tich(self):
        return (self.a * self.b * self.h)

# ====================================================
while True:
    try:
        n = int(input("Nhap so luong hinh: "))
        if n > 0:
            break
        else:
            print("Nhap so lon hon 0")
    except ValueError:
        print("Vui long nhap chinh xac !")

# ====================================================
ds_hinh = []
for i in range(n):
    canh = []
    print(f"\nNhap canh cua hinh hop chu nhat thu {i+1}: ")
    for ten in ["a", "b", "h"]:
        while True:
            try:
                x = float(input(f"Nhap {ten}: "))
                if x > 0:
                    canh.append(x)
                    break
                else:
                    print("Nhap so lon hon 0")
            except ValueError:
                print("Vui long nhao chinh xac !")
    a, b, h = canh
    ds_hinh.append(HinhHopChuNhat(a, b, h))

# ====================================================
# in 1
for i, hhcn in enumerate(ds_hinh):
    print(f"\nHinh hop chu nhat thu {i+1}: ")
    print("Canh a = ", hhcn.a)
    print("Canh b = ", hhcn.b)
    print("Canh h = ", hhcn.h)
    print("=> Dien tich xung quanh = ", hhcn.tinh_S_xung_quanh())

# in 2: tong the tich cua n hinh
tong_V = 0
for hhcn in ds_hinh: 
    tong_V = tong_V + hhcn.tinh_the_tich()
print("\n=> Tong the tich cua n hinh = ", tong_V)

# in 3: tim V max
hhcn_max = ds_hinh[0]
for hhcn in ds_hinh:
    if hhcn_max.tinh_the_tich() < hhcn.tinh_the_tich():
        hhcn_max = hhcn
print("\n=> Hinh co the tich lon nhat = ", hhcn_max.tinh_the_tich())


