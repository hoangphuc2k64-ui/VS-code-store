x = float(input("Nhap gia tri cua x: "))

if x > 1:
    y = 3*x -5
elif -1 <= x <= 1:
    y = x + 2
else:
    y = 5*x + 3

print("=> Khi x = ", x, " thi y = ", y)
print(f"{y = }")