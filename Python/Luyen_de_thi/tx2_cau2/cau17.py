import math

class PhuongTrinhBac2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    # Tim nghiem phuong trinh
    def tim_nghiem(self):
        delta = self.b**2 - 4*self.a*self.c

        if delta < 0:
            return ()

        elif delta == 0:
            x = -self.b / (2*self.a)
            return (x,)     # tuple nên de tam dau ','

        else:
            x1 = (-self.b + math.sqrt(delta)) / (2*self.a)
            x2 = (-self.b - math.sqrt(delta)) / (2*self.a)
            return (x1, x2)


# =====================================================
# Tao list gom 2 phuong trinh bac 2

ds_pt = []

for i in range(2):
    print(f"\nNhap phuong trinh thu {i+1}:")

    while True:
        try:
            a = float(input("Nhap a = "))
            if a != 0:
                break
            else:
                print("a phai khac 0 !")
        except ValueError:
            print("Vui long nhap so !")

    while True:
        try:
            b = float(input("Nhap b = "))
            c = float(input("Nhap c = "))
            break
        except ValueError:
            print("Vui long nhap so !")

    ds_pt.append(PhuongTrinhBac2(a, b, c))


# =====================================================
# In nghiem cua 2 phuong trinh

for i, pt in enumerate(ds_pt):
    nghiem = pt.tim_nghiem()    # important

    print(f"\nPhuong trinh thu {i+1}:")

    if len(nghiem) == 0:
        print("Phuong trinh vo nghiem")

    elif len(nghiem) == 1:
        print("Nghiem kep x =", nghiem[0])

    else:
        print("x1 =", nghiem[0])
        print("x2 =", nghiem[1])


# =====================================================
# Tao tuple chua tat ca nghiem

tuple_nghiem = ()

for pt in ds_pt:
    tuple_nghiem = tuple_nghiem + pt.tim_nghiem()

print("\nTuple cac nghiem:", tuple_nghiem)


# =====================================================
# Tim nghiem lon nhat

if len(tuple_nghiem) > 0:
    print("Nghiem lon nhat =", max(tuple_nghiem))
else:
    print("Hai phuong trinh deu vo nghiem")