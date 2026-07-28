def tim_ten(ds, key):
    if key in ds:
        return ds[key]
    return "Khong tim thay"

def tim_key(ds, ten):
    for key, value in ds.items():
        if value == ten:
            return key
    return "Khong tim thay"

# ===================================================================
import math

# Tính căn bậc 2
def canbac2(x):
    return math.sqrt(x)f

# Tính bình phương
def binhphuong(x):
    return x ** 2

# Tính khoảng cách giữa 2 điểm
def khoangcach(x1, y1, x2, y2):
    return canbac2(binhphuong(x2 - x1) + binhphuong(y2 - y1))

# Kiểm tra có tạo thành tam giác không
def kiemtra_tamgiac(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Tính chu vi
def chuvi(a, b, c):
    return a + b + c

# Tính diện tích (công thức Heron)
def dientich(a, b, c):
    p = chuvi(a, b, c) / 2
    return canbac2(p*(p - a)*(p - b)*(p - c))