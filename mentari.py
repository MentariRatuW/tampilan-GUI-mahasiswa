import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo

def panggil():
    pesan = f"Biodata Mahasiswa:\nNIM: {NIM.get()}\nNama: {Nama_Depan.get()} {Nama_Belakang.get()}\nJenis Kelamin: {Jenis_Kelamin.get()}\nProgram Studi: {Program_Studi.get()}\nAlamat: {Alamat.get()}"
    showinfo(title="Data Tersimpan", message=pesan)

def hitung_total_belanja():
    try:
        jumlah_belanja = int(jumlah_belanja_entry.get())
    except ValueError:
        showinfo(title="Error", message="Masukkan jumlah belanja dalam angka.")
        return
    
    diskon = 0
    persen_diskon = 0
    
    if jumlah_belanja >= 100000 and jumlah_belanja < 200000:
        diskon = 0.05 * jumlah_belanja
        persen_diskon = 5
    elif jumlah_belanja >= 200000 and jumlah_belanja < 500000:
        diskon = 0.1 * jumlah_belanja
        persen_diskon = 10
    elif jumlah_belanja >= 500000:
        diskon = 0.15 * jumlah_belanja
        persen_diskon = 15
    
    total_pembayaran = jumlah_belanja - diskon
    
    pesan = f"Total Belanja: Rp {jumlah_belanja}\nAnda mendapatkan diskon {persen_diskon}%: Rp {diskon}\nTotal Pembayaran: Rp {total_pembayaran}"
    showinfo(title="Pembayaran", message=pesan)

def hitung_nilai_akhir():
    try:
        nilai_absen = float(nilai_absen_entry.get())
        nilai_tugas = float(nilai_tugas_entry.get())
        nilai_quis = float(nilai_quis_entry.get())
        nilai_uts = float(nilai_uts_entry.get())
        nilai_uas = float(nilai_uas_entry.get())
    except ValueError:
        showinfo(title="Error", message="Masukkan nilai dalam bentuk angka.")
        return
    
    nilai_akhir = 0.1 * nilai_absen + 0.2 * nilai_tugas + 0.2 * nilai_quis + 0.2 * nilai_uts + 0.3 * nilai_uas
    
    if nilai_akhir >= 85:
        nilai_huruf = 'A'
    elif nilai_akhir >= 75:
        nilai_huruf = 'B'
    elif nilai_akhir >= 65:
        nilai_huruf = 'C'
    else:
        nilai_huruf = 'D'
    
    pesan = f"Nilai Akhir Mahasiswa:\nNama: {nama_lengkap_entry.get()}\nAbsen: {nilai_absen}\nTugas: {nilai_tugas}\nQuis: {nilai_quis}\nUTS: {nilai_uts}\nUAS: {nilai_uas}\nNilai Akhir: {nilai_akhir}\nNilai Huruf: {nilai_huruf}"
    showinfo(title="Nilai Akhir", message=pesan)

window = tk.Tk()
window.configure(bg="blue")
window.geometry("600x700")
window.resizable(False, False)
window.title("Mentari")

tab_control = ttk.Notebook(window)

tab1 = ttk.Frame(tab_control)
tab_control.add(tab1, text="Biodata Mahasiswa")

tab2 = ttk.Frame(tab_control)
tab_control.add(tab2, text="Total Belanja")

tab3 = ttk.Frame(tab_control)
tab_control.add(tab3, text="Nilai Akhir Mahasiswa")

tab_control.pack(expand=1, fill="both")

input_Frame_tab1 = ttk.Frame(tab1)
input_Frame_tab1.pack(padx=10, pady=10, fill="both", expand=True)

judul_label = ttk.Label(input_Frame_tab1, text="BIODATA MAHASISWA", font=("Arial", 16), anchor='center')
judul_label.pack(padx=10, pady=10, fill="x", expand=True)

nim_label = ttk.Label(input_Frame_tab1, text="Nomor Induk Mahasiswa (NIM)")
nim_label.pack(padx=10, pady=5, fill="x", expand=True)

