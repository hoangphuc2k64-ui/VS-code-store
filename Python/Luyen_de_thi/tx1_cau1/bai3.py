import ham_all
list_int3 = []
while True:
    try:
        x = input("Nhap so nguyen: ")
        if x == "t":
            break
        so = int(x)
        list_int3.append(so)
    except ValueError:
        print("Vui long nhap chinh xac !")

# in ra dictionary co values la can bac 2 cua key
dict3 = ham_all.create_dict3(list_int3)
print("Dictionary: ", dict3)

# in ra tuple chua tong cac so chan va le trong list
tuple3 =  [ham_all.tong_chan(list_int3), ham_all.tong_le(list_int3)]
print("Tuple chua tong cac so chan va le: ", tuple(tuple3))

