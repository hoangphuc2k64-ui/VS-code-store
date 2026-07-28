class Dientro:
    mau = {"den":0, "nau":1, "do":2, "cam":3, "vang":4, "luc":5, "lam":6, "tim":7, "xam":8, "trang":9}
    def __init__(self, vong1, vong2, vong3):
        self.vong1 = vong1.lower()
        self.vong2 = vong2.lower()
        self.vong3 = vong3.lower()
    def giatri(self):
        so = self.mau[self.vong1] *10 + self.mau[self.vong2]
        giatri_dientro = so * (10 **self.mau[self.vong3])
        return giatri_dientro

 # ===================================================================================================
while True:
    try:
        n = int(input("Nhap so luong dien tro: "))
        if n>0:
            break
        else:
            print("Vui long nhap so lon hon 0 !")
    except ValueError:
        print("Vui long nhap chinh xac !")

list_dientro = []
for i in range(n):
    v1 = input("Vong 1: ")
    v2 = input("Vong 2: ")
    v3 = input("Vong 3: ")
    list_dientro.append(Dientro(v1,v2,v3))

for dt in list_dientro:
    print("Dien tro: ", dt.giatri(), " (Ohm)")

t = tuple(dt.giatri() for dt in list_dientro)
print("Tuple: ", t)

print("R_min = ", min(t))
