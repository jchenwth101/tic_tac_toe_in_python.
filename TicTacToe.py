#Joel Chenoweth
#3-3-20
#This is a classic two player tic tac toe game in Python

class TicTacToe():

    def __init__(self):
        """This defines the array for the board initials the state function."""
        self.__board = [[' '] * 3 for row in range(3)]

        self.__current_state = 'UNFINISHED'

    def get_current_state(self):
        """this sets up the current state function"""
        return self.__current_state

    def make_move(self, row, col, symbol):
        """this highlights logical operators for the player move"""
        if 0 <= row <= 2 and 0 <= col <= 2 :
            if self.__board[row][col] == ' ':
                self.__board[row][col] = symbol
                self.__check_winner()
                return True

            else:
                return False
        else:
            return False

    def __check_winner(self):
        """this function checks columns and rows for the winner of the game"""
        if self.__board[0][0] == self.__board[0][1] == self.__board[0][2] and self.__board[0][0] != ' ':
            self.__current_state = 'X_WON' if self.__board[0][0] == 'X' else 'O_WON'
            return
        if self.__board[1][0] == self.__board[1][1] == self.__board[1][2] and self.__board[0][0] != ' ':
            self.__current_state = 'X_WON' if self.__board[1][0] == 'X' else 'O_WON'
            return
        if self.__board[2][0] == self.__board[2][1] == self.__board[2][2] and self.__board[2][0] != ' ':
            self.__current_state = 'X_WON' if self.__board[2][0] == 'X' else 'O_WON'
            return

        if self.__board[0][0] == self.__board[1][0] == self.__board[2][0] and self.__board[0][0] != ' ':
            self.__current_state = 'X_WON' if self.__board[0][0] == 'X' else 'O_WON'
            return
        if self.__board[0][1] == self.__board[1][1] == self.__board[2][1] and self.__board[0][1] != ' ':
            self.__current_state = 'X_WON' if self.__board[0][1] == 'X' else 'O_WON'
            return
        if self.__board[0][2] == self.__board[1][2] == self.__board[2][2] and self.__board[0][2] != ' ':
            self.__current_state = 'X_WON' if self.__board[0][2] == 'X' else 'O_WON'
            return

        if self.__board[0][0] == self.__board[1][1] == self.__board[2][2] and self.__board[0][0] != ' ':
            self.__current_state = 'X_WON' if self.__board[0][0] == 'X' else 'O_WON'
            return
        if self.__board[0][2] == self.__board[1][1] == self.__board[2][0] and self.__board[2][0] != ' ':
            self.__current_state = 'X_WON' if self.__board[2][0] == 'X' else 'O_WON'
            return

        for row in range(3):
            for col in range(3):
                if self.__board[row][col]==' ':
                    self.__current_state='UNFINISHED'
                    return

        self.__current_state='DRAW'

    def printBoard(self):
        """this function prints the board on screen"""

        print(' | '.join(self.__board[0]))
        print('-'* 9)
        print(' | '.join(self.__board[1]))
        print('-' * 9)
        print(' | '.join(self.__board[2]))



def main():
    """this establishes order of operations"""
    game=TicTacToe()
    game.printBoard()
    while game.get_current_state() =='UNFINISHED':
        x=y=0
        while True:
            x = int(input('Player 1 - Enter row [0-2]: '))
            y = int(input('Player 1 - Enter col [0-2]: '))
            if game.make_move(x,y,'X'):
                break
            else:
                print('Your move was invalid!')
        game.printBoard()
        if game.get_current_state()=='X_WON' or game.get_current_state()=='DRAW':
            break

        while True:
            x = int(input('Player 2 - Enter row [0-2]: '))
            y = int(input('Player 2 - Enter col [0-2]: '))
            if game.make_move(x,y,'O'):
                break
            else:
                print('Your move was invalid!')
        game.printBoard()
        if game.get_current_state()=='O_WON' or game.get_current_state()=='DRAW':
            break

    if game.get_current_state()=='DRAW':
        print('Its a DRAW!')
    elif game.get_current_state()=='O_WON':
        print('Player 1 Wins')
    else:
        print('Player 2 Wins')

main()