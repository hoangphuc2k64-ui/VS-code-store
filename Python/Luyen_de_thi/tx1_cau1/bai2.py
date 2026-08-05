import ham_all

list2 = []
while True:
    try:
        x = input("Nhap so nguyen: ")
        if x == "t":
            break
        so = int(x)
        list2.append(so)
    except ValueError:
        print("Vui long nhap chinh xac !")
        
# in ra tuple chua list vua nhap
tuple2 = ham_all.create_tuple2(list2)
print("Tuple: ", tuple2)

# in ra tuple chua cac so nguyen to trong list
list_prime = []
for x in list2:
    if ham_all.check_prime2(x):
        list_prime.append(x)
tuple_prime = tuple(list_prime)
print("Tuple chua so nguyen to: ", tuple_prime)        
