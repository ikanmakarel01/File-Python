print("--- Program Menentukan Jumlah Hari dalam Sebuah Bulan ---")

nomor_bulan = input("Masukkan nomor bulan 1-12: ")
try:
    nomor_bulan = int(nomor_bulan)
    if nomor_bulan == 1:
        print("Januari memiliki 31 hari")
    elif nomor_bulan == 2:
        print("Februari memiliki 28 hari")
    elif nomor_bulan == 3:
        print("Maret memiliki 31 hari")
    elif nomor_bulan == 4:
        print("April memiliki 30 hari")
    elif nomor_bulan == 5:
        print("Mei memiliki 31 hari")
    elif nomor_bulan == 6:
        print("Juni memiliki 30 hari")
    elif nomor_bulan == 7:
        print("Juli memiliki 31 hari")
    elif nomor_bulan == 8:
        print("Agustus memiliki 31 hari")
    elif nomor_bulan == 9:
        print("September memiliki 30 hari")
    elif nomor_bulan == 10:
        print("Oktober memiliki 31 hari")
    elif nomor_bulan == 11:
        print("November memiliki 30 hari")
    elif nomor_bulan == 12:
        print("Desember memiliki 31 hari")
except:
    print("Nomor bulan tidak valid, nomor bulan harus berupa angka")

