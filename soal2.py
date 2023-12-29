def cek_palindrom(teks):
    # Mengubah teks menjadi lowercase dan mengabaikan karakter selain huruf
    teks = ''.join(c.lower() for c in teks if c.isalpha())
    
    # Mengecek apakah teks palindrom atau tidak
    if teks == teks[::-1]:
        return "eureeka!"
    else:
        return "suka blyat"

# Contoh penggunaan dengan beberapa kalimat
kalimat_1 = "Angsa suka blyat"
kalimat_2 = "KataK eureeka!"
kalimat_3 = "kasur empuk suka blyat"
kalimat_4 = "Aku Suka Kamu ?"
kalimat_5 = "Ibu Ratna antar ubi. ?"

output_1 = cek_palindrom(kalimat_1)
output_2 = cek_palindrom(kalimat_2)
output_3 = cek_palindrom(kalimat_3)
output_4 = cek_palindrom(kalimat_4)
output_5 = cek_palindrom(kalimat_5)

print(kalimat_1, "-", output_1)
print(kalimat_2, "-", output_2)
print(kalimat_3, "-", output_3)
print(kalimat_4, "-", output_4)
print(kalimat_5, "-", output_5)
