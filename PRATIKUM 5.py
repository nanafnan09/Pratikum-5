
 # Program Manajemen Data Mahasiswa

"""
Program Manajemen Data Mahasiswa
Dibuat dengan menggunakan Dictionary
Fitur:
1. Tambah Data
2. Ubah Data
3. Hapus Data
4. Tampilkan Data
5. Cari Data
6. Keluar
"""

def hitung_nilai_akhir(tugas, uts, uas):
    """
    Menghitung nilai akhir berdasarkan bobot:
    Tugas: 30%, UTS: 35%, UAS: 35%
    """
    return (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)

def tampilkan_menu():
    """
    Menampilkan menu pilihan kepada pengguna.
    """
    print("\nMenu Pilihan:")
    print("1. Tambah Data")
    print("2. Ubah Data")
    print("3. Hapus Data")
    print("4. Tampilkan Data")
    print("5. Cari Data")
    print("6. Keluar")

def tambah_data(data):
    """
    Menambahkan data mahasiswa baru ke dalam dictionary.
    """
    nama = input("Masukkan nama: ")
    tugas = float(input("Masukkan nilai tugas: "))
    uts = float(input("Masukkan nilai UTS: "))
    uas = float(input("Masukkan nilai UAS: "))
    nilai_akhir = hitung_nilai_akhir(tugas, uts, uas)
    data[nama] = {'Tugas': tugas, 'UTS': uts, 'UAS': uas, 'Nilai Akhir': nilai_akhir}
    print(f"Data untuk {nama} berhasil ditambahkan.")

def ubah_data(data):
    """

    Mengubah data mahasiswa berdasarkan nama.
    """

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

def hapus_data(data):
    """

    Menghapus data mahasiswa berdasarkan nama.
    """
    nama = input("Masukkan nama data yang akan dihapus: ")
    if nama in data:
        del data[nama]
        print(f"Data untuk {nama} berhasil dihapus.")
    else:
        print(f"Data dengan nama {nama} tidak ditemukan.")

def tampilkan_data(data):
    """

    Menampilkan seluruh data mahasiswa.
    """

    if data:
        print("\nDaftar Data Mahasiswa:")
        print(f"{'Nama':<15}{'Tugas':<10}{'UTS':<10}{'UAS':<10}{'Nilai Akhir':<15}")
        print("-" * 60)
        for nama, nilai in data.items():
            print(f"{nama:<15}{nilai['Tugas']:<10}{nilai['UTS']:<10}{nilai['UAS']:<10}{nilai['Nilai Akhir']:<15.2f}")
    else:
        print("Tidak ada data yang tersedia.")

def cari_data(data):
    """

    Mencari data mahasiswa berdasarkan nama.
    """

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

def main():
    """

    Fungsi utama untuk menjalankan program.
    """

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

if __name__ == "__main__":
    main()