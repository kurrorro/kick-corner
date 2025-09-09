# Kick Corner — Django Web App

Aplikasi web berbasis Django untuk menampilkan daftar produk olahraga.  
Dibuat untuk tugas mata kuliah **PBP**.

**Link Deploy (PWS):** https://keisha-vania-kickcorner.pbp.cs.ui.ac.id/

- **Shop**: Kick Corner  
- **NPM**: 2406437331  
- **Nama**: Keisha Vania Laurent  
- **Kelas**: PBP B  

## Struktur Proyek
kick-corner/
├─ kick_corner/
│ ├─ settings.py
│ ├─ urls.py
│ ├─ asgi.py
│ └─ wsgi.py
├─ main/
│ ├─ migrations/
│ ├─ templates/
│ │ └─ main.html
│ ├─ models.py
│ ├─ views.py
│ ├─ urls.py
│ ├─ apps.py
│ ├─ tests.py
│ └─ admin.py
├─ assets/
├─ manage.py
└─ requirements.txt

# Tugas Individu 2

## Implementasi checklist

1. **Membuat proyek dan app**
   - Memulai dengan membuat repo bernama `kick-corner` berisi proyek Django dengan package utama `kick_corner`.
   - Lalu membuat aplikasi `main` dan mendaftarkannya pada `INSTALLED_APPS` di `kick_corner/settings.py` agar dikenali oleh Django.

2. **Menghubungkan routing proyek ke app**
   - Di `kick_corner/urls.py`, saya mengarahlan rute utama (root path) ke `include('main.urls')`.  
   - Ini memastikan setiap request ke root situs diteruskan ke routing milik app `main`, supaya logika halaman utama terpusat di app.

3. **Merancang model `Product`**
   - Model disimpan di `main/models.py` dengan **UUID** sebagai primary key agar id unik. 
   - Atribut yang dibuat:
     - `name`, `price`, `description` untuk informasi dasar produk.
     - `thumbnail` sebagai URL gambar yang bersifat opsional (boleh kosong).
     - `category` memakai **`choices`** (`jersey`, `shoes`, `ball`, `accessory`, `training`, `nutrition`, `merchandise`).
     - `is_featured` sebagai penanda produk unggulan.
     - `stock`, `brand`, dan `size` untuk kebutuhan domain toko olahraga (ketersediaan, merek, ukuran).  
   - `__str__` mengembalikan nama produk agar mudah dibaca di admin/log.
   - Setelah itu, saya membuat dan menerapkan **migrasi** agar skema database sinkron dengan definisi model.

4. **Menyusun fungsi pada `views.py`**
   - Di `main/views.py` saya membuat fungsi show_main yang:
     - Mengambil semua data `Product`.
     - Menyusun context (shop, NPM, nama, kelas, products).
     - Merender ke `main.html` agar data tampil rapi.

5. **Membuat routing app**
   - Di `main/urls.py`, saya memetakan path root ('') ke `show_main`.
   - Dengan begitu, ketika pengunjung membuka halaman utama, langsung diarahkan ke view yang menampilkan identitas dan daftar produk.

6. **Membangun template untuk tampilan**
   - Di `main/templates/main.html`, saya menampilkan:
     - Identitas (shop, NPM, nama, kelas) di header.
     - Daftar produk: gambar (jika ada), nama, label kategori via `{{ p.get_category_display }}`, brand (jika ada), penanda featured, harga, dan deskripsi.
     - Fallback “There is no product yet.” jika database masih kosong.

7. **Deployment ke PWS**
   - Saya mengunggah kode ke PWS sesuai alur platform:
     - Membuat proyek PWS
     - Atur environment variables
     - Menambahkan URL deployment PWS pada `ALLOWED_HOSTS`
     - Commit perubahan dan jalankan project command dari PWS

8. **Membuat README.md**
   - Saya menambahkan tautan PWS dan menjelaskan keseluruhan proses di atas dan juga menjelaskan mengenai alur request/response (kaitan `urls.py` → `views.py` → `models.py` → template), peran `settings.py`, cara kerja migrasi, alasan memilih Django, serta feedback untuk asisten dosen. (Akan ada di bawah ini).

## Bagan arsitektur request/response

![Django MVT Flow](assets/django-diagram.webp)

Django adalah web framework berbasis Python yang mengikuti pola **Model–View–Template (MVT)**. Pola ini memisahkan antara logika data (model), logika aplikasi (view), dan tampilan (template). Alur request–response di Django dapat dijelaskan sebagai berikut:

1. **Client → Server → Django**  
   User mengirimkan request melalui browser. Request ini diteruskan ke aplikasi Django oleh server.

2. **URL (`urls.py`)**  
   Django memiliki URL dispatcher yang bertugas mencocokkan path request dengan pola yang ada di `urls.py`. Misalnya, permintaan ke `/` diarahkan ke fungsi `show_main` di `views.py`.

3. **View (`views.py`)**  
   View bertugas memproses request.
   - Mengambil data dari model (`models.py`),
   - Menyusun context yang berisi data dan identitas,
   - Memanggil template untuk merender halaman.  

   Di proyek ini, `show_main` mengambil daftar produk dari model `Product` dan meneruskannya ke template `main.html`.

