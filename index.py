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
            Menu_utama(cur,conn)
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
        id_admin = data2[0]
        Menu_admin(cur,conn,id_admin)
    else:
        input('Username atau password salah.')
        Login_admin(cur,conn)    

def Menu_admin(cur,conn,id_admin):
    clear()
    tampilan_admin()
    # print(id_admin)
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
            Mata_pelajaran(cur,conn,id_admin)
        case '3':
            Siswa(cur,conn,id_admin)
        case '4':
            Guru()
        case '5':
            Jadwal_pelajaran()
        case '6':
            Menu_utama(cur,conn) 
        case _:
            input("Perintah tidak diketahui!")
            Menu_admin(cur,conn) 
            
def Mata_pelajaran(cur,conn,id_admin):
    # tampilan_admin()
    clear()
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
        print(f"{No:<8} {i[1]:<7} {i[2]:<23} {i[3]}")
    print("="*50)
    print("[1] Tambah")
    print("[2] Edit")
    print("[3] Hapus")
    print("[4] Kembali")
    print("="*50)
    pilih_menu = input(f"Pilih menu nomor (1/2/3/4) : ")
    match pilih_menu:
        case '1':
            Tbh_mata_pelajaran(cur,conn,id_admin)
        case '2':
            Edit_mata_pelajaran(cur,conn,id_admin)
        case '3':
            Hapus_mata_pelajaran(cur,conn,id_admin)
        case '4':
            Menu_admin(cur,conn,id_admin)
        case _:
            input("Perintah tidak diketahui!")
            Mata_pelajaran(cur,conn,id_admin)          
def Tbh_mata_pelajaran(cur,conn,id_admin):
    print(f"--Tambah Data--")
    total_input = int(input(f"Ingin Menambahkan Berapa Data : "))
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
                Tbh_mata_pelajaran(cur,conn,id_admin)
        else:
                Nama_pelajaran = input(f"Masukkan Nama Mata Pelaja1ran    : ")
                semester =   int(input(f"Masukkan Semester (angka)       : "))
                query_tambah = '''INSERT INTO mata_pelajaran (kode_pelajaran, nama_pelajaran, semester) 
                                VALUES(%s, %s, %s)'''
                cur.execute(query_tambah,(Kode_lengkap, Nama_pelajaran, semester))
                conn.commit()
                Mata_pelajaran(cur,conn,id_admin)

def Edit_mata_pelajaran(cur,conn,id_admin):
    print(f"--Edit Data--")
    Kode = input(f"Masukan kode mata pelajaran yang di update : ")
    select_query = '''SELECT * FROM mata_pelajaran WHERE kode_pelajaran = %s'''
    cur.execute(select_query,(Kode,))
    cek = cur.fetchone()
    if cek:
        print("Data Saat Ini")
        print(f"Kode mata pelejaran : {cek[1]}")
        print(f"Nama mata pelajaran : {cek[2]}")
        print(f"Semester            : {cek[3]}")
        Nama_pelajaran = input(f"Masukkan Nama Mata Pelajaran   : ") or cek[2]
        semester =   input(f"Masukkan Semester (angka)       : ") or cek[3]
        semester = int(semester)
        update_query = '''
            UPDATE mata_pelajaran
            SET nama_pelajaran = %s, semester = %s
            WHERE kode_pelajaran = %s
        '''
        cur.execute(update_query, (Nama_pelajaran, semester, Kode))
        conn.commit()
        input("Data mata pelajaran telah diperbarui.")
        Mata_pelajaran(cur,conn,id_admin)
    else:
        print("Kode mata pelajaran tidak ditemukan.")
        Edit_mata_pelajaran(cur,conn,id_admin)

