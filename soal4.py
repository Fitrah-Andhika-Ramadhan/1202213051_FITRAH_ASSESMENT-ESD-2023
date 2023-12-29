def cek_duplikat(data):
    # Menggunakan set untuk melacak elemen yang sudah ditemui
    seen = set()
    
    # Iterasi melalui setiap elemen dalam data
    for angka in data:
        # Jika angka sudah ada dalam set, berarti ada duplikat
        if angka in seen:
            return True
        else:
            # Tambahkan angka ke set
            seen.add(angka)
    
    # Tidak ada duplikat yang ditemukan
    return False

# Contoh penggunaan dengan data yang diberikan
data_angka = [20, 1, 3, 2, 4, 6, 8, 5, 7, 9, 11, 13, 15, 10, 12, 14, 16, 18, 20, 17, 19]
hasil_cek = cek_duplikat(data_angka)

# Output hasil
print(hasil_cek)
