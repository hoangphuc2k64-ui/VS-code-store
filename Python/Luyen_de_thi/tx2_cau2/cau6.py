import math

class TamGiacVuong:
    def __init__(self, canh_vuong1, canh_vuong2):
        self.canh_vuong1 = canh_vuong1
        self.canh_vuong2 = canh_vuong2

    def tinh_canh_huyen(self):      # de yeu cau viet phuong thuc
        return math.sqrt(self.canh_vuong1 **2 + self.canh_vuong2 **2)

    def tinh_dien_tich(self):
        return (self.canh_vuong1 * self.canh_vuong2) /2

    def tinh_chu_vi(self):
        return (self.canh_vuong1 + self.canh_vuong2 + self.tinh_canh_huyen())

# ====================================================
while True:
    try:
        n = int(input("Nhap so luong hinh: "))
        if n > 0:
            break
        else:
            print("Nhap so lon hon 0 !")
    except ValueError:
        print("Vui long nhap so nguyen !")

# ====================================================
ds_tg_vuong = []
for i in range(n):
    print(f"\nNhap tam giac vuong thu {i+1}: ")
    canh = []
    for ten in ["canh_vuong1", "canh_vuong2"]:
        while True:
            try: 
                x = float(input(f"Nhap {ten}: "))
                if x > 0:
                    canh.append(x)
                    break
                else:
                    print("Nhap canh lon hon 0 !")
            except ValueError:
                print("Vui long nhap chinh xac !")

    canh_vuong1, canh_vuong2 = canh
    ds_tg_vuong.append(TamGiacVuong(canh_vuong1, canh_vuong2))

# ====================================================
# in 1
for i, tam_giac_vuong in enumerate(ds_tg_vuong):
    print(f"\nTam giac vuong thu {i+1}: ")
    print("Canh vuong 1 = ", tam_giac_vuong.canh_vuong1)
    print("Canh vuong 2 = ", tam_giac_vuong.canh_vuong2)
    print("=> Canh huyen = ", tam_giac_vuong.tinh_canh_huyen())
    print("=> Chu vi = ", tam_giac_vuong.tinh_chu_vi())

# in 2: tong dien tich
tong_dt = 0
for tam_giac_vuong in ds_tg_vuong:
    tong_dt = tong_dt + tam_giac_vuong.tinh_dien_tich()
print("\n=> Tong dien tich = ", tong_dt)

# in 3: tim chu vi lon nhat
tam_giac_vuong_max = ds_tg_vuong[0]
for tam_giac_vuong in ds_tg_vuong:
    if tam_giac_vuong_max.tinh_chu_vi() < tam_giac_vuong.tinh_chu_vi():
        tam_giac_vuong_max = tam_giac_vuong
print("\n=> Tam giac vuong co chu vi lon nhat: ", tam_giac_vuong_max.tinh_chu_vi())

    

    
    