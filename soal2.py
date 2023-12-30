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

# Memeriksa setiap kalimat dan mencetak output yang sesuai
for teks in kalimat:
    if is_palindrome(teks):
        print(teks + " eureeka!")
    else:
        print(teks + " suka blyat")
