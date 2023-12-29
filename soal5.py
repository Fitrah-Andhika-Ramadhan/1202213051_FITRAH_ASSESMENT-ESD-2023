def hitung_kombinasi_username(nama_lengkap):
    # Gabungkan nama tanpa spasi dan ubah menjadi lowercase
    nama_gabung = nama_lengkap.replace(" ", "").lower()
    
    # Inisialisasi jumlah kombinasi
    jumlah_kombinasi = 0
    
    # Hitung jumlah kombinasi untuk setiap panjang username (1 hingga 6)
    for panjang_username in range(1, min(len(nama_gabung), 6) + 1):
        # Hitung jumlah kombinasi dengan permutasi
        jumlah_kombinasi += len(nama_gabung) - panjang_username + 1
    
    return jumlah_kombinasi

# Nama lengkap Naip
nama_lengkap_naip = "Naip Lovyu"

# Hitung jumlah kombinasi untuk username
jumlah_kombinasi_username = hitung_kombinasi_username(nama_lengkap_naip)

# Output hasil
print("Jumlah kombinasi username yang mungkin:", jumlah_kombinasi_username)
