##  CTF Name: Deary Diary (medium)

### Description:
If you can find the flag on this disk image, we can close the case for good!

### Hint:
If you're observing binary data raw in the terminal you may be misled about the contents of a block.

### Analysis:
Pada tantangan kali ini diberikan file disk.flag.img.gz yang harus di ekstrak menggunakan gunzip setelah diekstrak terdapat file disk.flag.img yang merupakan file disk untuk menganalisa file itu, langkah-langkahnya sebagai berikut:

### Solution:

 1. **Ekstrak file tadi dengan menggunakan gunzip dan cek jenis file nya menggunakan command file disk.flag.img**

	![f](./documentation/Screenshot%202025-02-06%20170920.png)

	![f](./documentation/Screenshot%202025-02-06%20171208.png)

	setelah dicek jenis file yang sudah diekstrak tersebut adalah disk dengan partisi MBR(Master Boot Record) untuk menganalisa disk ini saya menggunakan tools autopsy

2. **Membuka website autopsy dengan command sudo autopsy**

	![f](./documentation/Screenshot%202025-02-06%20172159.png)

	![f](./documentation/Screenshot%202025-02-06%20174501.png)

3. **Membuat case baru pada autopsy**
	
	![f](./documentation/Screenshot%202025-02-06%20174522.png)
	
	![f](./documentation/Screenshot%202025-02-06%20174638.png)

	![f](./documentation/Screenshot%202025-02-06%20174651.png)

4. **Setelah membuat case pada autopsy selanjutnya menambahkan image yang mau di analisa**

	![f](./documentation/Screenshot%202025-02-06%20174749.png)

	selanjutnya pilih tombol ADD IMAGE FILE
	
	![f](./documentation/Screenshot%202025-02-06%20174920.png
	)
	
	setelah itu pilih path disk yang mau di analisa kemudian klik next
	
	![f](./documentation/Screenshot%202025-02-06%20175357.png)	

	klik tombol add kemudian ok

	![f](./documentation/Screenshot%202025-02-06%20175426.png)

	![f](./documentation/Screenshot%202025-02-06%20175520.png)

5. **Setelah menambahkan image selanjutnya menganalisa image tersebut dengan klik tombol ANALYZE**

	![f](./documentation/Screenshot%202025-02-06%20175622.png)
	
	selanjutnya pilih menu keyword search pada navbar diatas lalu masukan kata kunci yang mau dicari dan klik search, saya disini akan mencari file txt yang biasanya itu berisi flag.

	![f](./documentation/Screenshot%202025-02-06%20180005.png)

	setelah melakukan pencarian ada banyak file txt yang bisa di analisa hex dan ascii nya

6. **Melakukan analisa terhadap file dengan extension txt**
	
	setelah saya melakukan analisa terhadap beberapa file saya menemukan hal menarik pada unit 1423344 yang berisi potongan flag yang saya cari flag tersebut ada di dalam file bernama innocuouss-file.txt 

	![f](./documentation/Screenshot%202025-02-06%20171953.png)

	![f](./documentation/Screenshot%202025-02-06%20172045.png)
	
	setelah saya melakukan anilsa pada file innocuouss-file.txt   saya mendapatkan semua potongan flag nya mulai dari unit 1423344 - 1423488 yang jika semua potongan itu digabung membentuk flag yaitu: **picoCTf{1_533_n4m35_80d24b30}**

	
	
	

	
	