4. **Model (`models.py`)**  
   Model merepresentasikan struktur data di database. Misalnya, `Product` dengan field `name`, `price`, `category`, dll. View menggunakan ORM Django untuk berinteraksi dengan model, misalnya `Product.objects.all()` untuk mengambil semua produk.

5. **Template (`main.html`)**  
   Template merender data menjadi HTML. Context dari view (identitas dan daftar produk) ditampilkan dalam format halaman web.

6. **Response kembali ke Client**  
   Hasil render berupa HTML dikirim kembali ke browser, lalu ditampilkan ke user sebagai halaman web.

### Hubungan antar file

- **`urls.py`** → menghubungkan request dengan fungsi view yang tepat.  
- **`views.py`** → berisi logika aplikasi, mengambil data dari model, lalu menyiapkan context.  
- **`models.py`** → merepresentasikan struktur database, menyimpan dan mengelola data.  
- **Template (HTML)** → menampilkan data ke user dengan format yang diinginkan.  

Dengan arsitektur ini, Django menyederhanakan proses membangun aplikasi web yang kompleks dengan cara yang terstruktur, cepat, dan aman.

Referensi: https://medium.com/@dhanendra73984/understanding-django-architecture-workflow-advantages-and-beginners-setup-guide-ad77f390bcc3

## Peran `settings.py` dalam proyek Django

File `settings.py` berfungsi sebagai pusat konfigurasi proyek Django. Semua pengaturan inti aplikasi didefinisikan di sini, mulai dari keamanan, daftar aplikasi, hingga database dan template. Di proyek ini, `settings.py` mengatur beberapa hal penting:

1. **Keamanan**: `SECRET_KEY` digunakan untuk operasi kriptografi, `DEBUG` menentukan mode development atau production, dan `ALLOWED_HOSTS` membatasi domain yang boleh mengakses aplikasi (termasuk domain PWS).

2. **Aplikasi & Middleware**: `INSTALLED_APPS` mendaftarkan aplikasi yang digunakan (misalnya `main`), sedangkan `MIDDLEWARE` berisi komponen perantara seperti autentikasi, session, dan proteksi CSRF.

3. **Routing & Template**: `ROOT_URLCONF` menunjuk ke `kick_corner/urls.py`, sementara `TEMPLATES` mengatur rendering HTML agar Django bisa menemukan file seperti `main/templates/main.html`.

4. **Database**: Saat development, proyek menggunakan SQLite. Saat production, konfigurasi PostgreSQL digunakan, dengan kredensial diambil dari environment variables (`.env` atau PWS).

5. **Lain-lain**: File ini juga mengatur validasi password, bahasa (`LANGUAGE_CODE`), zona waktu (`TIME_ZONE`), static files (`STATIC_URL`), dan tipe primary key default untuk model.

Singkatnya, `settings.py` adalah **otak konfigurasi** proyek Django. Tanpa file ini, Django tidak tahu harus menggunakan aplikasi apa, database mana, atau bagaimana cara merender template dan mengelola keamanan aplikasi.

## Cara kerja migrasi database di Django

Migrasi database di Django adalah mekanisme untuk menjaga agar struktur database selalu sesuai dengan definisi model pada kode. Prosesnya berjalan dalam beberapa tahap:

1. **Membuat Migrasi**  
   Setiap kali ada perubahan pada `models.py` (misalnya menambah field, mengubah tipe data, atau membuat model baru), Django bisa mendeteksi perubahan ini dan membuat berkas migrasi. Berkas ini berisi instruksi bagaimana database harus diubah.

2. **Menerapkan Migrasi**  
   Saat migrasi dijalankan, Django membaca berkas migrasi tersebut dan mengeksekusi instruksi di database. Contohnya: membuat tabel baru untuk model `Product`, menambah kolom `brand`, atau mengubah properti field tertentu.

3. **Mencatat Status Migrasi**  
   Django menyimpan catatan semua migrasi yang sudah dijalankan di tabel khusus bernama `django_migrations`. Dengan begitu, Django tahu migrasi mana yang sudah diterapkan dan mana yang belum.

Dengan sistem ini, developer bisa mengembangkan aplikasi dengan lebih fleksibel. Struktur database dapat terus berkembang mengikuti perubahan kode, tanpa perlu menulis query SQL manual. Migrasi juga memastikan semua developer memiliki struktur database yang konsisten.

## Mengapa Django cocok jadi framework awal untuk belajar?

Menurut saya, Django dipilih sebagai framework awal dalam pembelajaran karena sifatnya yang serba lengkap dan terstruktur. Framework ini sudah menyediakan banyak fitur bawaan seperti autentikasi, ORM untuk interaksi dengan database, serta proteksi keamanan, sehingga mahasiswa tidak perlu menambahkan komponen tambahan untuk memulai. 

Selain itu, Django menerapkan pola Model–View–Template (MVT) yang membantu memahami pemisahan antara data, logika, dan tampilan secara jelas. Hal ini sangat bermanfaat untuk melatih pola pikir terstruktur dalam membangun aplikasi. 

Dokumentasi yang lengkap, komunitas yang besar, serta penggunaannya yang luas di industri juga menjadi alasan mengapa Django relevan untuk dipelajari sejak awal. Django dapat memberikan pengalaman belajar yang mudah diikuti pemula dan tetap memberikan gambaran nyata tentang bagaimana aplikasi skala besar dikembangkan.

## Apakah ada feedback untuk asisten dosen tutorial 1?

Tidak ada.