import math

class TamGiac:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def tinh_chu_vi(self):
        return (self.a + self.b +self.c)

    def tinh_dien_tich(self):
        p = self.tinh_chu_vi() /2
        return math.sqrt(p *(p-self.a) *(p-self.b) *(p-self.c))

# =====================================================
while True:
    try:
        n = int(input("Nhap so luong hinh: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so lon hon 0 !")
    except ValueError:
        print("Vui long nhap chinh xac !")

# =====================================================
ds_tam_giac = []
for i in range(n):
    while True:
        canh = []
        print(f"\nNhap canh tam giac thu {i+1}: ")
        for ten in ["a", "b", "c"]:
            while True:
                try:
                    x = float(input(f"Nhap canh {ten}: "))
                    if x > 0:
                        canh.append(x)
                        break
                    else:
                        print("Nhap so lon hon 0 !")
                except ValueError:
                    print("Vui long nhap so !")
        a, b, c = canh
        if a+b>c and a+c>b and b+c>a:
            ds_tam_giac.append(TamGiac(a, b, c))
            break
        else:
            print("3 canh khong tao thanh tam giac. Nhap lai !")

# =====================================================
# in 1
for i, tam_giac in enumerate(ds_tam_giac):
    print(f"\nHinh tam giac thu {i+1}: ")             # dung i
    print(f"Canh {tam_giac.a} =", tam_giac.a)         # dung tam_giac
    print(f"Canh {tam_giac.b} =", tam_giac.b)         # dung tam_giac
    print(f"Canh {tam_giac.c} =", tam_giac.c)         # dung tam_giac
    print("=> Chu vi = ", tam_giac.tinh_chu_vi())     # dung tam_giac

# in 2
tong_dt = 0
for tam_giac in ds_tam_giac:
    tong_dt = tong_dt + tam_giac.tinh_dien_tich()
print("\n=> Tong dien tich: ", tong_dt)

# in 3
tam_giac_min = ds_tam_giac[0]
for tam_giac in ds_tam_giac:
    if tam_giac_min.tinh_dien_tich() > tam_giac.tinh_dien_tich():
        tam_giac_min = tam_giac
print("\n=> Dien tich nho nhat trong cac tam giac la: ", tam_giac_min.tinh_dien_tich())

