# 64 Knight Tour problem 
# En küçük maliyetli yolun bulunması
# Bu kod KTÜ Bilgisayar Mühendisliği Bölümü'nde staj yapan öğrenciler tarafından hazırlanmıştır.
# Yazar[lar]: Nuh Aslan , Beytullah Bilek

n = 8
def isSafe(x, y, board):
    '''
        İ, j'nin geçerli dizinler olup olmadığını kontrol etmek için bir yardımcı işlev
         N * N satranç tahtası için
    '''
    if (x >= 0 and y >= 0 and x < n and y < n and board[x][y] == -1):
        return True
    return False


def printSolution(board):
    '''
       Satranç tahtası matrisini basmak için bir yardımcı işlev
    '''
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=' ')
        print()


def solveKT():
    

    # Yönetim Kurulu matrisinin başlatılması
    board = [[-1 for i in range(n)] for i in range(n)]# sekize sekizlik bir matris oluşturarak içine -1 yerleştirir hepsinin

    #move_x ve move_y, Knight'ın bir sonraki hamlesini tanımlar.
    # move_x, bir sonraki x koordinatı değeri içindir
    # move_y, y koordinatının sonraki değeri içindir
    move_x = [2, 1, -1, -2, -2, -1, 1, 2]
    move_y = [1, 2, 2, 1, -1, -2, -2, -1]

    # Şövalye başlangıçta ilk blokta olduğundan
    board[0][0] = 0

    # atın konumu için adım sayacı
    pos = 1

    # Çözümün olup olmadığını kontrol etme
    if (not solveKTUtil(board, 0, 0, move_x, move_y, pos)):# Eğer solveKTUtil den dönen değer TRUE ( TRUE olması demek pos == n ** 2 yani işlemler sonlandı tüm board gezildi ) ise if ( not TRUE) ise else i yazdırır yani tahtanın son halini basar  
        print("Solution does not exist") # Eğer solveKTUtil den dönen deger FALSe ise ( ancak işlemler bitmeden önce cıkılması durumu yani return FALSE degeri dönünce)     if ( not FALSE ) ise if içerisini yazdıracak
    else:
        printSolution(board)


def solveKTUtil(board, curr_x, curr_y, move_x, move_y, pos):
    '''
        Knight Tour'u çözmek için tekrarlayan bir yardımcı fonksiyon
         
    '''

    if (pos == n ** 2):# eğer tüm kareler dolaşıldıysa yani board tamamen gezildiyse true döndürür
        return True

    # Geçerli koordinattan sonraki tüm hareketleri dene x, y
    for i in range(8):
        new_x = curr_x + move_x[i]
        new_y = curr_y + move_y[i]
        #print(new_x,"  ",new_y)

        if (isSafe(new_x, new_y, board)):
            board[new_x][new_y] = pos
            #print(new_x, "  ", new_y)
            #print()
            if (solveKTUtil(board, new_x, new_y, move_x, move_y, pos + 1)):

                return True

            else:
            # Backtracking

                board[new_x][new_y] = -1
            
    return False

solveKT()
