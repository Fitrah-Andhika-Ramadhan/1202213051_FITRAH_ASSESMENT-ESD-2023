from collections import Counter

def analisis_anak(anak_nakal):
    # Menghitung frekuensi masing-masing nama anak
    frekuensi_anak = Counter(anak_nakal)

    # Mencari nama anak yang paling banyak disebut
    maksimal_frekuensi = max(frekuensi_anak.values())
    anak_terbanyak = [nama for nama, frekuensi in frekuensi_anak.items() if frekuensi == maksimal_frekuensi]

    return anak_terbanyak

# Contoh input
anak_nakal_1 = ["Bagas", "Dimas", "Bagas", "Bagas", "Indra", "Gilang", "Gilang", "Hana", "Fajar", "Fajar"]
anak_nakal_2 = ["Bagas", "Dimas", "Fajar", "Bagas", "Indra", "Gilang", "Gilang", "Bagas", "Fajar", "Fajar"]
anak_nakal_3 = ["Aisyah", "Bagas", "Dewi", "Dimas", "Eka", "Fajar", "Gilang", "Hana", "Indra", "Jihan"]

# Analisis dan menampilkan hasil
hasil_analisis_1 = analisis_anak(anak_nakal_1)
hasil_analisis_2 = analisis_anak(anak_nakal_2)
hasil_analisis_3 = analisis_anak(anak_nakal_3)

print(f"{anak_nakal_1}\n{', '.join(hasil_analisis_1)} Nakal")
print(f"{anak_nakal_2}\n{', '.join(hasil_analisis_2)} Nakal")
print(f"{anak_nakal_3}\nSemuanya anak baik")
