class Game(object):
    def __init__(self):
        self.P1 = P1
        self.P2 = P2
        self.PBoard = PBoard
        self.rowSelect = ''
        self.colSelect = ''

    def select_rows_column(self,selection,row_or_column):
            while True:
                #If player is selecting row, original strings are used, else changes Top to Left and Bototm to Right
                first_opt = 'Top'
                second_opt = 'Middle'
                third_opt = 'Bottom'
                if row_or_column == 'Column':
                    first_opt = 'Left'
                    third_opt = 'Right'

                #Inserts strings above and then ask for user input    
                print('1 for {}, 2 for {}, 3 for {}').format(first_opt,second_opt,third_opt)
                message = '{}: '.format(row_or_column)
                self.selection = raw_input(message)
                
                try:
                    #Convert user input to int, check if it's in range of 1-3
                    self.selection = int(self.selection)
                    if self.selection<1 or self.selection>3:
                        print('Number not in range.')
                        print('')
                        continue                    
                    else:
                        #Here, a valid input will -1 because the board index starts at 0 and ends at 2
                        self.selection-=1
                        print('')
                        break
                    
                except ValueError:
                    #For any non integer inputs
                    print('Invalid input.')
                    print('')
            return self.selection

    def play_sequence(self,playBoard,player1,player2):
        while True:
            if player1.turn == True:                                                
                current_Player = player1
            else:
                current_Player = player2
            playBoard.print_board()    
            print('{}, your turn.').format(current_Player.name)

            #Player chooses row and columns
            self.rowSelect = self.select_rows_column(self.rowSelect,'Row')          
            self.colSelect = self.select_rows_column(self.colSelect,'Column')

            #If selected row and column is not empty, it is taken
            if PBoard.aRow[self.rowSelect][self.colSelect]!=' ':                    
                print('Choice already played')
                continue

            
            else: #Check for win and clear the board if yes, else check for draw.                                                                
                playBoard.aRow[self.rowSelect][self.colSelect] = current_Player.token
                playBoard.check_win()       
                if playBoard.win:
                    playBoard.print_board()
                    playBoard.clear_board()
                    print('{} wins!').format(current_Player.name)
                    break
                playBoard.check_draw()
                if playBoard.draw:
                    playBoard.clear_board()
                    break
                

                #Swap current_Player if game hasn't ended, don't change this, it lets P1 and P2 swap after every game                            
                elif player1.turn:
                    player1.turn = False
                    player2.turn = True
                else:
                    player1.turn = True
                    player2.turn = False
                       
class Board(object):
 
    def __init__(self):
        self.tRow = [' ',' ',' ']
        self.mRow = [' ',' ',' ']
        self.bRow = [' ',' ',' ']
        self.aRow = self.tRow,self.mRow,self.bRow
        self.win = False    #True if a win is detected
        self.draw = False   #True if a draw is detected

    def print_board(self):
        print('')
        print("   {} | {} | {} ").format(self.tRow[0],self.tRow[1],self.tRow[2])
        print('  -----------')
        print("   {} | {} | {} ").format(self.mRow[0],self.mRow[1],self.mRow[2])
        print('  -----------')
        print("   {} | {} | {} ").format(self.bRow[0],self.bRow[1],self.bRow[2])
        print('')

    def check_win(self):
        #This checks for horizontal wins, loop through each array and check if values in every indexes are the same
        for i in self.aRow:
            if i[0]!=' ' and i[0] == i[1] and i[0] == i[2]:
                self.win = True

        #This checks for vertical wins, loop through each index and check if values in every array are the same      
        for i in range(3):
            if self.aRow[0][i]!= ' ' and self.aRow[0][i] == self.aRow[1][i] and self.aRow[0][i] == self.aRow[2][i]:
                self.win = True

        #Checks for vertical wins
        if self.aRow[0][0]!=' ' and self.aRow[0][0] == self.aRow[1][1] and self.aRow[0][0] == self.aRow[2][2]:
            self.win = True
            
        if self.aRow[0][2]!=' ' and self.aRow[0][2] == self.aRow[1][1] and self.aRow[0][2] == self.aRow[2][0]:
            self.win = True
    
    def check_draw(self):
        #Checks if every row and column are occupied, if they are, declare draw. Win has to be checked before draw.
        top_row = ' ' not in self.aRow[0]
        mid_row = ' ' not in self.aRow[1]
        bot_row = ' ' not in self.aRow[2]
        self.draw = top_row and mid_row and bot_row
        if self.draw:
            self.draw = True
            print("It's a tie.")

    def clear_board(self):
        #Basically reinitializes the board
        self.tRow = [' ',' ',' ']
        self.mRow = [' ',' ',' ']
        self.bRow = [' ',' ',' ']
        self.win = False
        self.draw = False
        self.aRow = self.tRow,self.mRow,self.bRow

class Player(object):
    def __init__(self,token,name,turn):
        self.token = token
        self.name = name
        self.turn = turn

class Player1(Player):
    def __init__(self):
        Player.__init__(self,'X','Player 1',True)

class Player2(Player):
    def __init__(self):
        Player.__init__(self,'O','Player 2',False)

P1 = Player1()
P2 = Player2()
PBoard = Board()
G = Game()

while True:
    G.play_sequence(PBoard,P1,P2)
    print('\n\n Play again?')
    replay = raw_input('X to exit: ')
    if replay.upper() == 'X':
        break
    
        
