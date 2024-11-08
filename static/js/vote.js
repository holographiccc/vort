// サーバーとのSocket.IO接続を確立
var socket = io.connect('http://' + document.domain + ':' + location.port);

// 投票ボタンがクリックされたときの処理
function incrementVote() {
    console.log("投票ボタンがクリックされました。");
    socket.emit('increment_vote');  // サーバーに投票を通知
}

// サーバーから投票数の更新を受け取ったときの処理
socket.on('update_vote_count', function(data) {
    console.log("新しい投票数:", data.vote_count);
    // ページ内の投票数を更新
    document.getElementById("vote_count").innerText = data.vote_count;
});
