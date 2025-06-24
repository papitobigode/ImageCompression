# ImageCompression
Image Compression Project - Aljabar Linier Kelompok 6  
- ATAA ARKAN TSANY (L0124148)
- DEFFA ROHMAN WICAKSONO (L0124149)
- SALMAN ABDUSSALAM (L0124156)


Cara Menjalankan Program Image Compression:
-------------------------------------------
1. Buka folder project, kemudian buka folder bernama "src" (jika disediakan).  
   Jika tidak ada folder khusus, langsung buka folder yang berisi file "app.py".

2. Jalankan file "app.py" menggunakan terminal atau command prompt:
   > python app.py

3. Setelah dijalankan, akan muncul informasi bahwa server berjalan di `http://127.0.0.1:5000/`.

4. Buka browser dan akses alamat tersebut untuk membuka aplikasi.

*Catatan:*
Jika ini pertama kali dijalankan, pastikan Anda sudah menginstall modul yang diperlukan:
> pip install flask pillow numpy

Cara Menggunakan Program Image Compression:
-------------------------------------------
1. Klik tombol **Choose File** untuk mengunggah gambar yang ingin dikompresi.  
   Format gambar yang didukung: `.jpg`, `.jpeg`, dan `.png`.

2. File gambar uji coba juga telah disediakan di folder bernama **test** (jika tersedia).

3. Masukkan angka pada kolom **Image Compression Rate (%)**.  
   Semakin kecil nilainya, maka kompresi akan semakin besar (gambar menjadi lebih kabur).

4. Klik tombol **Submit** untuk memulai proses kompresi.

5. Tunggu beberapa detik. Setelah proses selesai:
   - Gambar asli dan hasil kompresi akan ditampilkan.
   - Informasi waktu kompresi dan rasio ukuran hasil kompresi juga ditampilkan.
   - Anda bisa klik kanan pada gambar hasil kompresi untuk menyimpannya.




