import ham
while True:
    try:
        n = int(input("Nhap so luong phan tu: "))
        if n > 0:
            break
        else:
            print("Nhap so luong > 0")
    except ValueError:
        print("Vui long nhap chinh xac !")

list1 = []
list2 = []
for i in range(n):
    a = ham.nhap_so_int(f"Nhap phan tu thu {i+1} cua list1: ")
    b = ham.nhap_so_int(f"Nhap phan tu thu {i+1} cua list2: ")
    list1.append(a)
    list2.append(b)

all_key = {}
for i in range(n):
    all_key[list1[i]] = list2[i]

print("Dictionary: ", all_key)

