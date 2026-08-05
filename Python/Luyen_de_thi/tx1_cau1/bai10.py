import ham_all

while True:
    try:
        a = float(input("Nhap a = "))
        b = float(input("Nhap b = "))
        c = float(input("Nhap c = "))
        d = float(input("Nhap d = "))
        break
    except ValueError:
        print("Vui long nhap chinh xac !")

t = ham_all.create_tuple10(a, b, c, d)
print("=> Tuple: ", t)

for x, y, z in t:
    kq = ham_all.pt_bac2(x, y, z)
    if kq is not False:
        print(f"{x}x^2 + {y}x + {z} = 0")
        print("Nghiem:", kq)

