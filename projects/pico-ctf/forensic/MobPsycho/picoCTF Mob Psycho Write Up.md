##  CTF Name: Mob Psycho (medium)

### Description:
Can you handle APKs?

### Hint:

 1. Did you know you can `unzip` APK files?
 2. Now you have the whole host of shell tools for searching these files.

### Analysis:
pada tantangan kali ini diberikan file apk yang bisa di unzip secara normal di kali linux menggunakan unzip setelah di unzip ada banyak sekali sub folder yang ada didalam apk ini strategi yang saya lakukan untuk mendapatkan flag nya menggunakan strings dan grep untuk menemukan lokasi flag nya berada.

### Solution:

 1. **Unzip file mobpyscho.apk dan menyimpan nya di folder apk**
 
	 ![foto](./documentation/Screenshot%202025-02-05%20141719.png)

2. **Mencari flag menggunakan strings * | grep flag**

	![foto](./documentation/Screenshot%202025-02-05%20142001.png)

	setelah saya melakukan pencarian menggunakan command diatas saya menemukan semua string yang mengandung kata flag di dalam nya ada satu hal menarik disini yaitu file flag.txt yang berada di res/color/flag.txt

3. **Membaca isi flag.txt menggunakan cat**
 
	![foto](./documentation/Screenshot%202025-02-05%20142332.png)

	setelah saya baca flag.txt seperti nya isi flag.txt ini dienskripsi dengan suatu encoder.

4. **Mendecode isi flag.txt menggunakan website cyberchef**

	![foto](./documentation/Screenshot%20(365).png)

	hebatnya menggunakan website cyberchef ini bisa secara otomatis mendecode kode tersebut sesuai dengan metode encode nya, kode dari file flag.txt itu di encode menggunakan hex setelah di decode saya mendapatkan flag nya yaitu: **picoCTF{ax8mC0RU6ve_NX85l4ax8mCl_b112ae57}**
