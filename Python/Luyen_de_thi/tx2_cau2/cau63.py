
class DienThoai:
    def __init__(self, name, os, unit_price, quantity):
        self.name = name
        self.os = os
        self.unit_price = unit_price
        self.quantity = quantity
    def total_amount(self):
        return (self.unit_price * self.quantity)

# =====================================================
ds_dienthoai = []
while True:
    try:
        n = int(input("Nhap so luong dien thoai: "))
        if n > 0:
            break
        else:
            print("Nhap so luong lon hon 0 !")
    except ValueError:
        print("Vui long nhap so nguyen !")

for i in range(n):
    print(f"\nNhap dien inf dien thoai thu {i+1}")
    # name
    name = input("Nhap ten dien thoai: ")

    # he dieu hanh
    os = input("Nhap he dieu hanh: ")

    # don gia
    while True:
        try:
            unit_price = float(input("Nhap don gia: "))
            if unit_price > 0:
                break
            else:
                print("Nhap don gia lon hon 0 !")
        except ValueError:
            print("Vui long nhap so !")

    # so luong 
    while True:
        try:
            quantity = int(input("Nhap so luong: "))
            if quantity >= 0:
                break
            else:
                print("Nhap so luong >= 0 !")
        except ValueError:
            print("Vui log nhap so nguyen !")

    # add list 
    ds_dienthoai.append(DienThoai(name, os, unit_price, quantity))

# ======================================================
print("======= Danh sach dien thoai ban dau =======")
for i, dienthoai in enumerate(ds_dienthoai):
    print(f"\nDien thoai thu {i+1}: ")
    print("=> Ten: ", dienthoai.name)
    print("=> He dieu hanh: ", dienthoai.os)
    print("=> Don gia: ", dienthoai.unit_price)
    print("=> So luong: ", dienthoai.quantity)
    print("=> Tong chi phi: ", dienthoai.total_amount())

# ======================================================
ds_Android = []         # tao list con de khong anh huong list cha
for dienthoai in ds_dienthoai:
    if dienthoai.os == "Android" or dienthoai.os == "android":
        ds_Android.append(dienthoai)
tuple_Android = tuple(ds_Android)

for i, dienthoai in enumerate(tuple_Android):
    print(f"\nDien thoai thu {i+1}: ")
    print("=> Ten: ", dienthoai.name)
    print("=> He dieu hanh: ", dienthoai.os)
    print("=> Don gia: ", dienthoai.unit_price)
    print("=> So luong: ", dienthoai.quantity)
    print("=> Tong chi phi: ", dienthoai.total_amount())

# ======================================================
ds_soluong_bang0 = []
for dienthoai in ds_dienthoai:
    if dienthoai.quantity == 0:
        ds_soluong_bang0.append(dienthoai)

print("\n=> So dien thoai co so luong mua = 0: ",len(ds_soluong_bang0))

for dienthoai in ds_soluong_bang0:
    ds_dienthoai.remove(dienthoai)

print("\n===== Danh sach sau khi xoa nhung dien thoai sl = 0 =====")
for i, dienthoai in enumerate(ds_dienthoai):
    print(f"\nDien thoai thu {i+1}: ")
    print("=> Ten: ", dienthoai.name)
    print("=> He dieu hanh: ", dienthoai.os)
    print("=> Don gia: ", dienthoai.unit_price)
    print("=> So luong: ", dienthoai.quantity)
    print("=> Tong chi phi: ", dienthoai.total_amount())



