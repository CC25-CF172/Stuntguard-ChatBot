# Chatbot Stunting Asisten

## Deskripsi Proyek

Proyek ini adalah sebuah chatbot sederhana yang dikembangkan menggunakan bahasa pemrograman Python. Chatbot ini dapat menjawab pertanyaan pengguna melalui model pembelajaran mesin yang telah dilatih. Chatbot ini nantinya akan digunakan sebagai salah satu fitur pada website pencegahan stunting dini dalam capstone projek tim kami.

## Cara Instalasi

1. Pastikan Python telah terpasang di sistem Anda. Anda dapat mengunduhnya dari [python.org](https://www.python.org/downloads/).
2. Clone repositori proyek ini dari GitHub:
   ```bash
   git clone https://github.com/CC25-CF172/Stuntguard-ChatBot.git
   ```
3. Masuk ke direktori proyek:
   ```bash
   cd Stuntguard-ChatBot
   ```
4. Instal dependensi yang diperlukan menggunakan pip:
   ```bash
   pip install -r requirements.txt
   ```

## Cara Menjalankan Chatbot

1. Pastikan Anda berada di direktori proyek.
2. Buka file notebook `notebook.ipynb` di Jupyter Notebook dan jalankan setiap sel.
3. Pastikan model telah dilatih dan disimpan sebagai `chatbot_model.h5`.
4. Ketik pertanyaan Anda di sel terakhir dan tekan `Shift+Enter` untuk mendapatkan respon dari chatbot.

## Struktur File Proyek

```
Stuntguard-ChatBot/
│
├── notebook.ipynb            # Notebook untuk eksplorasi dan pelatihan model chatbot
├── chatbot_model.h5          # File model chatbot yang telah dilatih (format Keras HDF5)
├── classes.pkl               # Pickle berisi daftar kelas intent
├── words.pkl                 # Pickle berisi daftar kata yang telah diproses
├── stunting_intents.json     # Dataset intent untuk chatbot (format JSON)
├── readme.md                 # Dokumentasi proyek
├── requirements.txt          # Daftar pustaka/dependensi Python yang diperlukan

```

## Contoh Penggunaan

Berikut adalah contoh interaksi dengan chatbot pada sell terakhir:

```python
test_messages = [
"makasih",
"susah makan",
"tinggi badan",
"anak saya susah makan",
"bagaimana cara mengatasi stunting",
"apa itu stunting",
"anak saya pendek",
"anak saya tidak mau makan sayur",
"bagaimana cara meningkatkan tinggi badan anak",
"apa yang harus dilakukan jika anak tidak mau makan",
"saya khawatir anak saya stunting",
"apakah susu bisa membantu pertumbuhan anak",
"berapa tinggi ideal anak usia 5 tahun",
"anak saya sering sakit, apakah itu tanda stunting",
"bagaimana cara mengetahui anak saya stunting",
"  tuliskan pertanyaan baru "
]
```

Tambahkan daftar pertanyaan baru yang ingin Anda uji ke dalam list test_messages, kemudian jalankan skrip dengan menekan tombol Shift + Enter.
