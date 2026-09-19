import math

class SoNguyen:
    def __init__(self, x):
        self.x = x

    def check_chan_le(self):
        if self.x %2 == 0:
            return True         # so chan
        return False            # so le

    def check_snt(self):
        if self.x < 2:
            return False
        for i in range(2, self.x):
            if self.x %i == 0:
                return False
        return True

    def check_scp(self):
        if self.x < 0:
            return False
        else:
            if int(math.sqrt(self.x)) **2 == self.x:
                return True
            else:
                return False

# =========================================================
while True:
    try:
        n = int(input("Nhap so luong so nguyen: "))
        if n > 0:
            break
        else:
            print("Nhap so lon hon 0")
    except ValueError:
        print("Vui long nhap chinh xac !")

# ==========================================================
ds_so_nguyen = []
for i in range(n):
    while True:
        try:
            x = int(input("Nhap so nguyen: "))
            ds_so_nguyen.append(SoNguyen(x))
            break
        except ValueError:
            print("Vui long nhap so !") 

# ==========================================================
# in 1: in ra so chan
print("\n=> Cac so chan: ")
for sn in ds_so_nguyen:
    if sn.check_chan_le() is True:
        print(sn.x)

# in 2: in ra tong chinh phuong
tong_cp = 0
for sn in ds_so_nguyen:
    if sn.check_scp() is True:
        tong_cp = tong_cp + sn.x
print("\n=> Tong so chinh phuong = ", tong_cp)

# in 3
snt_max = None
for sn in ds_so_nguyen:
    if sn.check_snt():
        if snt_max == None:
            snt_max = sn.x
        elif sn.x > snt_max:
            snt_max = sn.x
if snt_max == None:
    print("Khong co so nguyen to trong danh sach.")
else:
    print("So nguyen to lon nhat =", snt_max)            





