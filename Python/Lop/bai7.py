from ham import tim_key, tim_ten
while True:
    try:
        n = int(input("Nhap so sinh vien: "))
        if int(n) == n:
            break
        else:
            print("Nhap so nguyen > 0")
    except ValueError:
        print("Vui long nhap chinh xac !")

# =======================================================================
ds = {}
for i in range(n):
    # nhap key
    while True:
        try:
            key = int(input(f"Nhap 'KEY' sinh vien thu {i+1}: "))
            if int(key) == key:
                break
            else:
                print("Nhap so nguyen > 0")
        except ValueError:
            print("Vui long nhap chinh xac !")
    
    # nhap ten
    ten = input(f"Nhap 'TEN' sinh vien thu {i+1}: ") 

    # add dict
    ds[key] = ten       

# ==========================================================================

print("\n============ Tim sinh vien ===========")
while True:
    try:
        k = int(input("Nhap 'KEY' can tim "))
        if int(k) == k:
            break
        else:
            print("Nhap so nguyen > 0")
    except ValueError:
        print("Vu long nhap chinh xac !")
print("=> Ten sinh vien: ", tim_ten(ds, k))

ten = input("Nhap 'TEN' can tim: ")
print("=> Key: ", tim_key(ds, ten))