##  CTF Name: Permissions (medium)

### Description:
Can you read files in the root file?The system admin has provisioned an account for you on the 
main server:
`ssh -p 53821 picoplayer@saturn.picoctf.net` 
Password:  `NBD+zO8s4y`
Can you login and read the root file?

### Hint:
What permissions do you have?

### Analysis:
berdasarkan deskripsi dan hint yang dikasih tantangan kali ini bertujuan untuk mengakses file dengan hak root

### Solution:
1. Langkah pertama connect ke server menggunakan ssh dan password yang diberikan 

	![f](./documentation/Screenshot%202025-02-23%20085926.png)

2. Cek direktori yang ada menggunakan ls dan juga cek login sebagai siapa menggunakan whoami dan coba akses root menggunakan sudo su
	
	![f](./documentation/Screenshot%202025-02-23%20090409.png)
	
	dapat dilihat bahwa saya login sebagai picoplayer dan tidak diizinkan untuk mengakses root melalui sudo su

3. Mengecek hak akses apa aja yang dapat dijalankan oleh user menggunakan command sudo -l dan masukkan password yang dikasih

	![f](./documentation/Screenshot%202025-02-23%20091855.png)

	dapat dilihat disini bahwa hak akses yang dipunya oleh user sangat terbatas tapi ada hal menarik pada bagian bawah yaitu user bisa menjalankan text editor vim sebagai superuser(root) dengan ini saya bisa membuka shell dengan akses root di vim

4. Membuat script eksekusi untuk membuka shell menggunakan akses root

	![f](./documentation/Screenshot%202025-02-23%20090852.png)

5. Menjalankan script dengan sudo vi script

	![f](./documentation/Screenshot%202025-02-23%20091023.png)

	dan yap sekarang saya berhasil login sebagai root, setelah saya menjelajahi direktori yang ada pada direktori root terdapat file .flag.txt

6. Membaca file flag.txt tersebut menggunakan cat

	![f](./documentation/Screenshot%202025-02-23%20091057.png)
	
	didapatkan flag nya yaitu: **picoCTF{uS1ng_v1m_3dit0r_1cee9dcb}**
	

	
	


