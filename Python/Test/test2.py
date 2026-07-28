class sinhvien:
    def __init__(self, hoten, namsinh, toan, van, ngoaingu):
        self.hoten = hoten
        self.namsinh = namsinh
        self.toan = toan
        self.van = van
        self.ngoaingu = ngoaingu

    def tong_diem(self):
        return self.toan + self.van + self.ngoaingu
    
ds = []
while True:
    try:
        n = int(input("Nhap so sinh vien: "))
        if n > 0:
            break
        else:
            print("Vui long nhap lon hon 0")
    except ValueError:
        print("Vui long nhap chinh xac !!")

for i in range(n):
    print(f"\nNhap sinh vien thu {i+1}: ")
    hoten = input("Ten: ")
    namsinh = int(input("Nam sinh: "))
    toan = float(input("Diem toan: "))
    van = float(input("Diem van: "))
    ngoaingu = float(input("Diem ngoai ngu: "))
    ds.append(sinhvien(hoten, namsinh, toan, van, ngoaingu))

# Sap xep tong diem
ds.sort(key=lambda sv: sv.tong_diem(), reverse=True)

# Danh sach sv
for sv in ds:
    print("=> Sinh vien: ", sv.hoten, "Nam sinh: ", sv.namsinh, "Toan: ", sv.toan, "Van: ", sv.van, "Ngoai ngu: ", sv.ngoaingu, "Overall: ", sv.tong_diem())

# Tbc
tong_toan = tong_van = tong_nn = 0
for sv in ds:
    tong_toan = tong_toan + sv.toan
    tong_van = tong_van + sv.van
    tong_nn = tong_nn + sv.ngoaingu

print("TBC toan: ", tong_toan/n)
print("TBC van: ", tong_van/n)
print("TBC ngoai ngu: ", tong_nn/n)
