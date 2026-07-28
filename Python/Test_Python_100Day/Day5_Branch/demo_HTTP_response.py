status_code = int(input("Nhap code trang thai lan 1: "))

if status_code == 400:
    description = "Bad Request"
elif status_code == 401:
    description = "Unauthorized"
elif status_code == 403:
    description = "Forbidden"
elif status_code == 404:
    description = "Not Found"
elif status_code == 405:
    description = "Method Not Allowed"
elif status_code == 418:
    description = "Im a teapot"
elif status_code == 429:
    description = "Too many requests" 
else:
    description = " Unknown status code"

print("Xac dinh trang thai => ", description)   

# ========================================================== 
# same "switch - case" ben C++ / C
status_code = int(input('Nhap code trang thai lan 2: '))
match status_code:
    case 400: description = 'Bad Request'
    case 401: description = 'Unauthorized'
    case 403: description = 'Forbidden'
    case 404: description = 'Not Found'
    case 405: description = 'Method Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('Trang thai => :', description)

# ========================================================
status_code = int(input('Nhap code trang thai lan 3: '))
match status_code:
    case 400 | 405: description = 'Invalid Request'
    case 401 | 403 | 404: description = 'Not Allowed'
    case 418: description = 'I am a teapot'
    case 429: description = 'Too many requests'
    case _: description = 'Unknown Status Code'
print('Trang thai => ', description)

# case _: truong hop con lai, tuong tu else