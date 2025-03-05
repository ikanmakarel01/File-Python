def konversi_ke_hari(jam, menit):
    total_jam = jam + menit / 60
    hari = total_jam / 24
    return hari

jam = int(input("Masukkan jumlah jam: "))
menit = int(input("Masukkan jumlah menit: "))

hasil = konversi_ke_hari(jam, menit)
print(f"{jam} jam dan {menit} menit sama dengan {hasil} hari")
