# Game Pertualangan: Pertualangan Virtual dengan Nova
# -----------------------------------------------------

print("Selamat datang di Dunia Virtual!")
print("Saya adalah Nova, Asisten AI anda.")
username = input("Masukkan username: ")
print("Misi Anda adalah menemukan 'Kunci Virtual' untuk keluar dari dunia ini.")
print("Mari kita mulai petualangan!\n")

# Jalan Pertama yang harus dipilih
print("Nova: Ada dua jalan di depan.")
print("1. Hutan Kegelapan")
print("2. Kota Tua terbengkalai")
pilihan = input("Ke mana anda ingin pergi? ketik 'hutan' atau 'kota': ")

if pilihan == 'hutan':
    print("\nAnda memilih Hutan Kegelapan.")
    print("Nova: Hati-hati, Disini sangat berbahaya.")
    # Tantangan teka-teki sederhana
    jawaban = input("Nova: Lele-lele apa yang bisa terbang? Hewan apakah itu:  ")
    if jawaban.lower() == "lelelawar":
        print("Nova: Benar! Anda berhasil melanjutkan perjalanan.")
    else:
        print("Nova: Jawaban salah. Anda terjebak di hutan selamanya...")

elif pilihan == "kota":
    print("\nAnda memilih Kota Tua yang Terbengkalai.")
    print("Nova: Tempat ini sepertinya kosong, tapi saya merasakan sesuatu...")
    # Interaksi dengan robot
    tindakan = input("Nova: Ada robot rusak di depan. Ketik 'perbaiki' atau 'lewati': ")
    if tindakan == "perbaiki":
        print("Nova: Robot itu aktif dan membantu Anda! Anda mendapat petunjuk ke Kunci Virtual.")
    else:
        print("Nova: Anda mengabaikan robot itu dan tersesat di kota.")
else:
    print("Nova: Saya tidak mengerti pilihan Anda. Petualangan tidak dapat diselesaikan.")

print("\nTerima kasih telah bermain! Sampai jumpa di petualangan berikutnya.")