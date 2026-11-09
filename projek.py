import json
import os
import tkinter as tk
from tkinter import messagebox, ttk
from turtle import setup
import cv2
import qrcode
from PIL import Image, ImageTk

#FILE database lokal
DB_FILE = "data_mbg_kelas.json"

#data awal kelas dan kuota porsi MBG
DATA_AWAL = {
    "X TKJ 1": {"kuota": 36, "status": "Belum Ambil"},
    "X TKJ 2": {"kuota": 36, "status": "Belum Ambil"},
    "XI TKJ 1": {"kuota": 37, "status": "Belum Ambil"},
    "XI TKJ 2": {"kuota": 37, "status": "Belum Ambil"},
    "XII TKJ 1": {"kuota": 34, "status": "Belum Ambil"},
    "XII TKJ 2": {"kuota": 35, "status": "Belum Ambil"},
}

def muat_data():
    if not os.path.exists(DB_FILE):
        simpan_data(DATA_AWAL)
        return DATA_AWAL
    with open(DB_FILE, "r") as f:
        return json.load(f)
    
    
def simpan_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)
        
        
def buat_qr_kelas(data):
    """Membuat file gambar QR code untuk setiap kelas secara otomatis."""
    os.makedirs("qr_kelas", exist_ok=True)
    for nama_kelas in data.keys():
        file_path = f"qr_kelas/{nama_kelas.replace(' ', '_')}.png"
        if not os.path.exists(file_path):
            qr = qrcode.make(nama_kelas)
            qr.save(file_path)
            
            
class AppMBG:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Verifikasi QR Code MBG Per Kelas")
        self.root.geometry("850x500")

        self.data = muat_data()
        buat_qr_kelas(self.data)

        self.detector = cv2.QRCodeDetector()
        self.cap = None
        self.is_scanning = False
        self.last_scanned = ""