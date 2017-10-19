import os




class NewGame():
    def __init__(self):
        self.board = [["7", "8", "9"],
                      ["4", "5", "6"],
                      ["1", "2", "3"]]

        self.turn = 0
        self.winner = False
        self.exhaustedSlots = [False, False, False, False, False, False, False, False, False]

        self.playerToken = ["O", "X"]


    # Returns true if there is a winner
    def isThereWinner(self):

        # diagonals check
        if(self.board[0][0] == self.board[1][1] == self.board[2][2] or self.board[0][2] == self.board[1][1] == self.board[2][0]):
            return True

        for n in range(0, 3):
            # vertical check
            if(self.board[0][n] == self.board[1][n] == self.board[2][n]):
                return True

            # horizontal check
            if (self.board[n][0] == self.board[n][1] == self.board[n][2]):
                return True



    def printBoardState(self):
        clear = lambda: os.system('cls')
        clear()

        if(self.winner == False):
            print("it is Player " + str((self.turn % 2) + 1) + "'s Turn!")
            print()

        for row in range(0, 3):
            print("/".join(self.board[row]))
        print()
        print()

    # Mutates the appropriate slot to the value given. Value should be the appropriate player token
    def morphSlot(self, slotInput, value):
        slot = (slotInput - 1) % 3
        if(slotInput<4):
            self.board[2][slot] = self.board[2][slot].replace(str(slotInput), value)
        elif(slotInput<7):
            self.board[1][slot] = self.board[1][slot].replace(str(slotInput), value)
        else:
            self.board[0][slot] = self.board[0][slot].replace(str(slotInput), value)




    # Returns true if the slot is not taken or invalid
    def isValidSlot(self, slot):


        if(slot>0 and slot<10):
            if(self.exhaustedSlots[slot-1] == False):
                return True
            else:
                print()
                print("That slot has already been used! please try a different slot")
                input("press enter to continue")
                return False

        else:
            print()
            print("invalid number, please select a number between 1 and 9")
            input("press enter to continue")
            return False



# slot = int(input("Player " + str((self.turn%2) + 1) + ", choose where you would like to place your token"))


    def turnPhase(self):


        self.printBoardState()
        try:


            givenSlot = int(
                input( "choose where you would like to place your token"))

            if(self.isValidSlot(givenSlot)):
                self.morphSlot(givenSlot, self.playerToken[self.turn%2])
                self.exhaustedSlots[givenSlot - 1] = True
                game.turn += 1


        except ValueError:
            print()
            print("Invalid value, please use a number")
            input("press enter to continue")
            self.turnPhase()

        if(self.isThereWinner()):
            self.winner = True
            game.turn -= 1

        if(self.turn == 9):
            self.winner = True




game = NewGame()

while(game.winner != True):
    game.turnPhase()

# The game is over

game.printBoardState()

if(game.turn < 9):
    print("Player " +  str(game.turn%2 + 1) + " wins!!")
    print()
    input("press enter to close")
else:
    print("The game has ended in a Draw")
    print()
    input("press enter to close")



