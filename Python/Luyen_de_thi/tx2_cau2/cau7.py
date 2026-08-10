import math

class TamGiacDeu:
    def __init__(self, canh):
        self.canh = canh

    def tinh_duong_cao(self):
        return (self.canh * math.sqrt(3) /2)

    def tinh_dien_tich(self):
        return (math.sqrt(3)* (self.canh **2) /4)

    def tinh_chu_vi(self):
        return (3 *self.canh) 

# ========================================================
while True:
    try:
        n = int(input("Nhap so luong tam giac deu: "))
        if n > 0:
            break
        else:
            print("Nhap so lon hon 0 !")
    except ValueError:
        print("Vui long nhap chinh xac !")

# ========================================================
ds_tam_giac_deu = []
for i in range(n):
    print(f"Nhap canh tam giac deu thu {i+1}:")
    while True:
        try:
            x = float(input("Nhap canh: "))
            if x > 0:
                break
            else:
                print("Nhap canh lon hon 0 !")
        except ValueError:
            print("Vui long nhap chinh xac !")
    ds_tam_giac_deu.append(TamGiacDeu(x))

# ========================================================
# in 1
for i, tam_giac_deu in enumerate(ds_tam_giac_deu):
    print(f"\nTam giac deu thu {i+1}: ")
    print("Canh = ", tam_giac_deu.canh)
    print("=> Duong cao = ", tam_giac_deu.tinh_duong_cao())

# in 2: tong dien tich
tong_dt = 0
for tam_giac_deu in ds_tam_giac_deu:
    tong_dt = tong_dt + tam_giac_deu.tinh_dien_tich()
print("\n=> Tong dien tich = ", tong_dt)

# in 3: tim chu vi min
tam_giac_deu_min = ds_tam_giac_deu[0]
for tam_giac_deu in ds_tam_giac_deu:
    if tam_giac_deu_min.tinh_chu_vi() > tam_giac_deu.tinh_chu_vi():
        tam_giac_deu_min = tam_giac_deu
print("\n=> Chu vi min = ", tam_giac_deu_min.tinh_chu_vi())





