from random import randint


class Game:
    size = 0
    matrix = []
    current_player = 'player'
    won = False

    def __init__(self, size):
        self.size = size
        self.matrix = [['*' for j in range(size)] for i in range(size)]

    def draw(self):
        for i in range(len(self.matrix)):

            for j in range(len(self.matrix[i])):
                print(self.matrix[i][j], end='')

            print('')
        print('')

    def do_turn(self, x, char):
        for row in reversed(range(len(self.matrix[x]))):
            if self.matrix[row][x] == '*':
                self.matrix[row][x] = char
                break

        self.draw()

    def isplayer_Turn(self):
        if self.current_player == 'player':
            return True
        return False

    def change_player(self):
        if self.isplayer_Turn():
            self.current_player = 'computer'
        else:
            self.current_player = 'player'

    def update(self):
        while not self.won:
            if self.isplayer_Turn():
                col = input('Geef een kolom in: ')
                self.do_turn(int(col), 'X')
                self.change_player()
            else:
                col = randint(0, self.size - 1)
                self.do_turn(int(col), 'O')
                self.change_player()


    def check_if_won(self, lastX, lastY):
        char = self.matrix[lastY][lastX]

        print(char)



