import sqlite3
from datetime import datetime

NAMA_DB = "riwayat_ganjil_genap.db"


def buat_koneksi():
    """Membuat koneksi ke database SQLite."""
    return sqlite3.connect(NAMA_DB)


def buat_tabel():
    """Membuat semua tabel (riwayat & users) jika belum ada. Panggil sekali di awal program."""
    conn = buat_koneksi()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS riwayat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            angka INTEGER NOT NULL,
            hasil TEXT NOT NULL,
            waktu TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


def simpan_riwayat(angka, hasil):
    """Menyimpan satu hasil pengecekan ke database."""
    conn = buat_koneksi()
    cursor = conn.cursor()
    waktu = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute(
        "INSERT INTO riwayat (angka, hasil, waktu) VALUES (?, ?, ?)",
        (angka, hasil, waktu)
    )
    conn.commit()
    conn.close()


def tampilkan_riwayat():
    """Menampilkan semua riwayat pengecekan yang tersimpan."""
    conn = buat_koneksi()
    cursor = conn.cursor()
    cursor.execute("SELECT id, angka, hasil, waktu FROM riwayat ORDER BY id DESC")
    data = cursor.fetchall()
    conn.close()

    if not data:
        print("\nBelum ada riwayat tersimpan.\n")
        return

    print("\n=== RIWAYAT PENGECEKAN ===")
    print(f"{'No':<4}{'Angka':<10}{'Hasil':<10}{'Waktu':<20}")
    print("-" * 44)
    for row in data:
        id_, angka, hasil, waktu = row
        print(f"{id_:<4}{angka:<10}{hasil:<10}{waktu:<20}")
    print()


def hapus_riwayat():
    """Menghapus semua riwayat yang tersimpan."""
    konfirmasi = input("Yakin mau hapus semua riwayat? (y/n): ")
    if konfirmasi.lower() == "y":
        conn = buat_koneksi()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM riwayat")
        conn.commit()
        conn.close()
        print("Riwayat berhasil dihapus.\n")
    else:
        print("Dibatalkan.\n")


# =========================
# BAGIAN LOGIN & USER
# =========================

def daftar_user(username, password):
    """Mendaftarkan user baru. Return True kalau berhasil, False kalau username sudah dipakai."""
    conn = buat_koneksi()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "INSERT INTO users (username, password) VALUES (?, ?)",
            (username, password)
        )
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def cek_login(username, password):
    """Mengecek apakah kombinasi username & password cocok. Return True/False."""
    conn = buat_koneksi()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM users WHERE username = ? AND password = ?",
        (username, password)
    )
    hasil = cursor.fetchone()
    conn.close()
    return hasil is not None