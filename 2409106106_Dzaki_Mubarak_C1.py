# Input data
nama = input("Masukkan nama lengkap: ")
nim = input("Masukkan NIM: ")
harga_gula = float(input("Masukkan harga gula (Rp): "))

# Persentase diskon
diskon_gulaku = 7 / 100
diskon_manis_kita = 11 / 100
diskon_gunung_madu = 13 / 100

# Menghitung diskon
diskon_gulaku_nominal = (harga_gula * diskon_gulaku)
diskon_manis_kita_nominal = (harga_gula * diskon_manis_kita)
diskon_gunung_madu_nominal = (harga_gula * diskon_gunung_madu)

# Menghitung harga setelah diskon
harga_setelah_diskon_gulaku = harga_gula - diskon_gulaku_nominal
harga_setelah_diskon_manis_kita = harga_gula - diskon_manis_kita_nominal
harga_setelah_diskon_gunung_madu = harga_gula - diskon_gunung_madu_nominal

# Output
print(nama + " dengan NIM " + nim + " ingin membeli gula seharga Rp " + str(int(harga_gula)))
print("Jika dia membeli Gulaku ia harus membayar Rp " + str(int(harga_setelah_diskon_gulaku)) + " setelah mendapat diskon 7%.")
print("Jika dia membeli Manis Kita ia harus membayar Rp " + str(int(harga_setelah_diskon_manis_kita)) + " setelah mendapat diskon 11%.")
print("Jika dia membeli Gunung Madu ia harus membayar Rp " + str(int(harga_setelah_diskon_gunung_madu)) + " setelah mendapat diskon 13%.")
