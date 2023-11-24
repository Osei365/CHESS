import chess
import chess.engine

engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\user\Downloads\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe")
print(dir(engine))
print(engine.id)
board = chess.Board()
info = engine.analyse(board, chess.engine.Limit(time=0.1))
print("Score:", info["score"])
# Score: PovScore(Cp(+20), WHITE)

# board = chess.Board("r1bqkbnr/p1pp1ppp/1pn5/4p3/2B1P3/5Q2/PPPP1PPP/RNB1K1NR w KQkq - 2 4")
# info = engine.analyse(board, chess.engine.Limit(depth=20))
# print(info)
# print("Score:", dir(info["score"]))
# print("Score:", str(info["score"].relative))
print()
board.push(info['pv'][0])
info = engine.analyse(board, chess.engine.Limit(depth=20))
print(info)
print("Score:", dir(info["score"]))
print("Score:", str(info["score"].relative))

print()
board.push(info['pv'][0])
info = engine.analyse(board, chess.engine.Limit(depth=20))
print(info)
print("Score:", dir(info["score"]))
print("Score:", str(info["score"].relative))
print("Score:", str(info["pv"][0]))
# Score: PovScore(Mate(+1), WHITE)

engine.quit()
