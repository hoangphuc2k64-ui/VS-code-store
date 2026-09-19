class LuyThua:
    def __init__(self, x):
        self.x = x

    # Tinh binh phuong
    def tinh_binh_phuong(self):
        return self.x ** 2

    # Tinh lap phuong
    def tinh_lap_phuong(self):
        return self.x ** 3

    # Tinh giai thua
    def tinh_giai_thua(self):
        if self.x < 0:
            return None

        giai_thua = 1
        for i in range(1, self.x + 1):
            giai_thua = giai_thua * i

        return giai_thua


# =====================================================
# Nhap so luong

while True:
    try:
        n = int(input("Nhap so luong so nguyen: "))
        if n > 0:
            break
        else:
            print("Vui long nhap n > 0 !")
    except ValueError:
        print("Vui long nhap so nguyen !")


# =====================================================
# Tao list cac object LuyThua

ds = []

for i in range(n):
    while True:
        try:
            x = int(input(f"Nhap so nguyen thu {i+1}: "))
            ds.append(LuyThua(x))
            break
        except ValueError:
            print("Vui long nhap so nguyen !")


# =====================================================
# Tao dictionary
# key = so nguyen
# value = lap phuong cua so do

d = {}

for so in ds:
    d[so.x] = so.tinh_lap_phuong()

print("\nDictionary:", d)


# =====================================================
# In giai thua cac so

print("\n===== GIAI THUA =====")

for so in ds:
    if so.tinh_giai_thua() == None:
        print(so.x, ": Khong tinh duoc giai thua")
    else:
        print(so.x, "! =", so.tinh_giai_thua())


# =====================================================
# Tong lap phuong

tong_lap_phuong = 0

for so in ds:
    tong_lap_phuong = tong_lap_phuong + so.tinh_lap_phuong()

print("\nTong lap phuong =", tong_lap_phuong)