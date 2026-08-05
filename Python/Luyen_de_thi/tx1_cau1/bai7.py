import ham_all

list_float7 = []
while True:
    x = input("Nhap so thuc: ")
    if x == 't':
        break
    try:
        list_float7.append(float(x))
    except ValueError:
        print("Vui long nhap chinh xac !")

print("\n======= Ket qua =======")
# in ra dict co key la so luong cac so am/ dg va value la tong am /dg
d7 = ham_all.create_dict7(list_float7)
print("=> Dictionary: ", d7)

tong_am, tong_dg = ham_all.tong_am_dg(list_float7)
t = tuple([tong_am, tong_dg])
print("Tuple: ", t)