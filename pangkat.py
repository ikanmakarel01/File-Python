def perpangkatan(angka, pangkat):
    hasil = 1  
    for i in range(pangkat):  
        hasil *= angka  
    return hasil  

angka = int(input("Masukkan angka: "))
pangkat = int(input("Masukkan pangkatnya: "))


print(f"Hasil dari {angka}^{pangkat} adalah {perpangkatan(angka, pangkat)}")

