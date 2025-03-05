tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi + 1):
    spasi = ' ' * (tinggi - i)
    bintang = '#' * (2*i - 1)
    print(spasi + bintang)


tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(1, tinggi + 1):
    spasi = ' ' * (tinggi - i)  # Menghitung spasi di sebelah kiri
    pagar = '#' * i              # Menghitung jumlah #
    print(spasi + pagar)


tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(tinggi, 0, -1):
    spasi = ' ' * (tinggi - i)  # Spasi bertambah setiap baris
    pagar = '#' * i             # Jumlah # berkurang
    print(spasi + pagar)

tinggi = int(input("Masukkan tinggi segitiga: "))

for i in range(tinggi, 0, -1):
    spasi = ' ' * (tinggi - i)       # Spasi di sebelah kiri
    pagar = '#' * (2 * i - 1)        # Jumlah # ganjil
    print(spasi + pagar)
