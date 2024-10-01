# pengisian data
nama = input("masukkan nama anda : ")
hari = input("masukkan hari: ")
uang = int(input("uang yang anda miliki: "))

# harga tiket perhari
harga_tiket = 0
if hari in ['Senin', 'Selasa', 'Rabu', 'Kamis']:
    harga_tiket = 40000
elif hari == 'Jumat':
    harga_tiket = 45000
elif hari == 'Sabtu':
    harga_tiket = 55000
elif hari == 'Minggu':
    harga_tiket = 60000


# melihat apakah uang cukup
if uang < harga_tiket:
    print(f"{nama},uang anda kurang untuk membeli tiket pada hari {hari}.")
else:
    print(f"{nama}, uang anda cukup untuk membeli tiket pada hari {hari}.")

