# Ham nhap so int
def nhap_so_int(a):    
    while True:
        try: 
            n = int(input(a))
            return n
        except ValueError:
            print("Vui long nhap chinh xac !")
            continue

# ham nhap so float
def nhap_so_float(x):
    while True:
        try:
            n = float(input(x))
            return n
        except ValueError:
            print("Vui long nhap chinh xac !")

# =============================================================
# ham dem so dg 
def dem_dg(x):       # x = list
    check_lonhon0 = 0
    for i in x:
        if i > 0:
            check_lonhon0 = check_lonhon0 + 1
    return check_lonhon0

# ham tinh tong so duong
def tong_dg(x):
    total_dg = 0
    for i in x:
        if i > 0:
            total_dg = total_dg + i
    return total_dg

# ham dem so am
def dem_am(x):       # x = list
    check_nhohon0 = 0
    for i in x:
        if i < 0:
            check_nhohon0 = check_nhohon0 + 1
    return check_nhohon0   

# ham tinh tong so am
def tong_am(x):
    total_am = 0
    for i in x:
        if i < 0:
            total_am = total_am + i
    return total_am
 # ============================================================