def Hapus_mata_pelajaran(cur,conn,id_admin):
    print(f"--Hapus Data--")
    Kode = input(f"Masukan kode mata pelajaran yang ingin di hapus : ")
    select_query = '''SELECT * FROM mata_pelajaran WHERE kode_pelajaran = %s'''
    cur.execute(select_query,(Kode,))
    cek = cur.fetchone()
    if cek:
        print("Data Saat Ini")
        print(f"Kode mata pelejaran : {cek[1]}")
        print(f"Nama mata pelajaran : {cek[2]}")
        print(f"Semester            : {cek[3]}")
        konfirmasi = input(f"Apakah anda yakin ingin mengghapus data ini? (y/n): ")
        if konfirmasi == "y":
            query_delete = '''DELETE FROM mata_pelajaran WHERE kode_pelajaran = %s'''
            cur.execute(query_delete,(Kode,))
            conn.commit()
            input("Hapus data mata pelajaran berhasil.")
            Mata_pelajaran(cur,conn,id_admin)
        else :
            Mata_pelajaran(cur,conn,id_admin)
    else:
        print("Kode mata pelajaran tidak ditemukan.")
        Hapus_mata_pelajaran(cur,conn,id_admin)
# def Hapus_mata_pelajaran(cur, conn, id_admin):
#     print("--Hapus Data--")

#     try:
#         kode_pelajaran = input("Masukan kode mata pelajaran yang ingin dihapus: ")
#         query_select = f"SELECT * FROM mata_pelajaran WHERE kode_pelajaran = {kode_pelajaran}"
#         cur.execute(query_select)
#         data_mata_pelajaran = cur.fetchone()
#     except Exception as e:
#         print(f"Error: {e}")
#         return
#     if data_mata_pelajaran:
#         print("Data Saat Ini:")
#         print(f"Kode mata pelajaran: {data_mata_pelajaran[1]}")
#         print(f"Nama mata pelajaran: {data_mata_pelajaran[2]}")
#         print(f"Semester: {data_mata_pelajaran[3]}")

#         konfirmasi = input("Apakah Anda yakin ingin menghapus data ini? (y/n): ")
#         if konfirmasi.lower() == "y":
#             query_delete = f"DELETE FROM mata_pelajaran WHERE kode_pelajaran = {kode_pelajaran}"
#             cur.execute(query_delete)
#             conn.commit()
#             print("Hapus data mata pelajaran berhasil.")
#             Mata_pelajaran(cur, conn, id_admin)
#         else:
#             print("Penghapusan data dibatalkan.")
#             Mata_pelajaran(cur, conn, id_admin)
#     else:
#         print(f"Kode mata pelajaran '{kode_pelajaran}' tidak ditemukan.")
#         Hapus_mata_pelajaran(cur, conn, id_admin)
def Siswa(cur,conn,id_admin):
    clear()
    print("=" * 93)
    print("|" + " " * 40 + "Data Siswa" + " " * 41 + "|")
    print("=" * 93)
    # print(f"{'No':<8} {'Nisn':<8}{'Nama Siswa':<8}{'Angkatan':<8}{'Kelas':<8}{'Status':<8}")
    print("No\t Nisn\t\t Nama Siswa\t\t Angkatan\t Kelas\t\t Status")
    print("-"*93)
    query_siswa = '''select s.nisn, s.nama_siswa, s.tahun_angkatan, k.kelas, s.status
        from siswa s 
        join kelas k on s.id_kelas=k.id_kelas
        order by nisn asc'''
    cur.execute(query_siswa)
    data = cur.fetchall()
    No = 0;
    for i in data:
        No += 1;
        if i[4] == 1:
            print(f"{No:<8} {i[0]:<15} {i[1]:<23} {i[2]:<15} {i[3]:<15} {'Aktif'}")
        else:
            print(f"{No:<8} {i[0]:<15} {i[1]:<23} {i[2]:<15} {i[3]:<15} {'Tidak Aktif'}")
    print("="*93)
    print("[1] Tambah")
    print("[2] Edit")
    print("[3] Detail")
    print("[4] Kembali")
    print("="*93)
    pilih_menu = input(f"Pilih menu nomor (1/2/3/4) : ")
    match pilih_menu:
        case '1':
            Tbh_siswa(cur,conn,id_admin)
        case '2':
            Edit_siswa(cur,conn,id_admin)
        case '3':
            Detail_siswa(cur,conn,id_admin)
        case '4':
            Menu_admin(cur,conn,id_admin)
        case _:
            input("Perintah tidak diketahui!")
            Siswa(cur,conn,id_admin)  

