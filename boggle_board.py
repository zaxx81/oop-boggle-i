import random

class BoggleBoard:
  
  def __init__(self):
    self.board = self.reset()

  # Creates a random 4x4 board
  def shake(self):
    self.board = []

    # A list of uppercase letters with 'Q' represented as 'Qu'
    letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Qu','R','S','T','U','V','W','X','Y','Z']
    
    # A nested loop to fill the 4x4 board with random letters from letters[]
    for board_row in range(4):
      row = []
      for board_col in range(4):
        # Randomly selects a letter from letters[]
        letter = random.choice(letters)
        # Appends a letters 4 times to row[]
        row.append(letter)
      # Appends a row 4 times to self.board        
      self.board.append(row)

  # Resets the board  
  def reset(self):
    self.board = ["-  -  -  -"] * 4

  # Prints the board to console
  def display_board(self):
    board_str = ''
    
    # Adds a row_str to board_str
    for board_row in self.board:
      row_str = ''
      
      for letter in board_row:
        # Adds each letter to row_str and a single space
        row_str += f'{letter} '
        # If the letter is not 'Qu' it adds an extra space
        if letter != 'Qu':
          row_str += ' '
      # Adds a row to board_str with a '\n', so next row will be on another line
      board_str += f'{row_str}\n'

    print(board_str)

# Driver Test Code
my_bog = BoggleBoard()
my_bog.shake()
my_bog.display_board()
