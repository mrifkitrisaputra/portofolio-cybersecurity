# Keylogger dengan Integrasi Telegram

Proyek ini adalah keylogger sederhana yang mengirimkan hasil input keyboard ke bot Telegram melalui API. Program ini terdiri dari dua file:
1. **keylogger.py** - Script Python utama.
2. **keylogger.exe** - Versi executable dari keylogger yang dapat dijalankan langsung.

---

## **Fitur Utama**
- Mengirim hasil input keyboard ke bot Telegram.
- Dukungan perintah kontrol dari bot Telegram menggunakan command `/start` dan `/stop`.
- Buffer otomatis dikirim saat tombol Enter ditekan.

---

## **Persyaratan**
- Python 3.x (jika menggunakan file `keylogger.py`).
- Library tambahan:
  - `pynput`
  - `requests`
- Akses ke bot Telegram (token bot dan chat ID).
- File executable `keylogger.exe` (jika tidak ingin menggunakan Python).

---

## **Cara Menjalankan Program**

### **1. Menjalankan dengan Python**
Jika ingin menjalankan program dari source code `keylogger.py`, ikuti langkah-langkah berikut:

1. **Clone repositori** ini ke komputer kamu:
   ```bash
   git clone https://github.com/username/repository-name.git
   cd repository-name
   ```

2. **Install library yang dibutuhkan**:
   ```bash
   pip install pynput requests
   ```

3. **Jalankan script Python**:
   ```bash
   python keylogger.py
   ```

### **2. Menjalankan File Executable (keylogger.exe)**
Jika tidak memiliki Python, cukup jalankan file `keylogger.exe` dengan langkah berikut:

1. **Unduh file `keylogger.exe`** dari repositori.
2. **Jalankan file `keylogger.exe`** dengan double-click.

### **3. Mengubah keylogger.py Menjadi File Executable (.exe)**
Jika kamu ingin membuat file executable dari `keylogger.py` menggunakan PyInstaller, ikuti langkah-langkah di bawah ini:

1. **Pastikan PyInstaller sudah terpasang**. Jika belum, instal menggunakan pip:
   ```bash
   pip install pyinstaller
   ```

2. **Buka terminal atau command prompt** di direktori yang sama dengan `keylogger.py`.

3. **Jalankan perintah berikut** untuk membuat file executable tanpa console:
   ```bash
   python -m PyInstaller --onefile --noconsole --clean keylogger.py
   ```
   - **`--onefile`**: Menggabungkan semua file ke dalam satu file executable.
   - **`--noconsole`**: Menyembunyikan jendela terminal saat program berjalan.
   - **`--clean`**: Membersihkan file sementara yang dihasilkan selama proses build.

4. **Hasil file executable** akan berada di dalam folder `dist` yang dibuat otomatis:
   - Path: `dist/keylogger.exe`

5. **Jalankan file executable** dengan double-click pada `keylogger.exe` di dalam folder `dist`.

---

## **Konfigurasi Bot Telegram**

1. **Buat bot Telegram** melalui BotFather:
   - Kirim perintah `/newbot` ke BotFather.
   - Salin **token bot** yang diberikan.

2. **Dapatkan chat ID** dengan mengakses:
   ```
   https://api.telegram.org/bot<TOKEN_BOT>/getUpdates
   ```
   Gantilah `<TOKEN_BOT>` dengan token yang diperoleh. 

3. **Ubah konfigurasi program**:
   - Masukkan **token bot** dan **chat ID** ke dalam variabel berikut di file `keylogger.py`:
     ```python
     TELEGRAM_BOT_TOKEN = "<TOKEN_BOT>"
     CHAT_ID = "<CHAT_ID>"
     ```

---

## **Perintah Kontrol**

Saat program berjalan, kamu bisa mengontrolnya melalui bot Telegram:
- **`/start`** : Memulai keylogger.
- **`/stop`** : Menghentikan keylogger.

---

## **Video Testing**
Untuk melihat program ini beraksi, silakan tonton video testing di link berikut:
[**Video Testing Keylogger**](https://drive.google.com/file/d/1ueR7ZtgGyrBK5xrHhK-OqF5W8WdMixUP/view?usp=sharing)

---


## **Lisensi**
Proyek ini dilisensikan di bawah [MIT License](LICENSE).
