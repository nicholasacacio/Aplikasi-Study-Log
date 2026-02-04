catatan = []
target_harian = None

def tambah_catatan():
    mapel = input("Mapel: ").strip()
    topik = input("Topik: ").strip()
    while True:
        durasi_input = input("Durasi belajar (menit): ").strip()
        try:
            durasi = int(durasi_input)
            if durasi <= 0:
                print("Durasi harus angka positif. Coba lagi.")
                continue
            break
        except ValueError:
            print("Masukkan angka untuk durasi (contoh: 30). Coba lagi.")

    catatan.append({
        "mapel": mapel,
        "topik": topik,
        "durasi": durasi
    })
    print("Catatan tersimpan.")

def lihat_catatan():
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    print("\n=== Daftar Catatan Belajar ===")
    for i, c in enumerate(catatan, 1):
        print(f"{i}. {c['mapel']} - {c['topik']} ({c['durasi']} menit)")
    print(f"Total catatan: {len(catatan)}")

def total_waktu():
    if not catatan:
        print("Belum ada catatan belajar.")
        return

    total = sum(c["durasi"] for c in catatan)
    print(f"Total waktu belajar: {total} menit")
    if target_harian is not None:
        print(f"Target harian: {target_harian} menit")
        if total >= target_harian:
            lebih = total - target_harian
            print(f"Selamat — target tercapai! Melebihi target {lebih} menit.")
        else:
            sisa = target_harian - total
            print(f"Sisa untuk mencapai target: {sisa} menit")

def menu():
    print("\n=== Study Log App ===")
    print("1. Tambah catatan belajar")
    print("2. Lihat catatan belajar")
    print("3. Total waktu belajar")
    print("4. Set target harian")
    print("5. Keluar")

while True:
    menu()
    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        tambah_catatan()
    elif pilihan == "2":
        lihat_catatan()
    elif pilihan == "3":
        total_waktu()
    elif pilihan == "4":
        # set target harian
        while True:
            nilai = input("Target harian (menit): ").strip()
            try:
                menit = int(nilai)
                if menit <= 0:
                    print("Masukkan angka positif. Coba lagi.")
                    continue
                target_harian = menit
                print(f"Target harian diset: {target_harian} menit")
                break
            except ValueError:
                print("Masukkan angka untuk durasi (contoh: 60). Coba lagi.")
    elif pilihan == "5":
        print("Terima kasih, terus semangat belajar!")
        break
    else:
        print("Pilihan tidak valid")