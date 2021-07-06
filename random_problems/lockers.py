from time import sleep
from os import system, name

class Lockers:
    def __init__(self, size=10):
        self.size = size
        self.board = [[0 for i in range(size)] for j in range(size)]
        self.start()
        self.get_open()


    def start(self):
        system('cls')
        for n in range(1,self.size ** 2 + 1):
            self.toggle_multiples_of_sequel(n)


    def toggle_multiples_of(self, n):
        for i in range(self.size):
            for j in range(self.size):
                value = self.size*i + j + 1

                if value % n == 0:
                    self.board[i][j] = 1 - self.board[i][j]

                system('cls')

                self.print_board()
                print(f"[{n}]")

                sleep(0.0001)


    def toggle_multiples_of_sequel(self, n):
        curr = n
        while curr <= self.size ** 2:
            i = (curr-1) // self.size
            j = (curr-1) % self.size
            self.board[i][j] = 1 - self.board[i][j]

            system('cls')

            self.print_board()
            print(f"[{n}]")

            sleep(0.0001)

            curr += n


    def print_board(self):
        for row in self.board:
            print(row)


    def get_open(self):
        open_lockers = []
        for i in range(self.size):
            for j in range(self.size):
                if self.board[i][j] == 1:
                    open_lockers.append(self.size*i + j + 1)
        print('\nOpen Lockers:')
        print(open_lockers)


Lockers(15)
