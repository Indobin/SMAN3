import psycopg2
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for portability

def tampilan():
    print("=" * 31)
    print("|" + " " * 7 + "SMAN 3 LUMAJANG" + " " * 7 + "|")
    print("=" * 31)
def tampilan_admin():
    print("=" * 31)
    print("|" + " " * 12 + "Admin" + " " * 12 + "|")
    print("=" * 31)
def tampilan_guru():
    print("=" * 31)
    print("|" + " " * 12 + "Guru" + " " * 11 + "|")
    print("=" * 31)
    
def Main():
    try:
        conn = psycopg2.connect(database='SMAN3',
                                user='postgres',
                                password='321',
                                host='localhost',
                                port=5432)
        cur = conn.cursor()
        while True:
            Mata_pelajaran(cur,conn)
            break
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if conn:
            cur.close()
            conn.close()

def Menu_utama(cur,conn):
    clear()
    tampilan()
    print("[1] Login Admin")
    print("[2] Login Guru")
    print("=" * 31)
    pilih_menu = input("Pilih menu nomor (1/2) : ")
    if pilih_menu == '1':
        Login_admin(cur,conn)
        # break  
    elif pilih_menu == '2':
        Login_guru(cur,conn)
        # break  
    else:
        input("Perintah tidak diketahui!")


def Login_admin(cur,conn):
    clear()
    tampilan_admin()
    admin = '''SELECT username, password from admin'''
    cur.execute(admin)
    data = cur.fetchall()
    for i in data:
        print(i)
    username = input(f"Masukkan Username : ")
    password = input(f"Masukkan Password : ")
    select_query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    cur.execute(select_query, (username, password))
    data2 = cur.fetchone()
    if data2:
        Menu_admin(cur,conn)
    else:
        input('Username atau password salah.')
        Login_admin(cur,conn)    

def Menu_admin(cur,conn):
    clear()
    tampilan_admin()
    print("[1] Kelas")
    print("[2] Mata Pelajaran")
    print("[3] Siswa")
    print("[4] Guru")
    print("[6] Jadwal Pelajaran")
    print("[5] Logout")
    print("=" * 31)
    pilih_menu = input("Pilih menu nomor (1/2/3/4/5) : ")
    match pilih_menu:
        case '1':
            Kelas()
        case '2':
            Mata_pelajaran()
        case '3':
            Siswa()
        case '4':
            Guru()
        case '5':
            Jadwal_pelajaran()
        case '6':
            Menu_utama(cur,conn) 
        case _:
            input("Perintah tidak diketahui!")
            Menu_admin(cur,conn) 
            
def Mata_pelajaran(cur,conn):
    # tampilan_admin()
    print("=" * 50)
    print("|" + " " * 17 + "Mata Pelajaran" + " " * 17 + "|")
    print("=" * 50)
    print("No\t Kode\t Nama Mata Pelajaran\t Semester")
    print("-"*50)
    query_mapel = '''SELECT * FROM mata_pelajaran'''
    cur.execute(query_mapel)
    data = cur.fetchall()
    No = 0;
    for i in data:
        No += 1;
        if len(i[2]) <= 5:
            print(f"{No}\t {i[1]}\t {i[2]} \t\t\t {i[3]}") 
        elif len(i[2]) > 5:
            print(f"{No}\t {i[1]}\t {i[2]} \t\t {i[3]}")
    print("="*50)
    print("[1] Tambah")
    print("[2] Edit")
    print("[3] Hapus")
    print("[4] Kembali")
    print("="*50)
    pilih_menu = input(f"Pilih menu nomor (1/2/3/4) : ")
    match pilih_menu:
        case '1':
            Tbh_mata_pelajaran(cur,conn)
        case _:
            input("Perintah tidak diketahui!")
            Mata_pelajaran(cur,conn) 
            
def Tbh_mata_pelajaran(cur,conn):
    print(f"Tambah Data")
    total_input = int(input(f"Ingin Menambahkan Berapa Data"))
    for i in range(total_input):
        Kode_awal = "KD"
        Kode =           input(f"Masukkan Kode Pelajaran (angka) : ")
        Kode_lengkap = Kode_awal+Kode
        cek_query = '''SELECT * FROM mata_pelajaran'''
        cur.execute(cek_query)
        cek = cur.fetchall()
        for data in cek:
            if data[1] == Kode_lengkap:
                print("Kode Pelajaran sudah ada")
                Tbh_mata_pelajaran(cur,conn)
        else:
                Nama_pelajaran = input(f"Masukkan Nama Mata Pelaja1ran    : ")
                semester =   int(input(f"Masukkan Semester (angka)       : "))
                query_tambah = '''INSERT INTO mata_pelajaran (kode_pelajaran, nama_pelajaran, semester) 
                                VALUES(%s, %s, %s)'''
                cur.execute(query_tambah,(Kode_lengkap, Nama_pelajaran, semester))
                conn.commit()
def Login_guru(cur,conn):
    clear()
    tampilan_guru()
    nama_guru = input(f"Masukkan Nama : ")
    nip = input(f"Masukkan NIP  : ")
    select_query = "SELECT * FROM guru WHERE nama_guru = %s AND nip = %s"
    cur.execute(select_query, (nama_guru, nip))
    data2 = cur.fetchone()
    if data2:
        Menu_guru(cur,conn)
    else:
        input('Username atau password salah.')
        Login_admin(cur,conn)  
        
def Menu_guru(cur,conn):
    clear()
    tampilan_guru()
    print("[1] Jadwal Pelajaran")
    print("[2] Jenis Tugas")
    print("[3] Nilai Siswa")
    print("[4] Logout")
    print("=" * 31)
    pilih_menu = input("Pilih menu nomor (1/2) : ")
    match pilih_menu:
        case '1':
            Jadwal_pelajaran()
        case '2':
            Jenis_tugas()
        case '3':
            Nilai_siswa()
        case '4':
            Menu_utama(cur,conn) 
        case _:
            input("Perintah tidak diketahui!")
            Menu_guru(cur,conn) 
if __name__ == "__main__":
    Main()