NIM = tk.StringVar()
nim_entry = ttk.Entry(input_Frame_tab1, textvariable=NIM)
nim_entry.pack(padx=10, pady=5, fill="x", expand=True)

nama_depan = ttk.Label(input_Frame_tab1, text="Nama Depan")
nama_depan.pack(padx=10, pady=5, fill="x", expand=True)

Nama_Depan = tk.StringVar()
nama_depan_entry = ttk.Entry(input_Frame_tab1, textvariable=Nama_Depan)
nama_depan_entry.pack(padx=10, pady=5, fill="x", expand=True)

nama_belakang = ttk.Label(input_Frame_tab1, text="Nama Belakang")
nama_belakang.pack(padx=10, pady=5, fill="x", expand=True)

Nama_Belakang = tk.StringVar()
nama_belakang_entry = ttk.Entry(input_Frame_tab1, textvariable=Nama_Belakang)
nama_belakang_entry.pack(padx=10, pady=5, fill="x", expand=True)

jenis_kelamin_label = ttk.Label(input_Frame_tab1, text="Jenis Kelamin")
jenis_kelamin_label.pack(padx=10, pady=5, fill="x", expand=True)

Jenis_Kelamin = tk.StringVar()
radio_laki = ttk.Radiobutton(input_Frame_tab1, text="Laki-Laki", variable=Jenis_Kelamin, value="Laki-Laki")
radio_laki.pack(padx=10, pady=5, anchor='w')

radio_perempuan = ttk.Radiobutton(input_Frame_tab1, text="Perempuan", variable=Jenis_Kelamin, value="Perempuan")
radio_perempuan.pack(padx=10, pady=5, anchor='w')

program_studi_label = ttk.Label(input_Frame_tab1, text="Program Studi")
program_studi_label.pack(padx=10, pady=5, fill="x", expand=True)

Program_Studi = tk.StringVar()
radio_sipil = ttk.Radiobutton(input_Frame_tab1, text="Teknik Sipil", variable=Program_Studi, value="Teknik Sipil")
radio_sipil.pack(padx=10, pady=5, anchor='w')

radio_informatika = ttk.Radiobutton(input_Frame_tab1, text="Teknik Informatika", variable=Program_Studi, value="Teknik Informatika")
radio_informatika.pack(padx=10, pady=5, anchor='w')

radio_hasil_pertanian = ttk.Radiobutton(input_Frame_tab1, text="Teknik Hasil Pertanian", variable=Program_Studi, value="Teknik Hasil Pertanian")
radio_hasil_pertanian.pack(padx=10, pady=5, anchor='w')

radio_kesejahteraan_sosial = ttk.Radiobutton(input_Frame_tab1, text="Kesejahteraan Sosial", variable=Program_Studi, value="Kesejahteraan Sosial")
radio_kesejahteraan_sosial.pack(padx=10, pady=5, anchor='w')

alamat_label = ttk.Label(input_Frame_tab1, text="Alamat")
alamat_label.pack(padx=10, pady=5, fill="x", expand=True)

Alamat = tk.StringVar()
alamat_entry = ttk.Entry(input_Frame_tab1, textvariable=Alamat)
alamat_entry.pack(padx=10, pady=5, fill="x", expand=True)

tombol_panggil = ttk.Button(input_Frame_tab1, text="Simpan Data", command=panggil)
tombol_panggil.pack(padx=10, pady=10, fill="x", expand=True)


input_Frame_tab2 = ttk.Frame(tab2)
input_Frame_tab2.pack(padx=10, pady=10, fill="both", expand=True)

judul_label_tab2 = ttk.Label(input_Frame_tab2, text="INPUT JUMLAH BELANJA", font=("Arial", 16), anchor='center')
judul_label_tab2.pack(padx=10, pady=10, fill="x", expand=True)

nama_member_label = ttk.Label(input_Frame_tab2, text="Nama Member")
nama_member_label.pack(padx=10, pady=5, fill="x", expand=True)

