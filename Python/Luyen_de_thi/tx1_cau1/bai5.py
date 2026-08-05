import ham_all

list_int5 = []
while True:
    x = input("Nhap so nguyen: ")
    if x == "t":
        break
    try:
        so = int(x)
        list_int5.append(so)
    except ValueError:
        print("Vui long nhap chinh xac !") 

# in ra dictionary co value la so lien ke lon hon key
dict5 = ham_all.create_dict5(list_int5)
print("Dictionary: ", dict5)

# in ra tuple chua giai thua cac so nguyen to trong list_int5
list_giai_thua = []
for x in list_int5:
    if ham_all.check_prime(x):
        list_giai_thua.append(ham_all.tinh_giai_thua(x))

print("Tuple chua giai thua cac so nguyen to: ", tuple(list_giai_thua))
