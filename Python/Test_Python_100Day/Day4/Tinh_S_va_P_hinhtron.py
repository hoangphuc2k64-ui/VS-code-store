import math

R = float(input("Nhap ban kinh: "))
P = 2 * math.pi * R
S = math.pi * (R**2)

print("=> Cach 1")
print(f"Chu vi = {round(P, 2)}")        # round lam tron
print(f"Dien tich = {round(S, 2)}")

# template
# cach 2
print("\n=> Cach 2")
print(f"Chu vi = %.2f" % P)
print(f"Dien tich = %.2f" % S)

# cach 3
print("\n => Cach 3")
print(f"Chu vi = {P:.2f}")
print(f"Dien tich = {S:.2f}")