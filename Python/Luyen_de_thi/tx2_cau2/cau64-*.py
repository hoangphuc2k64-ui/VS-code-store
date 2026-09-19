import math
# ======================================== tao class
class DEMUX:
    def __init__(self, ten, so_bit_vao, so_bit_ra):
        self.ten = ten
        self.so_bit_vao = so_bit_vao
        self.so_bit_ra = so_bit_ra

    def tinh_so_duong_dieu_khien(self):
        return math.log2(self.so_bit_ra / self.so_bit_vao)

# ======================================== nhap n mach DEMUX
while True:
    try:
        n = int(input("Nhap so luong mach DEMUX: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so duong !")
    except ValueError:
        print("Vui long nhap so nguyen !")

ds_demux = []

for i in range(n):
    print(f"\nNhap mach DEMUX thu {i+1}: ")

    # ten
    ten = input("Nhap ten mach DEMUX thu: ")

    # so bit vao
    while True:
        try:
            so_bit_vao = int(input("Nhap so luong bit vao: "))
            if so_bit_vao > 0:
                break
            else:
                print("Vui long nhap so duong !")
        except ValueError:
            print("Vui long nhap so nguyen !")

    # so bit ra
    while True:
        try:
            so_bit_ra = int(input("Nhap so luong bit ra: "))
            if so_bit_ra >= so_bit_vao:
                break
            else:
                print("So bit ra phai >= so bit vao !")
        except ValueError:
            print("Vui long nhap so nguyen !")

    # add list 
    ds_demux.append(DEMUX(ten, so_bit_vao, so_bit_ra))


# ======================================== in ra danh sach vua nhap 
print("\n======= Danh sach demux ========")
for i, demux in enumerate(ds_demux):
    print(f"\nDEMUX thu {i+1}: ")
    print("Ten: ", demux.ten)
    print("So bit vao: ", demux.so_bit_vao)
    print("So bit ra: ", demux.so_bit_ra)
    print("So duong dieu khien: ", demux.tinh_so_duong_dieu_khien())

# ======================================== sxep demux giam dan theo bit dau ra
ds_demux.sort(key = lambda demux: demux.so_bit_ra, reverse= True)
print("\n======= Danh sach demux sau sap xep theo so bit ra ========")
for i, demux in enumerate(ds_demux):
    print(f"\nDEMUX thu {i+1}: ")
    print("Ten: ", demux.ten)
    print("So bit vao: ", demux.so_bit_vao)
    print("So bit ra: ", demux.so_bit_ra)
    print("So duong dieu khien: ", demux.tinh_so_duong_dieu_khien())

#  ======================================== tao tuple chua cac demux co nhieu duong dieu khien
# tao bien max
max_dk = ds_demux[0].tinh_so_duong_dieu_khien()
for demux in ds_demux:
    if max_dk < demux.tinh_so_duong_dieu_khien():
        max_dk = demux.tinh_so_duong_dieu_khien()

# demux_max = max(ds_demux, key=lambda demux: demux.tinh_so_duong_dieu_khien())
# max_dk = demux_max.tinh_so_duong_dieu_khien()

# so sanh voi gia tri max
ds_demux_max = []
for demux in ds_demux:
    if demux.tinh_so_duong_dieu_khien() == max_dk:
        ds_demux_max.append(demux)                  # append full cac tphan trong object

tuple_demux_max = tuple(ds_demux_max)
print("\n ========== Danh sach tuple co dg dieu khien nhieu nhat ==========")
for i, demux in enumerate(tuple_demux_max):
    print(f"\nDEMUX thu {i+1}: ")
    print("Ten: ", demux.ten)
    print("So bit vao: ", demux.so_bit_vao)
    print("So bit ra: ", demux.so_bit_ra)
    print("So duong dieu khien: ", demux.tinh_so_duong_dieu_khien())
