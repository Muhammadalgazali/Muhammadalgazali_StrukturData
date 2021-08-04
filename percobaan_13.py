print('NAMA    : Muhammad Algazali')
print('NIM     : E1E1 19 032')
print('MATKUL  : Struktur Data')
print('_________________________________________________')

class GameEntry:
    total = 0

    def __init__(self, name, score, timeq):
        self.name = name
        self.score = score
        self.time = timeq
        
        GameEntry.total += 1
    
    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setScore(self, score):
        self.score = score
    
    def getScore(self):
        return self.score

    def setTime(self, timeq):
        self.time = timeq

    def getTime(self):
        return self.time

    def getTotal():
        return GameEntry.total

class ScoreBoard:

    def __init__(self, capacity):
        self.capacity = capacity
        self.board = [None] * self.capacity
        self.n = 0 #number of actual entries
    
    def getCapacity(self):
        return self.capacity

    def sumEntries(self):
        return self.n

    def addItem(self, entry):
        score = entry.getScore()

        condition = len(self.board) > self.n or score > self.board[self.capacity - 1].getScore()
        # print(condition)

        if condition:
            if self.n < self.capacity:
                self.n += 1

            j = self.n - 1

            while j > 0 and self.board[j-1].getScore() < score:
                self.board[j] = self.board[j-1]
                j -= 1
            self.board[j] = entry
            print(f"\nPrestasi baru dengan {score} ditambahkan dalam List!")

    def listEntries(self):
        for i in range (0, self.n):
            print("peringkat ",i+1," = ", getattr(self.board[i], 'name'), getattr(self.board[i], 'score'))

board = ScoreBoard(10)

active = True

while active:
    print("")
    pilihan = input("Daftar Menu : \n 1. Tampilkan ScoreBoard \n 2. Tambah Prestasi \n 3. Keluar \n Masukkan Pilihan = ")
    print("")
    if pilihan == '1':
        board.listEntries()
    elif pilihan == '2':
        name =      input("Masukkan nama pemain = ")
        skor =  int(input("Masukkan skor        = "))
        waktu = int(input("Masukkan waktu       = "))

        in_score = GameEntry(name, skor, waktu)
        set_board = board.addItem(in_score)

        print(f"Entri baru ditambahkan: {in_score.getName()} {in_score.getScore()} {in_score.getTime()}")
    else:
        print(f"Semoga Hari Anda Menyenangkan!")
        break
