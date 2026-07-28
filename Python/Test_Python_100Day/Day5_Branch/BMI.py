# Cấu trúc rẽ nhánh là if, elif, else, switch - case
weight = float(input("Nhập cân nặng (kg): "))
height = float(input("Nhập chiều cao (cm): "))

bmi = weight /((height /100) **2)

print(f"{round(bmi, 1)}")
if  18.5 <= bmi < 24:
    print("=> Binh thuong")
elif bmi < 18.5:
    print("=> Nhẹ cân so với chieu cao")
else:
    print("=> Nặng cân so với chieu cao")