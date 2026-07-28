import ham
print("\n====== Nhap toa do 3 diem trong khong gian ========")

def nhap_so(x):
    while True:
        try:
            n = float(input(x))
            return n
        except ValueError:
            print("Vui long nhap lai !")
            continue

x1 = nhap_so("Nhap toa do truc hoanh diem 1: ")
y1 = nhap_so("Nhap toa do truc tung diem 1: ")
x2 = nhap_so("Nhap toa do truc hoanh diem 2: ")
y2 = nhap_so("Nhap toa do truc tung diem 2: ")
x3 = nhap_so("Nhap toa do truc hoanh diem 3: ")
y3 = nhap_so("Nhap toa do truc tung diem 3: ")

a = ham.khoangcach(x1, y1, x2, y2)
b = ham.khoangcach(x2, y2, x3, y3)
c = ham.khoangcach(x1, y1, x3, y3)


print("\n======= Tinh chu vi va dien tich =======")
if ham.kiemtra_tamgiac(a, b, c):
    print("Chu vi:", ham.chuvi(a, b, c))
    print("Diện tích:", ham.dientich(a, b, c))
else:
    print("Không tạo thành tam giác")