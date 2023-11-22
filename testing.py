import chess
 
# create board object
board=chess.Board()
print(list(board.legal_moves))
 
# display chess board
print(board.turn)
board.push_san("e4")
# It means moving the particular piece at 
# e place to 4th position 
  
# Display chess board  
print()
print(board.turn)
print(list(board.legal_moves))
