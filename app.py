from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

# 初期投票数
vote_count = 0

@app.route('/')
def index():
    return render_template('index.html', vote_count=vote_count)

@socketio.on('increment_vote')
def handle_increment_vote():
    global vote_count
    vote_count += 1
    # 投票数の更新を全クライアントにブロードキャスト
    emit('update_vote_count', {'vote_count': vote_count}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
