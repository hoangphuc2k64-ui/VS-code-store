import ham_all
list_int4 = []
while True:
    try:
        x = input("Nhap so nguyen: ")
        if x == "t":
            break
        so = int(x)
        list_int4.append(so)
    except ValueError:
        print("Vui long nhap chinh xac !")   

# in ra dictionary co values la can bac 2 cua key
dict4 = ham_all.create_dict4(list_int4)
print("Dictionary: ", dict4)

# in ra cac so khong phai la chinh phuong trong list
for x in list_int4:
    if ham_all.check_not_perfect_square(x):
        print("So khong phai chinh phuong: ", x)