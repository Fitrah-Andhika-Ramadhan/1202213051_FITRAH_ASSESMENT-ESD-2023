def hitung_kembalian(total_pembayaran, total_belanja):
    kembalian = total_pembayaran - total_belanja
    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

    hasil_kembalian = {}

    for nominal in pecahan_uang:
        jumlah = kembalian // nominal
        if jumlah > 0:
            hasil_kembalian[str(nominal)] = jumlah
            kembalian %= nominal

    return hasil_kembalian

# Contoh penggunaan
total_pembayaran_1, total_belanja_1 = 10000, 7500
total_pembayaran_2, total_belanja_2 = 5000, 1100
total_pembayaran_3, total_belanja_3 = 178000, 90500

hasil_kembalian_1 = hitung_kembalian(total_pembayaran_1, total_belanja_1)
hasil_kembalian_2 = hitung_kembalian(total_pembayaran_2, total_belanja_2)
hasil_kembalian_3 = hitung_kembalian(total_pembayaran_3, total_belanja_3)

print(hasil_kembalian_1)
print(hasil_kembalian_2)
print(hasil_kembalian_3)
