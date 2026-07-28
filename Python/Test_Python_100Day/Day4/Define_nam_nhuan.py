year = int(input("Nhap nam (SCN):"))
is_year = bool(year %4 == 0 and year %100 != 0 or year %400 == 0)
print(year, "la nam nhuan ", is_year)

