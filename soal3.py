def detektif_yanfei(foto_xiao):
    # Urutan kedatangan tamu
    urutan_tamu = ["Ningguang", "Hutao", "Xiao", "Childe"]

    # Kebiasaan tamu
    kebiasaan_tamu = {
        "Ningguang": "memeriksa kue",
        "Hutao": "langsung memberikan kado",
        "Xiao": "memotret apa pun yang dia lihat pertama kali",
        "Childe": "membawa air mineral dan meletakkannya di meja"
    }

    # Cek apakah kue masih utuh berdasarkan foto Xiao
    kue_masih_utuh = "kue" in foto_xiao.lower()

    # Memeriksa setiap tamu untuk menentukan siapa yang paling mungkin mengambil kue
    for tamu in urutan_tamu:
        if kue_masih_utuh:
            # Jika kue masih utuh, maka tamu yang memeriksa kue adalah yang paling mungkin mengambil
            if kebiasaan_tamu[tamu] == "memeriksa kue":
                return tamu
        else:
            # Jika kue sudah diambil, maka tamu yang membawa air mineral adalah yang paling mungkin mengambil
            if kebiasaan_tamu[tamu] == "membawa air mineral dan meletakkannya di meja":
                return tamu

# Contoh penggunaan dengan foto Xiao yang menunjukkan kue masih utuh
foto_xiao_masih_utuh = "Foto kue masih utuh di meja."
tamu_yang_mungkin_masih_utuh = detektif_yanfei(foto_xiao_masih_utuh)
print("Tamu yang paling mungkin mengambil kue:", tamu_yang_mungkin_masih_utuh)
