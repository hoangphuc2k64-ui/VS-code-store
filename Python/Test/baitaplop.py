# ============================================================
class nhanvien:
    def __init__(self, ten, namsinh, namcongtac):
        self.ten = ten
        self.namsinh = namsinh
        self.namcongtac = namcongtac

    def tinhtuoi(self):
        return (2026-self.namsinh)
    def tinhnamcongtac(self):
        return (2026 - self.namcongtac)
    def tennhanvien(self):
        return self.ten
    
# ============================================================ 
class chuyenvien(nhanvien):
    def __init__(self, ten, namsinh, namcongtac, trinhdo, luongcoban):
        super().__init__(ten, namsinh, namcongtac)
        self.trinhdo = trinhdo
        self.luongcoban = luongcoban
    
    def heso(self):
        if self.trinhdo == "Tien si":
            return 5
        elif self.trinhdo == "Thac si":
            return 4
        elif self.trinhdo == "Dai hoc":
            return 3
        elif self.trinhdo == "Cao dang":
            return 2
        return 0
    
    def tinhluong(self):
        return self.tinhnamcongtac() * self.heso() * self.luongcoban
    

# ===========================================================
class congnhan(nhanvien):
    def __init__(self, ten, namsinh, namcongtac, luongcoban):
        super().__init__(ten, namsinh, namcongtac)
        self.luongcoban = luongcoban
    
    def tinhluong(self):
        return self.tinhnamcongtac() * self.luongcoban
    
# ==========================================================
ds_cv = []
ds_cn = []
tong_luong = 0

for i in range(5):
    print(f"Nhap chuyen vien thu {i+1}: ")
    ten = input("Ten: ")
    namsinh = int(input("Nam sinh: "))
    namcongtac = int(input("Nam cong tac: "))
    trinhdo = input("Trinh do: ")
    luongcoban = int(input("Nhap luong co ban cua chuyen vien: "))
    ds_cv.append(chuyenvien(ten, namsinh, namcongtac, trinhdo, luongcoban))

for i in range(2):
    print(f"Nhap cong nhan thu {i+1}: ")
    ten = input("Ten: ")
    namsinh = int(input("Nam sinh: "))
    namcongtac = int(input("Nam cong tac: "))
    luongcoban = int(input("Luong co ban cua cong nhan: "))
    ds_cn.append(congnhan(ten, namsinh, namcongtac, luongcoban))

print("==== Danh sach chuyen vien ====")
for x in ds_cv:
    luong = x.tinhluong()
    tong_luong += luong
    print(x.ten, "- Luong:", luong)

print("\n==== Danh sach Cong Nhan ====")
for y in ds_cn:
    luong = y.tinhluong()
    tong_luong += luong
    print(y.ten, "- Luong:", luong)

print("\nTong luong cua tat ca nhan vien:", tong_luong)
