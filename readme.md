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
2. Pastikan model telah dilatih dan disimpan sebagai `chatbot_model.h5`.
3. Buat virtual env dengan perintah
   ```shell
    py -m venv .env
   ```
4. Aktifkan virtual env dengan perintah
   ```shell
   .env\Scripts\Activate.ps1
   ```
5. install requirements.txt
   ```shell
   pip install -r requirements.txt
   ```
6. Setelah requirements.txt terinstal, ketik perintah di terminal
   ```shell
   py
   import nltk
   nltk.download('punkt')
   nltk.download('wordnet')
   ```
7. jalankan file chatBot.py dengan perintah
   ```shell
   py chatBot.py
   ```

## Struktur File Proyek

```
Stuntguard-ChatBot/
│
├── notebook.ipynb            # Notebook eksplorasi data, preprocessing, dan pelatihan model chatbot
├── chatbot_model.h5          # File model chatbot hasil pelatihan dalam format HDF5 (Keras)
├── classes.pkl               # File pickle berisi daftar label intent (kelas-kelas chatbot)
├── words.pkl                 # File pickle berisi kosakata (daftar kata unik yang telah diproses)
├── stunting_intents.json     # Dataset intent dan respons chatbot bertema stunting (format JSON)
├── chatBot.py                # Skrip chatbot siap pakai di terminal (versi interaktif untuk input manual)
├── readme.md                 # Dokumentasi proyek: deskripsi, cara kerja, petunjuk instalasi & penggunaan
├── requirements.txt          # Daftar pustaka Python yang dibutuhkan (untuk `pip install -r requirements.txt`)


```

## Contoh Penggunaan

Berikut adalah contoh interaksi dengan chatbot pada terminal:

```shell
Halo! Saya adalah Chatbot Stunting Asisten. Ketik 'keluar' untuk mengakhiri.

Anda :
```

Ketikkan pesan anda pada terminal
