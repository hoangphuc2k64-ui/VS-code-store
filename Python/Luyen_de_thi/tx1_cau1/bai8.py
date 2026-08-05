import ham_all

while True:
    try:
        a = float(input('Nhap a = '))
        b = float(input('Nhap b = '))
        c = float(input('Nhap c = '))
        d = float(input('Nhap d = '))
        break
    except ValueError:
        print("Vui long nhap chinh xac !")

list8 = [(a, b, c), (a, b, d), (a, c, d), (b, c, d)]

for x, y, z in list8:
    if ham_all.check_tam_giac(x, y, z):
        kq = ham_all.tinh_P_S(x, y, z)
        print("Tuple: ", tuple(kq))

list_tuple = []
for x, y ,z in list8:
    if ham_all.check_tam_giac(x, y, z) is False:
        list_tuple.append((x, y, z))
print("To hop 3 so khong lap thanh tam giac: ", list_tuple)

