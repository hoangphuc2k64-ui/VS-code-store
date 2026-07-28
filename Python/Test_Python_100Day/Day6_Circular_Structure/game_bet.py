import random

# Số tiền ban đầu của người chơi
tien = 1000

# Tiếp tục chơi khi vẫn còn tiền
while tien > 0:
    print(f"Tong so tien hien co: {tien} dong")

    # Nhập số tiền cược (phải lớn hơn 0 và không vượt quá số tiền đang có)
    while True:
        cuoc = int(input("Nhap so tien cuoc: "))
        if 0 < cuoc <= tien:
            break
        print("So tien cược không hợp lệ, vui lòng nhập lại!")

    # Tung 2 viên xúc xắc (mỗi viên từ 1 đến 6)
    diem_dau = random.randrange(1, 7) + random.randrange(1, 7)

    print(f"\nBạn tung được {diem_dau} điem")

    # Thắng ngay nếu được 7 hoặc 11
    if diem_dau == 7 or diem_dau == 11:
        print("Bạn win!\n")
        tien += cuoc

    # Thua ngay nếu được 2, 3 hoặc 12
    elif diem_dau == 2 or diem_dau == 3 or diem_dau == 12:
        print("Nhà cái win!\n")
        tien -= cuoc

    # Nếu chưa phân thắng thua thì tiếp tục tung
    else:
        print(f"Điểm mục tiêu của bạn là {diem_dau}")

        while True:
            diem_hien_tai = random.randrange(1, 7) + random.randrange(1, 7)

            print(f"Bạn tung được {diem_hien_tai} điểm")

            # Ra 7 trước thì thua
            if diem_hien_tai == 7:
                print("Nhà cái win!\n")
                tien -= cuoc
                break

            # Ra lại đúng điểm ban đầu thì thắng
            elif diem_hien_tai == diem_dau:
                print("Bạn thang!\n")
                tien += cuoc
                break

print("Bạn đã hết tiền! Trò chơi kết thúc.")