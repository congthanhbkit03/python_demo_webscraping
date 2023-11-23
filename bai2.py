import random

#tao 1 so nguyen ngau nhien 1 - 20
randomNumber = random.randint(1, 20)

# print(randomNumber)

#nguoi dung chon so - nhap gia tri doan tu ban phim
# cho phep doan 6 lan
# range(0, n): 0, 1, 2, .... (n - 1)
# range(m): m lần 
for i in range(1, 7):
    print("Mời bạn đoán số:")
    playerGuess = int(input())
    if playerGuess == randomNumber:
        break;
    elif playerGuess > randomNumber:
        print("Số bạn đoán lớn hơn kết quả - Đoán lại")
    else:
        print("Số bạn đoán nhỏ hơn kết quả - Đoán lại")

#in ket qua
if playerGuess == randomNumber:
    print("Chúc mừng! Bạn đã đoán đúng!")
else:
    print("Bạn không đoán đúng - Kết quả là: " + str(randomNumber))
