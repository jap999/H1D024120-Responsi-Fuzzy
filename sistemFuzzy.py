import tkinter as tk
from tkinter import messagebox

def hitung_fuzzy():
    # Simulasi Logika Fuzzy Sederhana
    try:
        bat = float(entry_bat.get())
        temp = float(entry_temp.get())
        
        # Logika: Semakin rendah baterai & suhu normal, durasi semakin lama
        durasi = (100 - bat) * (1.2 if temp < 35 else 0.8)
        
        messagebox.showinfo("Hasil Fuzzy", f"Rekomendasi Durasi Cas: {durasi:.1f} Menit")
    except:
        messagebox.showerror("Error", "Masukkan angka yang valid!")

root = tk.Tk()
root.title("Fuzzy-Charge Saver")
root.geometry("300x250")

tk.Label(root, text="Sisa Baterai (%)").pack(pady=5)
entry_bat = tk.Entry(root)
entry_bat.pack()

tk.Label(root, text="Suhu Perangkat (°C)").pack(pady=5)
entry_temp = tk.Entry(root)
entry_temp.pack()

tk.Button(root, text="Hitung Durasi", command=hitung_fuzzy, bg="green", fg="white").pack(pady=20)
root.mainloop()
