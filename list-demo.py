# nhie vu 1
# n = int(input('So hoc sinh can nhap:'))
#
# hs = []
# for i in range(n):
#     ten = input('Nhap ten hoc sinh: ')
#     hs.insert(0, ten)
#
# for h in hs:
#     print(h, end=' ')

# nhiem vu 2
# A = [0, -1, 4, -3, 3, 4, -7]
# for v in A:
#     if v < 0:
#         A.remove(v)
#
# print(A)

# nhiem vu 3
# A = [12, 4, -3, 0, 1, 2, 3, 5, 9, 0, 3, 4, 5]
# P = [4, 5, 6]
#
# vitri = -1
# for i in range(len(A) - 2):
#     if A[i] == P[0] and A[i + 1] == P[1] and A[i + 2] == P[2]:
#         vitri = i
#         break
#     else:
#         i = i + 1
# if vitri >= 0:
#     print('Tim thay P trong A tai vi tri', vitri)
# else:
#     print('Khong tim thay P trong A')

# luyen tap 1
# A = [1, 2, 2, 3, 4, 5, 5]
# A.insert(1, 1)
# print(A)
# A.insert(4, 3)
# print(A)
# A.insert(6, 4)
# print(A)

# luyen tap 2
# B = [1, 1, 2, 2, 9, 3, 3, 2, 2]
# if len(B) % 2 == 1:
#     vitrixoa = int((len(B) - 1) / 2)
#     B.remove(B[vitrixoa])
# print(B)

#van dung 1
# n = int(input("Nhập số tự nhiên n:"))
# A = []
# for i in range(n):
#     if i % 2 == 0:
#         A.append(i)
# for i in A:
#     print(i, end=' ')

# van dung 2
n = int(input("Nhập số n: "))
Fibo = [0, 1]

for i in range(2, n):
    current_value = Fibo[i - 1] + Fibo[i - 2]
    Fibo.append(current_value)

for i in Fibo:
    print(i, end=' ')
