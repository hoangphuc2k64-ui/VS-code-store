import ham_all

list_float9 = []
while True:
    x = input("Nhap so thuc: ")
    if x.lower() == "t":
        break
    try:
        so = float(x)
        list_float9.append(so)
    except ValueError:
        print("Vui long nhap chinh xac !")

max_nega = ham_all.find_max_nega(list_float9)
min_pos = ham_all.find_min_pos(list_float9)
tbc_nega, tbc_pos = ham_all.tbc_pos_neg(list_float9)

print("\n======== Ket qua ========")
print("=> So am lon nhat:", max_nega)
print("=> So duong nho nhat:", min_pos)
print("=> TBC so am:", tbc_nega)
print("=> TBC so duong:", tbc_pos)

dict9 = {}
dict9[list_float9.index(min_pos)] = min_pos
dict9[list_float9.index(max_nega)] = max_nega
print("Dict chua so am lon nhat va so duong nho nhat: ", dict9)

t = tuple([max_nega, min_pos])
print("Tuple chua so am lon nhat va so duong nho nhat: ", t)