def Tbh_siswa(cur,conn,id_admin):
    print(f"--Tambah Data--")
    total_input = int(input(f"Ingin Menambahkan Berapa Data : "))
    for i in range(total_input):
        Nisn =           input(f"Masukkan NISN siswa (angka) : ")
        cek_query = '''SELECT * FROM siswa'''
        cur.execute(cek_query)
        cek = cur.fetchall()
        for data in cek:
            if data[1] == Nisn:
                print("NISN siswa sudah ada")
                Tbh_siswa(cur,conn,id_admin)
        else:
                Nama_siswa = input(f"Masukkan nama siswa    : ")
                No_telepon =   input(f"Masukkan no telepon siswa (angka) : ")
                Tahun_angkatan =   input(f"Masukkan tahun angkatan siswa (angka) : ")
                Tgl_lahir =   input(f"Masukkan tangal lahir siswa (yyyy-mm-dd) : ")
                Tempat_lahir =   input(f"Masukkan tempat lahir siswa : ")
                Jenis_kelamin =   input(f"Pilih jenis kelamin siswa (L/P) : ")
                Provinsi =   input(f"Masukkan provinsi siswa : ")
                Kabupatenkota =   input(f"Masukkan kabupaten/kota siswa : ")
                Kecamatan =   input(f"Masukkan kecamatan siswa : ")
                Jalan =   input(f"Masukkan alamat jalan siswa : ")
                query_kelas = '''SELECT * FROM kelas'''
                cur.execute(query_kelas)
                cek = cur.fetchall()
                for i in cek:
                    print(f"id : {i[0]} kelas : {i[1]}")
                Pilih_kelas = input(f"Masukkan id kelas yang dipilih : ")
                Id_admin = id_admin
                Status = True
                query_tambah = '''INSERT INTO alamat (provinsi, kabupatenkota, kecamatan, jalan) 
                                VALUES(%s, %s, %s, %s)
                                RETURNING id_alamat'''
                cur.execute(query_tambah,(Provinsi, Kabupatenkota, Kecamatan, Jalan))
                id_alamat_baru = cur.fetchone()[0]
                conn.commit()
                query_tambah_siswa = '''INSERT INTO siswa (nisn, nama_siswa, no_telp, tahun_angkatan, tgl_lahir,
                tempat_lahir, jenis_kelamin, id_alamat, id_kelas, id_admin, status)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
                cur.execute(query_tambah_siswa, (Nisn, Nama_siswa, No_telepon, Tahun_angkatan, Tgl_lahir, 
                            Tempat_lahir, Jenis_kelamin, id_alamat_baru, Pilih_kelas, Id_admin, Status))
                conn.commit()
                input(f"Menambah data siswa berhasil")
                Siswa(cur,conn,id_admin)

def Edit_siswa(cur,conn,id_admin):
    print(f"--Edit Data--")
    Nisn = input(f"Masukan Nisn siswa yang di update : ")
    select_query = '''select s.nisn, s.nama_siswa, s.no_telp, a.provinsi, a.kabupatenkota || ', ' || a.kecamatan 
