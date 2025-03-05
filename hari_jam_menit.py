def konversi_hari_ke_jam_menit(hari):
    total_menit = round(hari * 24 * 60)  # Konversi hari ke menit dan bulatkan
    jam = total_menit // 60              # Hitung jam (pembagian integer)
    menit = total_menit % 60             # Hitung sisa menit
    return jam, menit

# Input dari pengguna
hari = float(input("Masukkan jumlah hari: "))

# Konversi dan tampilkan hasil
jam, menit = konversi_hari_ke_jam_menit(hari)
print(f"{hari} hari sama dengan {jam} jam dan {menit} menit")
