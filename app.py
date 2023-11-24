import chess
import chess.engine
from flask import Flask, render_template, request, jsonify, redirect



app = Flask(__name__)
engine = chess.engine.SimpleEngine.popen_uci(r"C:\Users\user\Downloads\komodo-14\komodo-14_224afb\Windows\komodo-14.1-64bit-bmi2.exe")

engine_dict = {
    'stockfish' : r"C:\Users\user\Downloads\stockfish-windows-x86-64-avx2\stockfish\stockfish-windows-x86-64-avx2.exe",
    'komodo' : r"C:\Users\user\Downloads\komodo-14\komodo-14_224afb\Windows\komodo-14.1-64bit-bmi2.exe"
}


@app.route('/', strict_slashes=False)
def index():
    return render_template('main.html')

@app.route('/chess', strict_slashes=False)
def chess_game():
    return render_template('chess.html')

@app.route('/move', methods=['POST'], strict_slashes=False)
def move():
    #get json file
    data = request.get_json()

    #create board instance based on player feed
    board = chess.Board(data['fen'])

    #get best result to be played based on egine
    info = engine.analyse(board, chess.engine.Limit(time=0.1))
    score = str(info['score'].relative)
    board.push(info['pv'][0])
    return jsonify({
        'pv': str(info['pv'][0]),
        'fen': board.fen(),
        'score': score
        })

@app.route('/init', methods=['POST'], strict_slashes=False)
def initiliaze():
    print(request.form.get('comp_engine'))

    #get the global engine variable
    global engine

    # set the engine to the one selected
    engine = chess.engine.SimpleEngine.popen_uci(engine_dict[str(request.form.get('comp_engine'))])
    print(engine.id)
    return redirect('http://127.0.0.1:5000/chess')


if __name__ == "__main__":
    app.run(debug=True, threaded=True)