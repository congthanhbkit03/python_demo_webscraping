from datetime import date

#nam hien tai
nam_hien_tai = date.today().year

print("Nhập tên:")
ten = input()
print("Nhập năm sinh: ")
namsinh = int(input())

# input nhap vao 1 chuoi - string
# int() float() str() ép kiểu
print("Thông tin của bạn")
print("Họ tên: " + ten)
print("Tuổi của bạn: " + str(nam_hien_tai - namsinh))
