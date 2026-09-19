class PTb2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def nghiem(self):
        if self.a == 0:
            if self.b == 0:
                if self.c == 0:
                    return "Vo so nghiem"
                else:
                    return ()
            else:
                x = -self.c / self.b
                return (x,)

        delta = self.b ** 2 - 4 * self.a * self.c

        if delta < 0:
            return ()
        elif delta == 0:
            x = -self.b / (2 * self.a)
            return (x,)
        else:
            x1 = (-self.b + delta ** 0.5) / (2 * self.a)
            x2 = (-self.b - delta ** 0.5) / (2 * self.a)
            return (x1, x2)
        
# =========================================================
while True:
    try:
        n = int(input("Nhap so luong phuong trinh: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so luong > 0")
    except ValueError:
        print("Vui long nhap so")

ds_pt = []
print("\n========== NHAP DANH SACH PHUONG TRINH ==========")
for i in range(n):
    print(f"\nNhap phuong trinh thu {i+1}:")

    while True:
        try:
            a = float(input("Nhap a: "))
            if a != 0:
                break
            else:
                print("He so a phai khac 0")
        except ValueError:
            print("Vui long nhap so")

    while True:
        try:
            b = float(input("Nhap b: "))
            break
        except ValueError:
            print("Vui long nhap so")

    while True:
        try:
            c = float(input("Nhap c: "))
            break
        except ValueError:
            print("Vui long nhap so")

    pt = PTb2(a, b, c)
    ds_pt.append(pt)

# =========================================================
# In danh sach vua nhap
print("\n========== DANH SACH PHUONG TRINH ==========")

for i, pt in enumerate(ds_pt):
    print(f"\nPhuong trinh thu {i+1}:")
    print("a =", pt.a)
    print("b =", pt.b)
    print("c =", pt.c)

    kq = pt.nghiem()
    if len(kq) == 0:
        print("Vo nghiem")
    elif len(kq) == 1:
        print("Nghiem kep x =", kq[0])
    else:
        print("x1 =", kq[0])
        print("x2 =", kq[1])

# =========================================================
# Dem so phuong trinh vo nghiem
dem_vo_nghiem = 0
for pt in ds_pt:
    if len(pt.nghiem()) == 0:
        dem_vo_nghiem += 1
print("\nSo phuong trinh vo nghiem:", dem_vo_nghiem)

# =========================================================
# Dem so nghiem duong
dem_nghiem_duong = 0
for pt in ds_pt:
    kq = pt.nghiem()

    for x in kq:
        if x > 0:
            dem_nghiem_duong += 1
print("So nghiem duong:", dem_nghiem_duong)