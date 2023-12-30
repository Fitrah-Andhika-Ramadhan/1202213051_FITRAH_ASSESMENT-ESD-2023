def hitung_kembalian(total_pembayaran, total_belanja):
    kembalian = total_pembayaran - total_belanja

    # Pecahan uang yang tersedia
    pecahan_uang = [100000, 50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100]

    hasil_kembalian = {}

    for pecahan in pecahan_uang:
        if kembalian >= pecahan:
            jumlah_pecahan = kembalian // pecahan
            kembalian %= pecahan
            hasil_kembalian[str(pecahan)] = jumlah_pecahan

    return hasil_kembalian

# penggunaan fungsi tampilkan_tabel untuk menampilkan tabel    

def tampilkan_tabel(cases):
    print("{:<20} {:<20} {:<30}".format("Total Pembayaran", "Total Belanja", "Output"))
    print("-" * 70)

    for case in cases:
        total_pembayaran, total_belanja = case[0], case[1]
        kembalian = hitung_kembalian(total_pembayaran, total_belanja)
        print("{:<20} {:<20} {}".format(total_pembayaran, total_belanja, kembalian))

# penggunaan array untuk menyimpan tabel-tabel yang akan ditampilkan
cases = [
    (10000, 7500),
    (5000, 1100),
    (178000, 90500)
]

tampilkan_tabel(cases)
