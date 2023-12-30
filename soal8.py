# Data produk
produk = {
    "TV": {"Kategori": "elektronik", "Harga": 1000},
    "headphone": {"Kategori": "elektronik", "Harga": 200},
    "baju": {"Kategori": "fashion", "Harga": 50},
    "gitar": {"Kategori": "musik", "Harga": 300},
    "sepatu": {"Kategori": "olahraga", "Harga": 80},
    "kamera": {"Kategori": "elektronik", "Harga": 600},
}

# Data pelanggan
pelanggan = {
    "Rina": {"Minat": ["elektronik", "musik"], "Beli": ["TV", "headphone"]},
    "Budi": {"Minat": ["fashion", "musik"], "Beli": ["baju", "gitar"]},
    "Hartono": {"Minat": ["olahraga", "elektronik"], "Beli": ["sepatu", "kamera"]},
}

# Fungsi untuk memberikan rekomendasi produk berdasarkan minat pelanggan
def rekomendasi_produk(nama_pelanggan):
    minat_pelanggan = pelanggan.get(nama_pelanggan, {}).get("Minat", [])
    beli_pelanggan = pelanggan.get(nama_pelanggan, {}).get("Beli", [])

    # Mencari semua produk yang sesuai dengan minat pelanggan dan belum dibeli
    rekomendasi = [produk_nama for produk_nama, info_produk in produk.items()
                   if info_produk["Kategori"] in minat_pelanggan and produk_nama not in beli_pelanggan]

    return rekomendasi

# Memperbarui data pelanggan Rina dengan minat yang diinginkan
pelanggan["Rina"]["Minat"] = ["elektronik", "musik"]  # Memperbarui minat pelanggan Rina
pelanggan["Rina"]["Beli"] = []  # Mengosongkan daftar produk yang telah dibeli oleh Rina

# Menampilkan rekomendasi produk untuk pelanggan Rina
nama_pelanggan = "Rina"
hasil_rekomendasi = rekomendasi_produk(nama_pelanggan)

# Menampilkan tabel output
print("\n{:<20} {:<30}".format("Nama Pelanggan", "Rekomendasi Produk"))
print("-" * 60)
print("{:<20} {:<30}".format(nama_pelanggan, ", ".join(hasil_rekomendasi)))