|| ', ' || a.jalan as alamat, k.kelas, s.status, s.deskripsi, s.id_kelas
from siswa s
join alamat a on s.id_alamat=a.id_alamat
join kelas k on s.id_kelas=k.id_kelas
where nisn = %s '''
    cur.execute(select_query,(Nisn,))
    cek = cur.fetchone()
    if cek:
        print("Data Saat Ini")
        print(f"Nisn                    : {cek[0]}")
        print(f"Nama siswa              : {cek[1]}")
        print(f"No Telepon              : {cek[2]}")
        print(f"Provinsi tempat tinggal : {cek[3]}")
        print(f"Alamat tempat tinggal   : {cek[4]}")
        print(f"Kelas                   : {cek[5]}")
        if cek[6] == 1:
            print(f"Status                  : {'Aktif'}")
        else:
            print(f"Status                  : {'Tidak Aktif'}")
        if cek[7] == '':
            print(f"Keterangan              : ")
        else :
            print(f"Keterangan              : ")
        print(f"--Edit beberapa data--")
        Nisn_baru = input(f"Nisn                    : ") or cek[0]
        Nama_siswa = input(f"Nama siswa              : ")or cek[1]
        No_telp = input(f"No Telepon              : ")or cek[2]
        Kelas = input(f"Kelas                   : ")or cek[8]
        Status = input(f"Status                  : ")or cek[6]
        Keterangan = input(f"Keterangan              : ") or cek[7]
        update_query = '''
            UPDATE siswa
            SET nisn = %s, nama_siswa = %s, no_telp = %s, id_kelas = %s, status = %s, 
            deskripsi = %s
            WHERE nisn = %s
        '''
        cur.execute(update_query, (Nisn_baru, Nama_siswa, No_telp, Kelas, Status, Keterangan, Nisn))
        conn.commit()
        input("Data mata siswa telah diperbarui.")
        edit_alamat = input("Apakah Anda ingin mengedit alamat siswa? (y/n): ").lower()
        if edit_alamat == 'y':
            provinsi_baru = input("Masukkan provinsi baru: ") or cek[3]
            kabupatenkota_baru = input("Masukkan kabupaten/kota baru: ") or cek[4].split(', ')[0]
            kecamatan_baru = input("Masukkan kecamatan baru: ") or cek[4].split(', ')[1]
            jalan_baru = input("Masukkan jalan baru: ") or cek[4].split(', ')[2]
            update_alamat_query = '''
                UPDATE alamat
                SET provinsi = %s, kabupatenkota = %s, kecamatan = %s, jalan = %s
                WHERE id_alamat = (SELECT id_alamat FROM siswa WHERE nisn = %s)
            '''
            cur.execute(update_alamat_query, (provinsi_baru, kabupatenkota_baru, kecamatan_baru, jalan_baru, Nisn))
            conn.commit()
            input("Alamat siswa telah diperbarui.")
        Siswa(cur,conn,id_admin)
    else:
        print(f"Nisn {Nisn} tidak ditemukan.")
        Siswa(cur,conn,id_admin)

def Detail_siswa(cur,conn,id_admin):
    print(f"--Detail Siswa--")
    Nisn = input(f"Masukan nisn untuk melihat detail : ")
    select_query = '''select siswa.*, alamat.*, kelas.*
from siswa 
inner join alamat on siswa.id_alamat=alamat.id_alamat
inner join kelas on siswa.id_kelas=kelas.id_kelas
where nisn = %s '''
    cur.execute(select_query,(Nisn,))
    cek = cur.fetchone()
    if cek:
        print("Data Saat Ini")
        print(f"Nisn                    : {cek[1]}")
        print(f"Nama siswa              : {cek[2]}")
        print(f"No telepon              : {cek[3]}")
        print(f"Tahun angkatan          : {cek[4]}")
        print(f"Tempat,Tanggal lahir    : {cek[6]}, {cek[5]}")
        if cek[7] == "L":
            print(f"Jenis kelamin           : {'Laki-Laki'}")
        else:
            print(f"Jenis kelamin           : {'Perempuan'}")
        print(f"Provinsi                : {cek[14]}")
        print(f"Alamat Lengkap          : {cek[15]}, {cek[16]}, {cek[17]}")
        print(f"Kelas                   : {cek[20]}")
        if cek[11] == 1:
            print(f"Status                  : {'Aktif'}")
        else:
            print(f"Status                  : {'Tidak Aktif'}")
        if cek[12] == '':
            print(f"Keterangan              : {'Kosong'}")
        else :
            print(f"Keterangan              : {cek[12]}")
        input(f"Tekan enter untuk kembali...")
        Siswa(cur,conn,id_admin)
    else:
        input(f"Nisn siswa {Nisn} tidak ditemukan.")
        Siswa(cur,conn,id_admin)
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
