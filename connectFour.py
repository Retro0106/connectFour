def make_board(rows, columns):
    # TODO: create a board, which is a 2D list with
    # 'rows' rows and 'columns' columns. The contents of each cell
    # should start out as '.'
    board = []
    for row in range(rows):
      board.append([])
      for col in range(columns):
        board[row].append('.')
    return board


def print_board(board):
    # TODO: print the board to the screen; don't just do
    # this, which is ugly:
    #   print(board)
    for row in board:
      print(row)
    

def make_move(token_color, column, board):
    # TODO: update 'board', by placing a token
    # of 'token_color' in 'column'. If a player
    # attempts an illegal move, which could be
    # 'column' < 0, 'column' > 'board' column size,
    # or trying to add a token to an already full
    # column, you can do this:
    #   raise Exception('illegal move')
    if column < 0 or column > len(board[0]) or board[0][column] != '.':
      raise Exception('illegal move')
    
    for row in range(-1,-len(board)-1,-1):
      if board[row][column]=='.':
        board[row][column] = token_color
        break


def evaluate_board(board):
    # TODO: evaluate 'board' looking for a winner; return
    # a character as follows:
    #   '.' - nobody has won yetR
    #   'R' - there are 4 'R' tokens in a row: this 
    #         is a win for 'R'
    #   'Y' - there are 4 'Y' tokens in a row: this
    #         is a win for 'Y'
    #   'T' - the game is a tie: all cells full and no 
    #         lines of 4 tokens for either player
    
    
    #Horzontal Win
    for row in range(len(board)):
      for col in range(len(board[row])-3):
        if board[row][col] != '.' and (board[row][col]==board[row][col+1]==board[row][col+2]==board[row][col+3]):
          return board[row][col]
    
    #Vertical Win
    for row in range(len(board)-3):
      for col in range(len(board[row])-3):
        if board[row][col] != '.' and (board[row][col]==board[row+1][col]==board[row+2][col]==board[row+3][col]):
          return board[row][col]
    
    #Backslash Diagonal Win
    for row in range(len(board)-3):
      for col in range(len(board[row])-3):
        if board[row][col] != '.' and (board[row][col]==board[row+1][col+1]==board[row+2][col+2]==board[row+3][col+3]):
          return board[row][col]
    
    # Frontslash Diagonal Win
    for row in range(3, len(board)):  
        for col in range(len(board[row]) - 3):  
            if board[row][col] != '.' and board[row][col] == board[row - 1][col + 1] == board[row - 2][col + 2] == board[row - 3][col + 3]:
                return board[row][col]

    

    
    #Tie
    if '.' not in board:
      return 'T'
    return '.'





    









# NOTE: you should not have to make any changes below this line
if __name__ == '__main__':
  board = make_board(6, 7)

  score = '.'
  # score '.' means no winner yet
  while score == '.':
    # ask R player for their move
    c = int(input('R move: which column? '))
    # apply the move 
    make_move('R', c, board)
    # print out the board so we can see it
    print_board(board)
    # check to see if anybody has won
    score = evaluate_board(board)
    if score == '.':
      # if we get here, nobody has won yet, ask
      # Y for their move
      c = int(input('Y move: which column? '))
      # apply the move
      make_move('Y', c, board)
      # print out the board so we can see it
      print_board(board)
      # check to see if anybody has won
      score = evaluate_board(board)
    
 # outside the 'while' loop means the game is over;
  # either one of the players won, or it's a tie
  if score == 'R':
    print('R wins')
  elif score == 'Y':
    print('Y wins')
  elif score == 'T':
    print('tie game')

