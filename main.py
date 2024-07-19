
from flask import Flask, request, render_template
import chess

app = Flask(__name__)

board = chess.Board()


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/api/move', methods=['POST'])
def move():
    data = request.get_json()
    move = chess.Move.from_uci(data['move'])
    board.push(move)
    return {'board': board.fen()}


if __name__ == '__main__':
    app.run(debug=True)
