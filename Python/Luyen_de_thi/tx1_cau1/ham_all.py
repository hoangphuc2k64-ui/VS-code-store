# bai 1 ===========================================

# ham tao dictionary
def create_dict1(list_int):
    d1 = {}
    for i in list_int:
        d1[i] = i**2 
    return d1

# ham check 1 so nguyen to
def check_prime(x):
    if x < 2:
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True



# bai 2 ===========================================
# ham tao tuple (***)
def create_tuple2(list_int):
    return tuple(list_int)

# ham check 1 so nguyen to (bai 1 co roi)
def check_prime2(x):
    if x < 2:
        return False 
    for i in range(2, x):
        if x % i == 0:
            return False
    return True



# bai 3 ===========================================
# ham tao dictionary
import math
def create_dict3(list_int3):
    d3 = {}
    for x in list_int3:
        d3[x] = math.sqrt(x)
    return d3

# ham tong chan
def tong_chan(list_int3):
    tongchan = 0
    for x in list_int3:
        if x % 2 == 0:
            tongchan = tongchan + x
    return tongchan

def tong_le(list_int3):
    tongle = 0
    for x in list_int3:
        if x % 2 != 0:
            tongle = tongle + x
    return tongle



# bai 4 ===========================================
# ham tao dictionary
def create_dict4(list_int4):
    d4 ={}
    for x in list_int4:
        d4[x] = math.sqrt(x)
    return d4

#ham chek chinh phuong
def check_not_perfect_square(x):
    if x < 0:
        return False
    else:
        if (int(math.sqrt(x)) **2) == x:
            return False
        else:
            return True



# bai 5 ===========================================
# tao dict co values la cac so lien ke lon hon keys
def create_dict5(list_int5):
    d5 = {}
    for x in list_int5:
        d5[x] = x + 1
    return d5

# ham tinh giai thua
def tinh_giai_thua(x):
    gt = 1
    for i in range(1, x + 1):
        gt = gt * i
    return gt




# bai 6 ===========================================
# ham tinh tong tu 1 -> n
def tinh_tong(n):           # n la don gia tri
    tong = 0
    for x in range(1, n+1):
        tong = tong + x
    return tong

# ham tao dict key la int va value la tong cac so tu 1 den chinh nos
def create_dict6(list_int6):
    d6 = {}
    for x in list_int6:
        d6[x] = tinh_tong(x)
    return d6




# bai 7 ===========================================
# tong am va tong duong trong 1 list
def tong_am_dg(list):
    tong_am = 0
    tong_dg = 0
    for x in list:
        if x > 0:
            tong_dg = tong_dg + x
        elif x < 0: 
            tong_am = tong_am + x
    return tong_am, tong_dg

# tao dict gom key la so luong so am, dg trong 1 list value la tong am, duong trong list do
def create_dict7(list):
    d7 = {}
    count_am = 0
    count_dg = 0
    for x in list:
        if x > 0:
            count_dg = count_dg + 1
        elif x < 0:
            count_am = count_am + 1
    tong_am, tong_dg = tong_am_dg(list)
    d7[count_am] = tong_am      # 2 key khac nhau khong de ma theo thu tu 
    d7[count_dg] = tong_dg
    return d7



# bai 8 ===========================================
import math
# ham check 3 so co lap thanh 3 canh cua 1 tam giac khong
def check_tam_giac(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return True
    return False

# ham tinh chu vi va dien tich tam giac
def tinh_P_S(a, b, c):
    p = a + b + c
    p2 = p/2
    s = math.sqrt(p2 * (p2-a)*(p2-b)*(p2-c))
    return p, s


# bai 9 ===========================================
# ham tim so am lon nhat
def find_max_nega(list_float9):
    max_nega = float('-inf')
    for x in list_float9:
        if x < 0 and x > max_nega:
            max_nega = x
    if max_nega == float('-inf'):
        return None
    return max_nega

# ham tim so duong nho nhat
def find_min_pos(list_float9):
    min_pos = float('inf')
    for x in list_float9:
        if x > 0 and x < min_pos:
            min_pos = x
    if min_pos == float('inf'):
        return None
    return min_pos 

# ham tbc cac so duong va tbc cac so am  
def tbc_pos_neg(list_float9):
    sum_pos = 0
    count_pos = 0
    sum_nega = 0
    count_nega = 0
    for x in list_float9:
        if x > 0:
            sum_pos += x
            count_pos += 1
        elif x < 0:
            sum_nega += x
            count_nega += 1
    if count_nega > 0:
        tbc_nega = sum_nega / count_nega
    else:
        tbc_nega = None
    if count_pos > 0:
        tbc_pos = sum_pos / count_pos
    else:
        tbc_pos = None
    return tbc_nega, tbc_pos  



# bai 10  ====================================
# ham tao list co do dai 3 phan tu tu 4 phan tu
def create_tuple10(a, b, c, d):
    return tuple([(a,b,c), (a,b,d), (a,c,d), (b,c,d)])

# ham giai phuong trinh bac 2
def pt_bac2(a,b,c):
    if a == 0:
        return False
    delta = b**2 - (4*a*c)
    if delta > 0:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        return x1, x2
    return False
