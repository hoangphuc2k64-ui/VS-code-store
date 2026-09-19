class HinhHopChuNhat:
    def __init__(self, dai, rong, cao):
        self.dai = dai
        self.rong = rong
        self.cao = cao

    def dientich_tp(self):
        return (2*(self.dai * self.rong) + 2*(self.cao * self.dai) + 2*(self.rong * self.cao))

    def thetich(self):
        return self.cao * self.dai * self.rong

# ======================================================================
ds_hhcn = []
while True:
    try:
        n = int(input("Nhap so luong hinh hop chu nhat: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so > 0 !")
    except ValueError:
        print("Vui long nhap so !")

for i in range(n):
    print(f"\n===== Nhap thong so hinh thu {i+1} =====")
    while True:
        try:
            dai = float(input("Nhap do dai: "))
            if dai > 0:
                break
            else:
                print("Vui long nhap so > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    while True:
        try:
            rong = float(input("Nhap do rong: "))
            if rong > 0:
                break
            else:
                print("Vui long nhap so > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    while True:
        try:
            cao = float(input("Nhap chieu cao: "))
            if cao > 0:
                break
            else:
                print("Vui long nhap so > 0 !")
        except ValueError:
            print("Vui long nhap so !")

    ds_hhcn.append(HinhHopChuNhat(dai, rong, cao))

# ==================================================================
print("\n======================================================================")
print("====== Danh sach hinh hop chu nhat ======")
for i, hhcn in enumerate(ds_hhcn):
    print(f"\nHinh hop chu nhat thu {i+1}: ")
    print("Chieu cao: ", hhcn.cao)
    print("Chieu dai: ", hhcn.dai)
    print("Chieu rong: ", hhcn.rong)
    print("Dien tich toan phan: ", hhcn.dientich_tp())
    print("The tich: ", hhcn.thetich())

# ==================================================================
ds_thetich_lonhon50 = []
for hhcn in ds_hhcn:
    if hhcn.thetich() > 50:
        ds_thetich_lonhon50.append(hhcn)
tuple_thetich_lonhon50 = tuple(ds_thetich_lonhon50)
print("\n=> Tuple: ", tuple_thetich_lonhon50)

print("\n====== Tuple hinh hop chu nhat co the tich > 50 ======")
for i, hhcn in enumerate(tuple_thetich_lonhon50):
    print(f"\nHinh hop chu nhat thu {i+1}: ")
    print("Chieu cao: ", hhcn.cao)
    print("Chieu dai: ", hhcn.dai)
    print("Chieu rong: ", hhcn.rong)
    print("Dien tich toan phan: ", hhcn.dientich_tp())
    print("The tich: ", hhcn.thetich())

# ===================================================================
# sort 
ds_hhcn.sort(key= lambda hhcn: hhcn.thetich(), reverse= True)
print("\n====== Danh sach hinh hop chu nhat sau khi sap xep giam dan theo V ======")
for i, hhcn in enumerate(ds_hhcn):
    print(f"\nHinh hop chu nhat thu {i+1}: ")
    print("Chieu cao: ", hhcn.cao)
    print("Chieu dai: ", hhcn.dai)
    print("Chieu rong: ", hhcn.rong)
    print("Dien tich toan phan: ", hhcn.dientich_tp())
    print("The tich: ", hhcn.thetich())