Nama_Member = tk.StringVar()
nama_member_entry = ttk.Entry(input_Frame_tab2, textvariable=Nama_Member)
nama_member_entry.pack(padx=10, pady=5, fill="x", expand=True)

nomor_member_label = ttk.Label(input_Frame_tab2, text="Nomor Member")
nomor_member_label.pack(padx=10, pady=5, fill="x", expand=True)

Nomor_Member = tk.StringVar()
nomor_member_entry = ttk.Entry(input_Frame_tab2, textvariable=Nomor_Member)
nomor_member_entry.pack(padx=10, pady=5, fill="x", expand=True)

jumlah_belanja_label = ttk.Label(input_Frame_tab2, text="Jumlah Belanja (Rp)")
jumlah_belanja_label.pack(padx=10, pady=5, fill="x", expand=True)

jumlah_belanja_entry = ttk.Entry(input_Frame_tab2)
jumlah_belanja_entry.pack(padx=10, pady=5, fill="x", expand=True)

def panggil_tab2():
    hitung_total_belanja()

tombol_panggil_tab2 = ttk.Button(input_Frame_tab2, text="Total Belanja", command=panggil_tab2)
tombol_panggil_tab2.pack(padx=10, pady=10, fill="x", expand=True)

input_Frame_tab3 = ttk.Frame(tab3)
input_Frame_tab3.pack(padx=10, pady=10, fill="both", expand=True)

judul_label_tab3 = ttk.Label(input_Frame_tab3, text="INPUT NILAI MAHASISWA", font=("Arial", 16), anchor='center')
judul_label_tab3.pack(padx=10, pady=10, fill="x", expand=True)

nama_lengkap_label = ttk.Label(input_Frame_tab3, text="Nama Lengkap")
nama_lengkap_label.pack(padx=10, pady=5, fill="x", expand=True)

nama_lengkap_entry = ttk.Entry(input_Frame_tab3)
nama_lengkap_entry.pack(padx=10, pady=5, fill="x", expand=True)

nilai_absen_label = ttk.Label(input_Frame_tab3, text="Nilai Absen")
nilai_absen_label.pack(padx=10, pady=5, fill="x", expand=True)

nilai_absen_entry = ttk.Entry(input_Frame_tab3)
nilai_absen_entry.pack(padx=10, pady=5, fill="x", expand=True)

nilai_tugas_label = ttk.Label(input_Frame_tab3, text="Nilai Tugas")
nilai_tugas_label.pack(padx=10, pady=5, fill="x", expand=True)

nilai_tugas_entry = ttk.Entry(input_Frame_tab3)
nilai_tugas_entry.pack(padx=10, pady=5, fill="x", expand=True)

nilai_quis_label = ttk.Label(input_Frame_tab3, text="Nilai Quis")
nilai_quis_label.pack(padx=10, pady=5, fill="x", expand=True)

nilai_quis_entry = ttk.Entry(input_Frame_tab3)
nilai_quis_entry.pack(padx=10, pady=5, fill="x", expand=True)

nilai_uts_label = ttk.Label(input_Frame_tab3, text="Nilai UTS")
nilai_uts_label.pack(padx=10, pady=5, fill="x", expand=True)

nilai_uts_entry = ttk.Entry(input_Frame_tab3)
nilai_uts_entry.pack(padx=10, pady=5, fill="x", expand=True)

nilai_uas_label = ttk.Label(input_Frame_tab3, text="Nilai UAS")
nilai_uas_label.pack(padx=10, pady=5, fill="x", expand=True)

nilai_uas_entry = ttk.Entry(input_Frame_tab3)
nilai_uas_entry.pack(padx=10, pady=5, fill="x", expand=True)

def panggil_tab3():
    hitung_nilai_akhir()

tombol_panggil_tab3 = ttk.Button(input_Frame_tab3, text="Lihat Nilai", command=panggil_tab3)
tombol_panggil_tab3.pack(padx=10, pady=10, fill="x", expand=True)

window.mainloop()
