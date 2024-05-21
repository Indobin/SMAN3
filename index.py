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
            Menu_utama(cur)
    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)
    finally:
        if conn:
            cur.close()
            conn.close()

def Menu_utama(cur):
    clear()
    tampilan()
    print("[1] Login Admin")
    print("[2] Login Guru")
    print("=" * 31)
    pilih_menu = input("Pilih menu nomor (1/2) : ")
    if pilih_menu == '1':
        Login_admin(cur)
        # break  
    elif pilih_menu == '2':
        Login_guru(cur)
        # break  
    else:
        input("Perintah tidak diketahui!")


def Login_admin(cur):
    clear()
    tampilan_admin()
    username = input(f"Masukkan Username : ")
    password = input(f"Masukkan Password : ")
    select_query = "SELECT * FROM admin WHERE username = %s AND password = %s"
    cur.execute(select_query, (username, password))
    data2 = cur.fetchone()
    if data2:
        Menu_admin(cur)
    else:
        input('Username atau password salah.')
        Login_admin(cur)    

def Menu_admin(cur):
    clear()
    tampilan_admin()
    print("[1] Kelas")
    print("[2] Mata Pelajaran")
    print("[3] Siswa")
    print("[4] Guru")
    print("[6] Jadwal Pelajaran")
    print("[5] Logout")
    print("=" * 31)
    pilih_menu = input("Pilih menu nomor (1/2) : ")
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
            Menu_utama(cur) 
        case _:
            input("Perintah tidak diketahui!")
            Menu_admin(cur) 
def Login_guru(cur):
    clear()
    tampilan_guru()
    nama_guru = input(f"Masukkan Nama : ")
    nip = input(f"Masukkan NIP  : ")
    select_query = "SELECT * FROM guru WHERE nama_guru = %s AND nip = %s"
    cur.execute(select_query, (nama_guru, nip))
    data2 = cur.fetchone()
    if data2:
        Menu_guru(cur)
    else:
        input('Username atau password salah.')
        Login_admin(cur)  
        
def Menu_guru(cur):
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
            Menu_utama(cur) 
        case _:
            input("Perintah tidak diketahui!")
            Menu_guru(cur) 
if __name__ == "__main__":
    Main()
