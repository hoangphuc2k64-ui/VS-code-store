class ConGa:
    def __init__(self, loai, tuoi, gioitinh, socon):
        self.loai = loai
        self.tuoi = tuoi
        self.gioitinh = gioitinh
        self.socon = socon
    def tinh_so_trung(self):
        if self.loai.lower() == "ga ri":
            if self.gioitinh.lower() == "ga mai" and self.tuoi > 45:
                return (self.tuoi - 45) * self.socon
            return 0
        elif self.loai.lower() == "ga lai":
            if self.gioitinh.lower() == "ga mai" and self.tuoi > 30:
                return ((self.tuoi - 30) *2) * self.socon
            return 0
        else:
            if self.gioitinh.lower() == "ga mai" and self.tuoi > 35:
                return (self.tuoi - 35) * self.socon
            return 0

# ===============================================================
while True:
    try:
        n = int(input("Nhap so luong lua ga: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so > 0 !!")
    except ValueError:
        print("Vui long nhap chinh xac !!")

ds_ga = []
print("\n====================================================")
for i in range(n):
    print(f"\nNhap lua ga thu {i+1}: ")

    loai = input("Nhap loai cua lua ga: ")

    while True:
        try:
            tuoi = int(input("Nhap ngay tuoi cua lua ga: "))
            if tuoi > 0:
                break
            else:
                print("Vui long nhap so > 0 !!")
        except ValueError:
            print("Vui long nhap chinh xac !!")

    while True:
        gioitinh = input("Nhap gioi tinh cua lua ga: ")
        if gioitinh.lower() == "ga mai" or gioitinh.lower() == "ga trong":
            break
        else:
            print("Vui long nhap dung gioi tinh ga (mai / trong) !")

    while True:
        try:
            socon = int(input("Nhap so con trong lua ga: "))
            if socon > 0:
                break
            else:
                print("Vui long nhap so con > 0 !!")
        except ValueError:
            print("Vui long nhap so !")

    # add list 
    ds_ga.append(ConGa(loai, tuoi, gioitinh, socon))

# ======================================================================
print("\n=================================================")
print("=========== Danh sach dan ga ban dau ============")
for i, cg in enumerate(ds_ga):
    print(f"\nLua ga thu {i+1}: ")
    print("Loai: ", cg.loai)
    print("Ngay tuoi: ", cg.tuoi)
    print("Gioi tinh: ", cg.gioitinh)
    print("So con trong lua: ", cg.socon)
    print("So trung: ", cg.tinh_so_trung())

# ======================================================================
# Tong trung
tong_trung = 0
for cg in ds_ga:
    tong_trung = tong_trung + cg.tinh_so_trung()
print("\n=> Tong so trung ca dan da de = ", tong_trung)

# ======================================================================
# dem ga ri trong
ds_gari_trong = []
for cg in ds_ga:
    if cg.loai.lower() == "ga ri" and cg.gioitinh.lower() == "ga trong":
        ds_gari_trong.append(cg.socon)
print("\n=> So ga ri trong: ", sum(ds_gari_trong))          # len dem so thu tu tung thanh phan

# tong_ga_ri_trong = 0
# for cg in ds_ga:
#    if cg.loai.lower() == "ga ri" and cg.gioitinh.lower() == "ga trong":
#         tong_ga_ri_trong += cg.socon
# print("\n=> So ga ri trong:", tong_ga_ri_trong)

# dem tong trung ga ri
tong_trung_gari = 0
for cg in ds_ga:
    if cg.loai.lower() == "ga ri":
        tong_trung_gari = tong_trung_gari + cg.tinh_so_trung()
print("\n=> Tong so trung ga ri: ", tong_trung_gari)



