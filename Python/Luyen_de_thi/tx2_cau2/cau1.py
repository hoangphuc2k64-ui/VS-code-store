class HinhTuGiac:
    def __init__(self, a, b, c, d):
        self.a = a 
        self.b = b
        self.c = c
        self.d = d
    def tinh_chu_vi(self):      # tinh chu vi hinh tren
        return (self.a + self.b + self.c + self.d)
    def find_max(self):         # tim canh lon nhat 
        return max(self.a, self.b, self.c, self.d)
    
# ======================================================
while True:
    try:
        n = int(input("Nhap so luong hinh tu giac: "))
        if n > 0:
            break
        else:
            print("Nhap so luong > 0 !")
    except ValueError:
        print("Vui long nhap chinh xac !")

# ======================================================
ds_tugiac = []
for i in range(n):
    canh = []
    print(f"\n=== Nhap canh tu giac {i+1} ===")
    for ten in ["a", "b", "c", "d"]:
        while True:
            try:
                canh.append(float(input(f"Nhap canh {ten} cua tu giac thu {i+1} = ")))
                break
            except ValueError:
                print("Vui long nhap chinh xac !")

    a, b, c, d = canh
    tugiac = HinhTuGiac(a, b, c, d)
    ds_tugiac.append(tugiac)

# ======================================================
# in chu vi va tim canh 
print("\n==== Danh sach tu giac ====")
for i, tugiac in enumerate(ds_tugiac):
    print(f"\nTu giac {i + 1}:")
    print("a =", tugiac.a)
    print("b =", tugiac.b)
    print("c =", tugiac.c)
    print("d =", tugiac.d)

    print("=> Chu vi =", tugiac.tinh_chu_vi())
    print("=> Canh lon nhat =", tugiac.find_max())

# in chu vi min trong list tu giác
tugiac_min = ds_tugiac[0]
for tugiac in ds_tugiac:
    if tugiac.tinh_chu_vi() < tugiac_min.tinh_chu_vi():
        tugiac_min = tugiac

print("\n========== HINH CO CHU VI NHO NHAT ==========")
print("Chu vi nho nhat =", tugiac_min.tinh_chu_vi())
print("Cac canh:",tugiac_min.a, tugiac_min.b, tugiac_min.c, tugiac_min.d)