import sqlite3

# ==============================
# SISTEM INVENTARIS BARANG
# ==============================
conn = sqlite3.connect("inventaris_barang.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS barang (
    kode_barang TEXT PRIMARY KEY,
    nama_barang TEXT,
    stok INTEGER,
    harga REAL
)
""")
conn.commit()

# ==============================
# Fungsi Menu
# ==============================
def tampil_menu():
    print("=" * 45)
    print(" SISTEM INVENTARIS BARANG  ")
    print("=" * 45)
    print("1. Tambah barang")
    print("2. Tampilkan inventaris")
    print("3. Update stok")
    print("4. Hapus barang")
    print("0. Keluar")
    print("=" * 45)

# ==============================
# Tambah Data
# ==============================
def tambah_data():
    print("\nTAMBAH DATA BARANG")
    kode_barang = input("Kode Barang      : ")
    nama_barang = input("Nama Barang     : ")
    stok = int(input("Stok             : "))
    harga = float(input("Harga            : "))

    try:
        cursor.execute(
            "INSERT INTO barang VALUES (?, ?, ?, ?)",
            (kode_barang, nama_barang, stok, harga)
        )
        conn.commit()
        print("✅ Data berhasil ditambahkan!")
    except sqlite3.IntegrityError:
        print("❌ Barang sudah terdaftar")

# ==============================
# Tampilkan Data
# ==============================
def tampil_data():
    print("\nTAMPILKAN INVENTARIS BARANG")
    print("-" * 60)
    print(f"{'Kode Barang':<15}{'Nama Barang':<20}{'Stok':<10}{'Harga':<15}")
    print("-" * 60)

    cursor.execute("SELECT * FROM barang")
    data = cursor.fetchall()

    if not data:
        print("Data masih kosong.")
    else:
        for barang in data:
            print(f"{barang[0]:<15}{barang[1]:<20}{barang[2]:<10}{barang[3]:<15}")

# ==============================
# Update Stok
# ==============================
def update_stok():
    print("\nUPDATE STOK BARANG")
    kode_barang = input("Masukkan Kode Barang : ")
    stok_baru = int(input("Stok baru            : "))

    cursor.execute(
        "UPDATE barang SET stok = ? WHERE kode_barang = ?",
        (stok_baru, kode_barang)
    )

    if cursor.rowcount == 0:
        print("❌ Kode barang tidak ditemukan!")
    else:
        conn.commit()
        print("✅ Stok berhasil diperbarui!")

# ==============================
# Hapus Data
# ==============================
def hapus_data():
    print("\nHAPUS DATA BARANG")
    kode_barang = input("Masukkan Kode Barang : ")

    cursor.execute("DELETE FROM barang WHERE kode_barang = ?", (kode_barang,))

    if cursor.rowcount == 0:
        print("❌ Kode barang tidak ditemukan!")
    else:
        conn.commit()
        print("✅ Data berhasil dihapus!")

# ==============================
# Program Utama
# ==============================
while True:
    tampil_menu()
    pilihan = input("Pilih menu [0-4]: ")

    if pilihan == "1":
        tambah_data()
    elif pilihan == "2":
        tampil_data()
    elif pilihan == "3":
        update_stok()
    elif pilihan == "4":
        hapus_data()
    elif pilihan == "0":
        print("\nTerima kasih 🙏 Program selesai.")
        break
    else:
        print("❌ Pilihan tidak valid!")

conn.close() 