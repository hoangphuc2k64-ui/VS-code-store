import ham
while True:
    try:
        n = int(input("Nhap so luong phan tu: "))
        if n>0:
            break
        else:
            print("Nhap so luong lon hon 0 !")
    except ValueError:
        print("Vui long nhap chinh xac !")

list = []
for i in range(n):
    a = ham.nhap_so_float(f"Nhap so thuc thu {i+1}: ")
    list.append(a)


print("\n====== Danh sach so thuc ======")
print(list)

print("=> so so duong: ",ham.dem_dg(list))
print("=> so so am: ",ham.dem_am(list))
print("=> tbc so duong = ", ham.tong_dgcn(list) / ham.dem_dg(list))
print("=> tbc so am = ", ham.tong_am(list) / ham.dem_am(list))



