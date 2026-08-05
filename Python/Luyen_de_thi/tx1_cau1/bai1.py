import ham_all
list_int = []
while True:
    try:
        x = input("Nhap so nguyen: ")
        if x == "t":
            break
        so = int(x)     # input khong dinh dang thi se la str va khong the ép str thành int nên nó lỗi
        list_int.append(int(so))
    except ValueError:
        print("Khong phai so nguyen hop le!")

# in ra dictionary co values la binh phuong cua key
dict1 = ham_all.create_dict1(list_int)
print("Dictionary: ", dict1)

# in ra cac so nguyen to trong list
for x in list_int:
    if ham_all.check_prime(x):
        print("So nguyen to:", x)
