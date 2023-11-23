import random, sys

print("Xin chào đến với trò chơi Oẳn tù tì")
#cac bien luu ket qua của tro choi
thang = 0
thua = 0
hoa = 0

#vong lap chinh chay lien tuc den khi nao chuong trinh dung
while True:
    # in ket qua
    print("Thang: %s, Thua: %s, Hoà: %s" %(thang, thua, hoa))
    while True: #vong lap yeu cau nguoi dung chon Bua (u), Bao (b), Keo (k) hay q - vong lap (2)
        print("Mời bạn chọn: u (Búa), b (Bao), k (Kéo) hoặc q để Thoát chương trinh")
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  #thoat chuong trinh
        elif playerMove == 'u' or playerMove == 'b' or playerMove == 'k':
            break   #thoat khoi vong lap (2)
        print("Bạn chỉ được chọn u, b, k hoặc q thôi")

    #in ket qua cua nguoi chon chon
    if (playerMove == 'u'):
        print("BÚA sẽ đấu với ...")
    elif (playerMove == 'b'):
        print("BAO sẽ đấu với ...")
    elif (playerMove == 'k'):
        print("KÉO sẽ đấu với ...")

    #hien thi may tiinh chọn
    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        computerMove = 'u'
        print(" BÚA")
    elif randomNumber == 2:
        computerMove = 'b'
        print(" BAO")
    elif randomNumber == 3:
        computerMove = 'k'
        print(" KÉO")

    #so sanh va cap nhat ket qua
    if computerMove == playerMove:
        print("Hoà!")
        hoa = hoa + 1
    elif computerMove == 'u' and playerMove == 'b':
        print("Bạn thắng!")
        thang = thang + 1
    elif computerMove == 'u' and playerMove == 'k':
        print("Bạn đã thua!")
        thua = thua + 1
    elif computerMove == 'b' and playerMove == 'u':
        print("Bạn đã thua!")
        thua = thua + 1
    elif computerMove == 'b' and playerMove == 'k':
        print("Bạn thắng!")
        thang = thang + 1
    elif computerMove == 'k' and playerMove == 'u':
        print("Bạn thắng!")
        thang = thang + 1
    elif computerMove == 'k' and playerMove == 'b':
        print("Bạn đã thua!")
        thua = thua + 1
