class SoNguyen:
    def __init__(self, x):
        self.x = x
    def check_am_duong(self):
        if self.x > 0:
            return True 
        elif self.x < 0: 
            return False
        else:
            return None
        
    def check_so_ht(self):
        if self.x <= 0:
            return False
        else:
            tong = 0
            for i in range(1, self.x):
                if self.x % i == 0:
                    tong = tong + i
            if self.x == tong:
                return True
            else:
                return False
            
    def check_so_dx(self):
        if self.x < 0:
            return False
        else:
            store = self.x
            temp = self.x
            so_dao = 0

            while temp > 0:
                so_dao = so_dao *10 + temp %10
                temp = temp // 10

            if so_dao == store:
                return True
            else:
                return False

# ======================================================
ds_sn = []
while True:
    try:
        n = int(input("Nhap so luong so nguyen: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so > 0 !")
    except ValueError:
        print("Vi long nhap so !")

print("\n========= Nhap ")
for i in range(n):
    while True:
        try:
            x = int(input(f"Nhap so nguyen thu {i+1}: "))
            break
        except ValueError:
            print("Vui long nhap so !")

    # add list 
    ds_sn.append(SoNguyen(x))

# ====================================================
print("\n======= Danh sach so duong =======")
for i, sn in enumerate(ds_sn):
    if sn.check_am_duong() is True:
        print("So duong: ", sn.x)

# ====================================================
print("\n======= Tong cac so hoan thien =======")
tong_ht = 0
for sn in ds_sn:
    if sn.check_so_ht() is True:
        tong_ht = tong_ht + sn.x
print("Tong cac so hoan thien: ", tong_ht)

# ====================================================
ds_dx = []
for sn in ds_sn:
    if sn.check_so_dx() is True:
        ds_dx.append(sn)
if len(ds_dx) > 0:
    so_dx_max = max(ds_dx, key=lambda sn: sn.x)
    print("\n=> So dx max la:", so_dx_max.x)
else:
    print("\n=> Khong co so doi xung")