def is_palindrome(text):
    # Mengubah teks menjadi huruf kecil dan menghapus karakter non-alfabet
    cleaned_text = ''.join(filter(str.isalpha, text)).lower()
    
    # Mengecek apakah teks adalah palindrom
    return cleaned_text == cleaned_text[::-1]

# Daftar kalimat untuk diperiksa
kalimat = [
    "Angsa",
    "KataK",
    "kasur empuk",
    "Aku Suka Kamu",
    "Ibu Ratna antar ubi."
]

# Mencetak tabel secara manual
print("Kalimat                 Output")
print("--------------------------------")
# Mengecek setiap kalimat menggunakan fungsi is_palindrome
for teks in kalimat:
    if is_palindrome(teks):
        print(f"{teks:20s} eureeka!")
    else:
        print(f"{teks:20s} suka blyat")
