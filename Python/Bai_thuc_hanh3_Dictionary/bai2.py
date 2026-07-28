import ham
while True:
    try:
        n = int(input("Nhap so luong phan tu: "))
        if n>0:
            break
        else:
            print("Vui long nhap so lon hon 0 !")
    except ValueError:
        print("Vui long nhap chinh xac !")

list =[]
for i in range(n):
    x = ham.nhap_so_int(f"Nhap so nguyenthu {i+1}: ")
    list.append(x)

# dictionary
binhphuong_key = {}
for i in range(n):
    binhphuong_key[list[i]] = (list[i] ** 2)

# dictionary co value la binh phuong cua key
print("Dictionary: ", binhphuong_key)