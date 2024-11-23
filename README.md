# PRATIKUM-5 Program Manajemen Data Mahasiswa

Nama: Afnan Dika Ramadhan

NIM: 312410518

MATAKULIAH: Bahasa Pemograman

Program Manajemen Data Mahasiswa ini adalah aplikasi berbasis konsol yang menggunakan struktur data dictionary untuk menyimpan, mengelola, dan memanipulasi data mahasiswa. Program ini memiliki beberapa fitur utama seperti menambahkan data, mengubah data, menghapus data, menampilkan data, mencari data, dan keluar dari aplikasi. Berikut adalah penjelasan terperinci setiap bagian kode:

1. Fungsi `hitung_nilai_akhir`
Fungsi ini menghitung nilai akhir mahasiswa berdasarkan formula tertentu:

Tugas: 30%
UTS (Ujian Tengah Semester): 35%
UAS (Ujian Akhir Semester): 35%
```
def hitung_nilai_akhir(tugas, uts, uas):
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

```

2. Fungsi tampilkan_menu
Fungsi ini bertugas menampilkan daftar pilihan menu kepada pengguna. Menu ini menjadi navigasi utama untuk menggunakan fitur program.

```
def tampilkan_menu():
    print("\nMenu Pilihan:")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

```

3. Fungsi `tambah_data`
Fungsi ini memungkinkan pengguna menambahkan data mahasiswa baru. Input berupa nama mahasiswa, nilai tugas, nilai UTS, dan nilai UAS. Setelah data diterima:

Nilai akhir dihitung menggunakan fungsi hitung_nilai_akhir.
Data disimpan ke dalam dictionary dengan nama mahasiswa sebagai key.
```
def tambah_data(data):
    nama = input("Masukkan nama: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data[nama] = {'Tugas': tugas, 'UTS': uts, 'UAS': uas, 'Nilai Akhir': nilai_akhir}
    print(f"Data untuk {nama} berhasil ditambahkan.")

```
4. Fungsi `ubah_data`
Fungsi ini digunakan untuk mengubah data mahasiswa berdasarkan nama.

Pengguna memasukkan nama mahasiswa yang datanya ingin diubah.
Jika nama ditemukan, data baru akan di-input ulang, dan nilai akhir dihitung ulang.
Jika nama tidak ditemukan, program memberikan pesan kesalahan.
```
def ubah_data(data):
    nama = input("Masukkan nama data yang akan diubah: ")
    if nama in data:
        tugas = float(input("Masukkan nilai tugas baru: "))
        uts = float(input("Masukkan nilai UTS baru: "))
        uas = float(input("Masukkan nilai UAS baru: "))
        nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
        data[nama] = {'Tugas': tugas, 'UTS': uts, 'UAS': uas, 'Nilai Akhir': nilai_akhir}
        print(f"Data untuk {nama} berhasil diubah.")
    else:
        print(f"Data dengan nama {nama} tidak ditemukan.")
```

5.Fungsi`hapus_data`
Fungsi ini menghapus data mahasiswa berdasarkan nama.

Jika nama ditemukan, data mahasiswa dihapus dari dictionary.
Jika nama tidak ditemukan, program memberikan pesan kesalahan.
```
def hapus_data(data):
    nama = input("Masukkan nama data yang akan dihapus: ")
    if nama in data:
        del data[nama]
        print(f"Data untuk {nama} berhasil dihapus.")
    else:
        print(f"Data dengan nama {nama} tidak ditemukan.")

```

6.Fungsi `tampilkan_data`
Fungsi ini menampilkan seluruh data mahasiswa dalam format tabel.

Jika data kosong, akan menampilkan pesan "Tidak ada data yang tersedia".
Data ditampilkan dengan format rapi, termasuk nama, nilai tugas, nilai UTS, nilai UAS, dan nilai akhir.

```
def tampilkan_data(data):
    if data:
        print("\nDaftar Data Mahasiswa:")
        print(f"{'Nama':<15}{'Tugas':<10}{'UTS':<10}{'UAS':<10}{'Nilai Akhir':<15}")
        print("-" * 60)
        for nama, nilai in data.items():
            print(f"{nama:<15}{nilai['Tugas']:<10}{nilai['UTS']:<10}{nilai['UAS']:<10}{nilai['Nilai Akhir']:<15.2f}")
    else:
        print("Tidak ada data yang tersedia.")

```

7.Fungsi `cari_data`
Fungsi ini mencari data mahasiswa berdasarkan nama.

Jika nama ditemukan, data mahasiswa ditampilkan.
Jika tidak ditemukan, pesan kesalahan diberikan.
```
def cari_data(data):
    nama = input("Masukkan nama yang dicari: ")
    if nama in data:
        print("\nData Ditemukan:")
        print(f"Nama        : {nama}")
        print(f"Nilai Tugas : {data[nama]['Tugas']}")
        print(f"Nilai UTS   : {data[nama]['UTS']}")
        print(f"Nilai UAS   : {data[nama]['UAS']}")
        print(f"Nilai Akhir : {data[nama]['Nilai Akhir']:.2f}")
    else:
        print(f"Data dengan nama {nama} tidak ditemukan.")

```

8.Fungsi `main`
Fungsi utama untuk menjalankan program:

Membuat dictionary kosong untuk menyimpan data mahasiswa.
Menampilkan menu pilihan menggunakan tampilkan_menu.
Memproses input pengguna untuk memilih fitur yang diinginkan.
Program berjalan hingga pengguna memilih opsi "Keluar" (menu 6).
```
def main():
    data_mahasiswa = {}
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-6): ")
        if pilihan == '1':
            tambah_data(data_mahasiswa)
        elif pilihan == '2':
            ubah_data(data_mahasiswa)
        elif pilihan == '3':
            hapus_data(data_mahasiswa)
        elif pilihan == '4':
            tampilkan_data(data_mahasiswa)
        elif pilihan == '5':
            cari_data(data_mahasiswa)
        elif pilihan == '6':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

```

Cara Kerja Program:

Program dimulai dengan memanggil fungsi main.

Pengguna memilih menu dengan memasukkan angka (1-6).

Berdasarkan pilihan, program menjalankan fungsi terkait.

Program terus berjalan hingga pengguna memilih menu Keluar (6).

Program ini cocok digunakan untuk latihan pengelolaan data menggunakan dictionary dan manipulasi data berbasis teks.

# Flowchart Pratikum 5
![Foto](https://github.com/nanafnan09/Pratikum-5/blob/12560e75979712f7565a712e496a792fa913cc87/FLOWCHART%20PRATIKUM-5.png)






