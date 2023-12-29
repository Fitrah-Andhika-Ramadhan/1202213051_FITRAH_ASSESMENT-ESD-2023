# Mendefinisikan harga menu
harga_menu = {
    "Ayam Goreng Krispi": 15000,
    "Ayam Puk Puk": 13000,
    "Ayam Bakar": 20000,
    "Es Teh": 5000,
    "Es Jeruk": 7000
}

# Mendefinisikan pajak
pajak_makanan = 0.05  # 5% untuk makanan
pajak_minuman = 0.03  # 3% untuk minuman
pajak_transaksi = 0.15  # 15% untuk setiap transaksi

# Fungsi untuk menghitung total biaya termasuk pajak
def hitung_biaya(pesanan):
    total_sebelum_pajak = sum(harga_menu[item] * pesanan[item] for item in pesanan)

    total_pajak = sum(harga_menu[item] * pesanan[item] * pajak_makanan 
    if item in ["Ayam Goreng Krispi", "Ayam Puk Puk", "Ayam Bakar"] 
    else harga_menu[item] * pesanan[item] * pajak_minuman for item in pesanan)

    total_setelah_pajak = total_sebelum_pajak + total_pajak
    total_akhir = total_setelah_pajak + (total_setelah_pajak * pajak_transaksi)
    
    return total_akhir

# Pesanan untuk masing-masing sahabat
pesanan_rehan = {"Ayam Bakar": 2, "Es Teh": 1}
pesanan_amba = {"Ayam Puk Puk": 1, "Es Teh": 3}
pesanan_faiz = {"Ayam Goreng Krispi": 1, "Ayam Puk Puk": 1, "Ayam Bakar": 1, "Es Teh": 1, "Es Jeruk": 1}

# Menghitung biaya untuk masing-masing sahabat
biaya_rehan = hitung_biaya(pesanan_rehan)
biaya_amba = hitung_biaya(pesanan_amba)
biaya_faiz = hitung_biaya(pesanan_faiz)

# Menampilkan hasil
print(f"Biaya Rehan: Rp{biaya_rehan}")
print(f"Biaya Amba: Rp{biaya_amba}")
print(f"Biaya Faiz: Rp{biaya_faiz}")
