from flask import Flask, render_template, send_file
from flask_socketio import SocketIO, send

pesan_dikirim = []

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'  # Kunci rahasia untuk enkripsi komunikasi WebSocket
socketio = SocketIO(app)

# Membuat struktur data untuk menyimpan informasi pengguna

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('message')
def handle_message(message):
    print('Received message:', message)
    pesan_dikirim.append(message)
    send(message, broadcast=True)

#Coba-coba
@socketio.on('hapus_pesan_terakhir')
def handle_hapus_pesan_terakhir():
    if pesan_dikirim:
        pesan_akhir = pesan_dikirim.pop()
        print('Web Socket List Dihapus!!!')
        socketio.emit('update_pesan_list')  # Mengirim perintah ke klien untuk memperbarui daftar pesan
        
if __name__ == '__main__':
    socketio.run(app, debug=True)
