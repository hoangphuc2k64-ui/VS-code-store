while True:
    try:
        n = int(input("Nhap so nguyen duong: "))
        if n > 0:
            break
        else:
            print("Vui long nhap so lon hon 0")
    except ValueError:
        print("Vui long nhap so nguyen !")

ds = []
for i in range(0, n+1):
    if int(i**(1/3)) == i**(1/3):
        ds.append(i)
        print(i, "=> la so co the khai can bac 3")
    else:
        print(i, "=> la so khong the khai can bac 3")
    
print(ds)