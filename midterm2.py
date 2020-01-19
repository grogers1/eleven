from eleven import Player
from eleven import test_player
import random


class HumanPlayer(Player):

    def __init__(self):
        super()


    def get_move(self):
        print(self.board) 
        print("Score: ", self.score) 

        valid_input = False

        while not valid_input:
            user_input = input("Enter a move (up, down, left, right): ").lower()

            if user_input in self.board.valid_moves(): 
                return user_input 

    def play(self):
        result = super.play(self) 

        if result:
            print("You won!")
        else:
            print("Game over, better luck next time!")

        print(self.board)  
        print("Your Score is: ", self.score)  

class ComputerPlayer(Player):
    def __init__(self):
        super().__init__()

    def play(self):
        super().play()

    def get_move(self):
        valid_inputs = self.board.valid_moves() 

        move = random.choice(valid_inputs) 

        return move 


class ComputerPlayer2(ComputerPlayer):
    def __init__(self):
        super().__init__()

    def get_move(self):
        valid_inputs = self.board.valid_moves() 

        move_score = dict() 

       
        for move in valid_inputs:
            new_board, score = self.board.calculate_move(move) 
            open_space = new_board.count(None)
            move_value = score + open_space
            move_score[move] = move_value

       
        max_move = max(move_score, key=move_score.get)

        
        return max_move

if __name__ == "__main__":

    print(test_player(ComputerPlayer))
    print(test_player(ComputerPlayer2))

        
    

        
