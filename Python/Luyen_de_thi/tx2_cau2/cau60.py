class HoaQua:
    def __init__(self, loai_qua, gia, sl, chat_luong):
        self.loai_qua = loai_qua
        self.gia = gia
        self.sl = sl
        self.chat_luong = chat_luong
    def tien_thu(self):
        if self.chat_luong.lower() == "loai 1":
            return (self.sl * self.gia)
        elif self.chat_luong.lower() == "loai 2":
            return (self.sl * self.gia) - ((self.sl * self.gia) *20/100)
        else:
            return 0

# ========================================================
ds_hoaqua = []

while True:
    try:
        n = int(input("Nhap so lan thu hoach: "))
        if n > 0:
            break
        else:
            print("-> Nhap so lan thu hoach > 0 ")
    except ValueError:
        print("-> Vui long nhap so nguyen !")

for i in range(n):
    print(f"\n===== Nhap danh sach lan thu hoach {i+1} =====")
    while True:
        loai_qua = input("Nhap loai qua (cam / chuoi / na): ")
        if loai_qua.lower() == "cam" or loai_qua.lower() == "chuoi" or loai_qua.lower() == "na":
            break
        else:
            print("-> Nhap 3 loai qua cam / chuoi / na !")

    while True:
        try:
            gia = float(input(f"Nhap gia cua loai qua '{loai_qua}': "))
            if gia > 0:
                break
            else:
                print("-> Nhap gia lon hon 0 !")
        except ValueError:
            print("-> Vui long nhap chinh xac !")

    while True:
        try:
            sl = int(input(f"Nhap so luong loai qua '{loai_qua}': "))
            if sl >= 0:
                break
            else:
                print("-> Nhap so luong >= 0 !")
        except ValueError:
            print("-> Vui long nhap so nguyen !")

    while True:
        chat_luong = input("Nhap chat luong: ")
        if chat_luong.lower() == "loai 1" or chat_luong.lower() == "loai 2":
            break
        else:
            print("-> Nhap dung loai chat luong !")

    ds_hoaqua.append(HoaQua(loai_qua, gia, sl, chat_luong))

# ===========================================================================
print("\n====== Danh sach lan thu hoach =======")
for i, hoaqua in enumerate(ds_hoaqua):
    print(f"\nLan thu hoach {i+1}: ")
    print("Loai qua: ", hoaqua.loai_qua)
    print("Gia: ", hoaqua.gia)
    print("So luong: ", hoaqua.sl)
    print("Chat luong: ", hoaqua.chat_luong)
    print("Tinh tien: ", hoaqua.tien_thu())

# ===========================================================================
dict_hoaqua = {}
for hoaqua in ds_hoaqua:
    dict_hoaqua[hoaqua.loai_qua] = hoaqua.tien_thu()
print("\nDictionary: ", dict_hoaqua)

# ===========================================================================
ds_hoaqua.sort(key = lambda hoaqua: hoaqua.sl, reverse= True)
print("\n====== Danh sach sau khi sap xep giam dan cua so luong =======")
for i, hoaqua in enumerate(ds_hoaqua):
    print(f"\nLan thu hoach {i+1}: ")
    print("Loai qua: ", hoaqua.loai_qua)
    print("Gia: ", hoaqua.gia)
    print("So luong: ", hoaqua.sl)
    print("Chat luong: ", hoaqua.chat_luong)
    print("Tinh tien: ", hoaqua.tien_thu())
