"""
Chuyển đổi nhiệt độ từ độ F (Fahrenheit) sang độ C (Celsius)

Phiên bản: 1.1
Tác giả: Lạc Hạo (Luo Hao)
"""
f = float(input('Vui lòng nhập nhiệt độ F: '))
c = (f - 32) / 1.8
# 1.
print('%.1f độ F = %.1f độ C' % (f, c))
# %1f là làm tròn khá giống round nhưng có thể hoạt động trong chuỗi, nó làm tròn ở bên (f, c)
# trước đó nhập f và tính c, thì có 2 cái %1f, cái vế %1f sẽ bốc ở bên f và làm tròn, cái vế 2 sẽ bốc của c và làm tròn

# 2.
print(f'{f:.1f} độ F = {c:.1f} độ C')

# 3. cach cua ban than nghi ra
print(f'{round(f, 1)} do F = {round(c, 1)} do C')