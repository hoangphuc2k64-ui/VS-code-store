import ham_all

list_int6 = []
while True:
    x = input("Nhap so nguyen: ")
    if x == "t":
        break
    try:
        so = int(x)
        list_int6.append(so)
    except ValueError:
        print("Vui long nhap chinh xac !")

print("\n===== Ket qua ======")
# dict co key la cac so int trong list
d6 = ham_all.create_dict6(list_int6)
print("Dictionary: ", d6)

# in ra tuple chua tong cac so tu 1 den tung so co trong list6
list_tong = []
for x in list_int6:
    list_tong.append(ham_all.tinh_tong(x)) 
t = tuple(list_tong)
print("Tuple chua tong cac so tu 1 den tung so co trong list6: ", t)
