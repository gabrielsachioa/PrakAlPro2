# LATIHAN 2.3
minggu = 5
gaji = int(input("Gaji per jam yang Anda inginkan: "))
jumlahJamKerja = int(input("Jumlah jam kerja selama 1 minggu: "))

pendapatanKotor = gaji * jumlahJamKerja * minggu
pajak = 0.14 * pendapatanKotor
pendapatanBersih = pendapatanKotor - pajak

bajuAksesoris = 0.1 * pendapatanBersih
alatTulis = 0.01 * pendapatanBersih
sisaUang = pendapatanBersih - (bajuAksesoris + alatTulis)

uangSedekah = 0.25 * sisaUang
sedekahAnakYatim = 0.3 * uangSedekah
sedekahKaumDhuafa = uangSedekah - sedekahAnakYatim

print(f"Pendapatan Budi selama libur musim panas sebelum melakukan pembayaran pajak = Rp. {pendapatanKotor}")
print(f"Pendapatan Budi selama libur musim panas setelah melakukan pembayaran pajak = Rp. {pendapatanBersih}")
print(f"Jumlah uang yang akan Budi habiskan untuk membeli pakaian dan aksesoris = Rp. {bajuAksesoris}")
print(f"Jumlah uang yang akan Budi habiskan untuk membeli alat tulis = Rp. {alatTulis}")
print(f"Jumlah uang yang akan Budi sedekahkan = Rp. {uangSedekah}")
print(f"Jumlah uang yang akan diterima anak yatim = Rp. {sedekahAnakYatim}")
print(f"Jumlah uang yang akan diterima kaum dhuafa = Rp. {sedekahKaumDhuafa}")