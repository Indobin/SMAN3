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
    elif pilih_menu == '2':
        Login_guru(cur,conn)
    else:
        input("Perintah tidak diketahui!")
        Menu_utama(cur,conn)

def Login_admin(cur,conn):
    clear()
    tampilan_admin()
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
    print("[1] Kelas")
    print("[2] Mata Pelajaran")
    print("[3] Siswa")
    print("[4] Guru")
    print("[5] Jadwal Pelajaran")
    print("[6] Logout")
    print("=" * 31)
    pilih_menu = input("Pilih menu nomor (1/2/3/4/5) : ")
    match pilih_menu:
        case '1':
            Kelas(cur,conn,id_admin)
        case '2':
            Mata_pelajaran(cur,conn,id_admin)
        case '3':
            Siswa(cur,conn,id_admin)
        case '4':
            Admin_Guru(cur,conn,id_admin)
        case '5':
            Jadwal_pelajaran_a(cur,conn,id_admin)
        case '6':
            Menu_utama(cur,conn) 
        case _:
            input("Perintah tidak diketahui!")
            Menu_admin(cur,conn) 

def Kelas(cur,conn,id_admin):
    clear()
    print("=" * 41)
    print("|" + " " * 17 + "Kelas" + " " * 17 + "|")
    print("=" * 41)
    print(f"{'No':<15} {'ID':<15} {'Kelas'}")
    print("-"*41)
    query_kelas = '''SELECT * FROM kelas'''
    cur.execute(query_kelas)
    data = cur.fetchall()
    No = 0;
    for i in data:
        No += 1;
        print(f"{No:<15} {i[0]:<15} {i[1]}")
    print("="*41)
    print("[1] Tambah")
    print("[2] Edit")
    print("[3] Hapus")
    print("[4] Kembali")
    print("="*41)
    pilih_menu = input(f"Pilih menu nomor (1/2/3/4) : ")
    match pilih_menu:
        case '1':
            Tambah_kelas(cur,conn,id_admin)
        case '2':
            Edit_kelas(cur,conn,id_admin)
        case '3':
            Hapus_kelas(cur,conn,id_admin)
        case '4':
            Menu_admin(cur,conn,id_admin)
        case _:
            input("Perintah tidak diketahui!")
            Kelas(cur,conn,id_admin)  

def Tambah_kelas(cur,conn,id_admin):
    print(f"-- Tambah Kelas --")
    total_input = int(input(f"Ingin Menambahkan Berapa Data : "))
    for i in range(total_input):
        id = input(f"Masukkan ID Kelas (Angka) : ")
        cek_query = '''SELECT * FROM kelas'''
        cur.execute(cek_query)
        cek = cur.fetchall()
        for data in cek:
            if data[0] == id:
                print("ID Kelas Sudah Ada")
                Tambah_kelas(cur,conn,id_admin)

            else:
                Nama_Kelas = input(f"Masukkan Kelas    : ")
                query_tambah_kelas = '''INSERT INTO kelas (id_kelas, kelas) 
                                VALUES(%s, %s)'''
                cur.execute(query_tambah_kelas,(id, Nama_Kelas))
                conn.commit()
                Kelas(cur,conn,id_admin)
                
def Edit_kelas(cur,conn,id_admin):
    print(f"-- Edit Kelas --")
    id = input(f"Masukkan ID Kelas Yang Ingin Diupdate: ")
    select_query_kelas = '''SELECT * FROM kelas WHERE id_kelas = %s'''
    cur.execute(select_query_kelas, (id,))
    cek = cur.fetchone()
    if cek:
        print("Data Saat Ini")
        print(f"ID Kelas :  {cek[0]}")
        print(f"Kelas    :  {cek[1]}")
        Nama_Kelas = input(f"Masukkan Nama Kelas : ") or cek[1]
        update_query_kelas = '''
            UPDATE kelas
            SET kelas = %s
            WHERE id_kelas = %s
        '''
        cur.execute(update_query_kelas, (Nama_Kelas, id))
        conn.commit()
        input("Data Kelas Telah Diperbarui.")
        Kelas(cur,conn,id_admin)

    else:
        print("ID Kelas Tidak Ditemukan.")
        Edit_kelas(cur,conn,id_admin)

def Hapus_kelas(cur,conn,id_admin):
    print(f"-- Hapus Kelas --")
    id = input(f"Masukkan ID Kelas Yang Ingin Dihapus : ")
    select_query_kelas = '''SELECT * FROM kelas WHERE id_kelas = %s'''
    cur.execute(select_query_kelas,(id,))
    cek = cur.fetchone()
    if cek:
        print("Data Saat Ini")
        print(f"ID Kelas :  {cek[0]}")
        print(f"Kelas    :  {cek[1]}")
        konfir = input(f"Apakah Anda Yakin Untuk Menghapus? (y/n) : ")
        if konfir == "y":
            query_delete_kelas = '''DELETE FROM kelas WHERE id_kelas = %s'''
            cur.execute(query_delete_kelas,(id,))
            conn.commit()
            input("Hapus Data Kelas Berhasil.")
            Kelas(cur,conn,id_admin)

        else:
            Kelas(cur,conn,id_admin)
    
    else:
        print("ID Kelas Tidak Ditemukan.")
        Hapus_kelas(cur,conn,id_admin)
        
def Mata_pelajaran(cur,conn,id_admin):
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
    try:
        total_input = int(input("Ingin Menambahkan Berapa Data: "))
        if total_input <= 0:
            raise ValueError("Jumlah data harus lebih dari 0")
    except ValueError:
        print("Mohon masukkan jumlah tambah data yang valid (angka positif)")
        Tbh_mata_pelajaran(cur, conn, id_admin)
        return
    for i in range(total_input):
        Kode_awal = "KD"
        Kode = input("Masukkan Kode Pelajaran (angka): ")
        if Kode.strip() == "":
            print("Mohon masukkan kode pelajaran")
            Tbh_mata_pelajaran(cur, conn, id_admin)
            return
        Kode_lengkap = Kode_awal + Kode
        cek_query = '''SELECT * FROM mata_pelajaran'''
        cur.execute(cek_query)
        cek = cur.fetchall()
        for data in cek:
            if data[1] == Kode_lengkap:
                print("Kode Pelajaran sudah ada")
                Tbh_mata_pelajaran(cur, conn, id_admin)
                return
        Nama_pelajaran = input("Masukkan Nama Mata Pelajaran: ")
        if Nama_pelajaran.strip() == "":
            print("Mohon masukkan nama mata pelajaran")
            Tbh_mata_pelajaran(cur, conn, id_admin)
            return
        try:
            semester = int(input("Masukkan Semester (angka): "))
        except ValueError:
            print("Semester harus berupa angka")
            Tbh_mata_pelajaran(cur, conn, id_admin)
            return
        query_tambah = '''INSERT INTO mata_pelajaran (kode_pelajaran, nama_pelajaran, semester) 
                        VALUES(%s, %s, %s)'''
        cur.execute(query_tambah, (Kode_lengkap, Nama_pelajaran, semester))
        conn.commit()
        input("Data berhasil ditambahkan, enter untuk kembali")
    Mata_pelajaran(cur, conn, id_admin)

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
            try:
                cur.execute(query_delete, (Kode,))
                conn.commit()
                input("Data mata pelajaran berhasil dihapus.")
                Mata_pelajaran(cur,conn,id_admin)
            except psycopg2.IntegrityError as e: 
                input("Gagal menghapus data karena ada relasi dengan data lain.")
                conn.rollback()
                Mata_pelajaran(cur,conn,id_admin)
        else :
            Mata_pelajaran(cur,conn,id_admin)
    else:
        print("Kode mata pelajaran tidak ditemukan.")
        Hapus_mata_pelajaran(cur,conn,id_admin)

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
        print(f"Kelas                   : {cek[8]}")
        if cek[6] == 1:
            print(f"Status                  : {'Aktif'}")
        else:
            print(f"Status                  : {'Tidak Aktif'}")
        if cek[7] == None:
            print(f"Keterangan              : {'Belum ada keterangan'}")
        else :
            print(f"Keterangan              : {cek[7]}")
        print(f"--Edit beberapa data--")
        Nisn_baru = input(f"Nisn                    : ") or cek[0]
        Nama_siswa = input(f"Nama siswa              : ")or cek[1]
        No_telp = input(f"No Telepon              : ")or cek[2]
        query_kelas = '''SELECT * FROM kelas'''
        cur.execute(query_kelas)
        cek_kelas = cur.fetchall()
        for i in cek_kelas:
            print(f"id : {i[0]} kelas : {i[1]}")
        Kelas = input (f"Pilih id kelas          : ")or cek[8]
        Kelas = int(Kelas)
        Status = input(f"Status (1/0)                : ")or cek[6]
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
    
        if cek[12] == None:
            print(f"Keterangan              : {'Belum ada keterangan'}")
        else :
            print(f"Keterangan              : {cek[12]}")
        input(f"Tekan enter untuk kembali...")
        Siswa(cur,conn,id_admin)
    else:
        input(f"Nisn siswa {Nisn} tidak ditemukan.")
        Siswa(cur,conn,id_admin)
        
def Admin_Guru(cur,conn,id_admin):
    clear()
    query = """
            select g.nama_guru, g.no_telp, g.jenis_kelamin, mp.nama_pelajaran, a.provinsi|| ', '||a.kabupatenkota || ', '|| a.kecamatan || ', '|| a.jalan || ', '|| detail, g.status, g.deskripsi, g.nip
            from guru g
            join alamat a on g.id_alamat = a.id_alamat
            join mata_pelajaran mp on g.id_pelajaran = mp.id_pelajaran
            """
    cur.execute(query=query)
    data = cur.fetchall()
    No = 0
    # tampilan_guru()
    print(f'No\t Nama \t\t\t Nomor Telepon\t Gender\tMapel\tAlamat\tAdmin\tStatus\tDeskripsi\tNIP\n{"-"*125}')
    for i in data:
        No += 1
        if len(i[1]) <= 5 and (i[8] != 'null' or len(i[8]) <= 5):
            print(f"{No}\t {i[1]}\t\t\t {i[2]}\t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t{i[9]}")
        if len(i[1]) <= 15 and (i[8] != 'null' or len(i[8]) <= 5):
            print(f"{No}\t {i[1]}\t\t {i[2]} \t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t\t{i[9]}")
        elif len(i[1]) > 15 and (i[8] != 'null' or len(i[8]) <= 5):
            print(f"{No}\t {i[1]}\t {i[2]} \t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t\t{i[9]}")
        elif len(i[1]) <= 5 and (i[8] != 'null' or len(i[8]) > 5):
            print(f"{No}\t {i[1]}\t\t {i[2]} \t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t{i[9]}")
        elif len(i[1]) <= 15 and (i[8] != 'null' or len(i[8]) > 5):
            print(f"{No}\t\t {i[1]}\t {i[2]} \t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t{i[9]}")
        elif len(i[1]) > 15 and (i[8] != 'null' or len(i[8]) > 5):
            print(f"{No}\t\t {i[1]}\t {i[2]} \t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t{i[9]}")
    print("="*125)
    print("[1] Tambah")
    print("[2] Edit")
    print("[3] Kembali")
    print("="*125)
    pilih_menu = input(f"Pilih menu nomor (1/2/3/4) : ")
    match pilih_menu:
        case '1':
            Tambah_Guru(cur,conn,id_admin)
        case '2':
            print('edit data')
            Update_Guru(cur,conn,id_admin)
        case '3':
            Menu_admin(cur,conn,id_admin)
        case _:
            input("Perintah tidak diketahui!")
            Admin_Guru(cur,conn,id_admin)

def Tambah_Guru(cur, conn,id_admin):
    clear()
    print("=" * 42)
    print("|" + " " * 12 + "Tambah Data Guru" + " " * 12 + "|")
    print("=" * 42)
    nama_guru = input("Nama : ")
    no_telp = input("Nomer Telepon : ")
    while True:
        gender = input("Gender (L/P): ")
        if gender == 'L' or gender == 'P':
            break
    cek_pelajaran = "select kode_pelajaran, nama_pelajaran from mata_pelajaran"
    cur.execute(cek_pelajaran)
    cek = cur.fetchall()
    No = 0
    for i in cek:
        No += 1
        print(f"{No}\t {i[1]}") 
    pelajaran = input("Nomer pelajaran : ")
    for data in cek:
        if data[0] == 'KD'+pelajaran:
            break
        else:
            input("Kode mata pelajaran tidak ada")
            Tambah_Guru(cur, conn,id_admin)
    
    provinsi = input    ("Provinsi tempat tinggal       : ")
    kabupaten = input   ("Kabupaten/Kota tempat tinggal : ")
    kecamatan = input   ("Kecamatan tempat tinggal      : ")
    jalan = input       ("Jalan tempat tinggal          : ")
    detail = input      ("Detail alamat (opsional)      : ")
    nip = input         ("NIP                           : ")
    x = True
    print("-"*42)
    while x == True:
        confirm = input("Apakah anda ingin memasukkan data ini ? (y/n) : ")
        if confirm == 'y': 
            x = False
        elif confirm == 'n':
            x = False
            Admin_Guru(cur, conn,id_admin)

    #add alamat ke db
    if detail == '':
        query_tambah_alamat =  '''insert into alamat (provinsi, kabupatenkota, kecamatan, jalan)
                        values(%s, %s, %s, %s)'''
        cur.execute(query_tambah_alamat, (provinsi, kabupaten, kecamatan, jalan))
    else:
        query_tambah_alamat =  '''insert into alamat (provinsi, kabupatenkota, kecamatan, jalan, detail)
                        values(%s, %s, %s, %s, %s)'''
        cur.execute(query_tambah_alamat, (provinsi, kabupaten, kecamatan, jalan, detail))
    conn.commit()
    
    #add guru ke db
    cek_alamat = "select * from alamat"
    cur.execute(cek_alamat)
    cek = cur.fetchall()
    count = 0
    for i in cek:
        count+=1
    query_tambah = '''insert into guru (nama_guru, no_telp, jenis_kelamin, id_pelajaran, id_alamat, id_admin, status, nip)
                    values(%s, %s, %s, %s, %s, %s, %s, %s)'''
    cur.execute(query_tambah,(nama_guru, no_telp, gender, pelajaran, count, id_admin, True, nip ))
    conn.commit()

    ulang = input ("Data guru behasil ditambahkan!\nApakah ingin menambah data baru ? (y/n)")
    if ulang == 'y':
        Tambah_Guru(cur,conn,id_admin)
    if ulang == 'n':
        Admin_Guru(cur, conn,id_admin)

def Update_Guru(cur, conn, id_admin):
    clear()
    query_cek_data = "select * from guru"
    cur.execute(query_cek_data)
    data = cur.fetchall()
    print("=" * 125)
    print("|" + " " * 54 + "Update Data Guru" + " " * 53 + "|")
    print("=" * 125)
    print(f'No\t\t Nama \t\t Nomor Telepon\t Gender\tMapel\tAlamat\tAdmin\tStatus\tDeskripsi\tNIP')
    print("-"*125)
    No = 0
    for i in data:
        No += 1
        if len(i[1]) <= 5 and (i[8] != 'null' or len(i[8]) <= 5):
            print(f"{No}\t {i[1]}\t\t\t {i[2]}\t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t{i[9]}")
        if len(i[1]) <= 15 and (i[8] != 'null' or len(i[8]) <= 5):
            print(f"{No}\t {i[1]}\t\t {i[2]} \t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t\t{i[9]}")
        elif len(i[1]) > 15 and (i[8] != 'null' or len(i[8]) <= 5):
            print(f"{No}\t {i[1]}\t {i[2]} \t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t\t{i[9]}")
        elif len(i[1]) <= 5 and (i[8] != 'null' or len(i[8]) > 5):
            print(f"{No}\t {i[1]}\t\t {i[2]} \t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t{i[9]}")
        elif len(i[1]) <= 15 and (i[8] != 'null' or len(i[8]) > 5):
            print(f"{No}\t\t {i[1]}\t {i[2]} \t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t{i[9]}")
        elif len(i[1]) > 15 and (i[8] != 'null' or len(i[8]) > 5):
            print(f"{No}\t\t {i[1]}\t {i[2]} \t {i[3]}\t{i[4]}\t{i[5]}\t{i[6]}\t{i[7]}\t{i[8]}\t{i[9]}")
    print("="*125)
    while True:
        id = input ("nomer dari data yang ingin diubah : ")
        if id != "":
            id = int(id)
            break
    
    count = 0
    for i in data:
        count+=1
        if count == id:
            data_lama_guru = i

    print("Inputkan data baru!\nTekan Enter jika data tidak diubah!")
    nama = input      ("Nama          :")
    if nama == '':
        nama = data_lama_guru[1]
    no_telp = input   ("Nomer Telepon :")
    if no_telp == '':
        no_telp = data_lama_guru[2]
    gender = input    ("Gender (L/P)  :")
    if gender == '':
        gender = data_lama_guru[3]
    cek_pelajaran = "select kode_pelajaran, nama_pelajaran from mata_pelajaran"
    cur.execute(cek_pelajaran)
    cek = cur.fetchall()
    No = 0
    for i in cek:
        No += 1
        print(f"{No}\t {i[1]}")
    loop = True
    while loop == True:
        pelajaran = input("nomer Pelajaran  :")
        if pelajaran == '':
            pelajaran = data_lama_guru[4]
            loop = False
        else:
            kode = True
            for data in  cek:
                if data[0] == 'KD'+pelajaran:
                    loop = False
                    kode = False
                    break
            if kode == True:
                input("kode mata pelajaran tidak ada")
    
    cek_alamat = "select * from alamat"
    cur.execute(cek_alamat)
    cek_data = cur.fetchall()
    count_id = 0
    for data in cek_data:
        count_id += 1
        if data[0] == data_lama_guru[5]:
            data_lama_alamat = data

    provinsi = input    ("Provinsi tempat tinggal       : ")
    if provinsi == '':
        provinsi = data_lama_alamat[1]
    kabupaten = input   ("Kabupaten/Kota tempat tinggal : ")
    if kabupaten == '':
        kabupaten = data_lama_alamat[2]
    kecamatan = input   ("Kecamatan tempat tinggal      : ")
    if kecamatan == '':
        kecamatan = data_lama_alamat[3]
    jalan = input       ("Jalan tempat tinggal          : ")
    if jalan == '':
        jalan = data_lama_alamat[4]
    detail = input      ("Detail alamat (Opsional)      : ")
    if detail == '':
        detail = data_lama_alamat[5]
    while True:
        status = input  ("Status (Aktif/Tidak)          : ")
        if status == '':
            if data_lama_guru[6] == True:
                status = 'true'
            else:
                status = 'false'
            deskripsi = data_lama_guru[8]
            break
        elif status == 'Aktif':
            status = 'true'
            deskripsi = ''
            break
        elif status == "Tidak":
            status = 'false'
            deskripsi = input ("Deskripsi                     : ")
            break
    nip = input         ("NIP                           : ")
    if nip == '':
        nip = data_lama_guru[9]

    print("-"*125)
    x = True
    while x == True:
        confirm = input("Apakah anda ingin memasukkan data ini ? (y/n) : ")
        if confirm == 'y': 
            x = False
        elif confirm == 'n':
            x = False
            Admin_Guru(cur, conn,id_admin)

    #update alamat
    query_update_alamat = f'''update alamat set   provinsi = '{provinsi}', 
                                            kabupatenkota = '{kabupaten}', 
                                            kecamatan = '{kecamatan}', 
                                            jalan = '{jalan}', 
                                            detail = '{detail}' 
                        where id_alamat = {count_id}'''
    cur.execute(query_update_alamat)
    conn.commit()

    #update guru
    query_update_guru = f'''update guru set nama_guru = '{nama}',
                                            no_telp = '{no_telp}', 
                                            jenis_kelamin = '{gender}',
                                            id_pelajaran = {pelajaran},
                                            id_admin = {id_admin}
                                            status = {status},
                                            deskripsi = '{deskripsi}',
                                            nip = '{nip}'
                            where id_guru = {id} '''
    cur.execute(query_update_guru)
    conn.commit()

    ulang = input ("Data guru behasil diupdate!\nApakah ingin update data lain ? (y/n)")
    if ulang == 'y':
        Update_Guru(cur,conn,id_admin)
    if ulang == 'n':
        Admin_Guru(cur, conn,id_admin)

def Jadwal_pelajaran_a(cur, conn, id_admin):
    print("=" * 31)
    print("|" + " " * 6 + "Jadwal Pelajaran" + " " * 7 + "|")
    print("=" * 31)
    print("[1] Tambah")
    print("[2] Edit")
    print("[3] Detail")
    print("[4] Kembali")
    print("="*93)
    pilih_menu = input(f"Pilih menu nomor (1/2/3/4) : ")
    match pilih_menu:
        case '1':
            Tambah_jadwal(cur, conn, id_admin)
        case '2':
            Edit_jadwal(cur, conn, id_admin)
        case '3':
            Detail_jadwal_a(cur, conn, id_admin)
        case '4':
            Menu_admin(cur, conn, id_admin)
        case _:
            input("Perintah tidak diketahui!")
            Jadwal_pelajaran_a(cur, conn, id_admin)

def Tambah_jadwal(cur, conn, id_admin):
    print("--Tambah Jadwal--")
    hari = input("Masukkan hari: ")
    awal_pelajaran = input("Masukkan waktu awal pelajaran (HH:MM:SS): ")
    akhir_pelajaran = input("Masukkan waktu akhir pelajaran (HH:MM:SS): ")
    id_guru = int(input("Masukkan ID guru: "))
    id_kelas = int(input("Masukkan ID kelas: "))

    try:
        # Mencari id_pelajaran berdasarkan id_guru
        cur.execute("SELECT id_pelajaran FROM guru WHERE id_guru = %s", (id_guru,))
        id_pelajaran = cur.fetchone()[0]

        # Cek apakah ada jadwal yang tumpang tindih pada hari dan kelas yang sama
        cur.execute("""
            SELECT COUNT(*) FROM jadwal_pelajaran 
            WHERE hari = %s AND id_kelas = %s AND (
                (awal_pelajaran <= %s AND akhir_pelajaran > %s) OR
                (awal_pelajaran < %s AND akhir_pelajaran >= %s) OR
                (%s <= awal_pelajaran AND %s >= akhir_pelajaran)
            )
        """, (hari, id_kelas, awal_pelajaran, awal_pelajaran, akhir_pelajaran, akhir_pelajaran, awal_pelajaran, akhir_pelajaran))
        overlapping_count = cur.fetchone()[0]

        if overlapping_count > 0:
            print("Jadwal bentrok dengan jadwal yang sudah ada, tidak dapat menambahkan data.")
            Tambah_jadwal(cur, conn, id_admin)
        else:
            cur.execute("""
                INSERT INTO jadwal_pelajaran (hari, awal_pelajaran, akhir_pelajaran, id_guru, id_pelajaran, id_kelas)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (hari, awal_pelajaran, akhir_pelajaran, id_guru, id_pelajaran, id_kelas))
            conn.commit()
            print("Jadwal berhasil ditambahkan.")
            Jadwal_pelajaran_a(cur, conn, id_admin)
    except TypeError:
        print("ID guru tidak valid atau tidak terkait dengan mata pelajaran apa pun.")
        Tambah_jadwal( cur, conn, id_admin)
    except Exception as e:
        conn.rollback()
        print(f"Terjadi kesalahan: {e}")
        Jadwal_pelajaran_a(cur, conn, id_admin)

def Edit_jadwal(cur, conn, id_admin):
    print("--Edit Jadwal--")
    id_jadwal = int(input("Masukkan ID jadwal yang akan diedit: "))
    print("Pilih kolom yang ingin diedit:")
    print("[1] Hari")
    print("[2] Awal Pelajaran")
    print("[3] Akhir Pelajaran")
    print("[4] ID Guru")
    print("[5] ID Pelajaran")
    print("[6] ID Kelas")
    print("[7] Edit Semua")
    pilihan = input("Masukkan pilihan (1/2/3/4/5/6/7): ")

    update_fields = []
    update_values = []

    if pilihan in ['1', '7']:
        hari = input("Masukkan hari baru: ")
        update_fields.append("hari = %s")
        update_values.append(hari)
    if pilihan in ['2', '7']:
        awal_pelajaran = input("Masukkan waktu awal pelajaran baru (HH:MM:SS): ")
        update_fields.append("awal_pelajaran = %s")
        update_values.append(awal_pelajaran)
    if pilihan in ['3', '7']:
        akhir_pelajaran = input("Masukkan waktu akhir pelajaran baru (HH:MM:SS): ")
        update_fields.append("akhir_pelajaran = %s")
        update_values.append(akhir_pelajaran)
    if pilihan in ['4', '7']:
        id_guru = int(input("Masukkan ID guru baru: "))
        update_fields.append("id_guru = %s")
        update_values.append(id_guru)
    if pilihan in ['5', '7']:
        id_pelajaran = int(input("Masukkan ID pelajaran baru: "))
        update_fields.append("id_pelajaran = %s")
        update_values.append(id_pelajaran)
    if pilihan in ['6', '7']:
        id_kelas = int(input("Masukkan ID kelas baru: "))
        update_fields.append("id_kelas = %s")
        update_values.append(id_kelas)

    update_values.append(id_jadwal)

    if not update_fields:
        print("Tidak ada perubahan yang dipilih.")
        return

    update_query = f"UPDATE jadwal_pelajaran SET {', '.join(update_fields)} WHERE id_jadwal = %s"
    
    try:
        cur.execute(update_query, tuple(update_values))
        conn.commit()
        print("Jadwal berhasil diubah.")
        Jadwal_pelajaran_a(cur, conn, id_admin)
    except Exception as e:
        conn.rollback()
        print(f"Terjadi kesalahan: {e}")
        Jadwal_pelajaran_a(cur, conn, id_admin)

def Detail_jadwal_a(cur, conn, id_admin):
    print("--Detail Jadwal--")
    print("Pilih jenis pencarian:")
    print("[1] Berdasarkan ID Jadwal")
    print("[2] Berdasarkan Hari")
    print("[3] Berdasarkan ID Kelas")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    query = ""
    parameter = None

    if pilihan == '1':
        id_jadwal = int(input("Masukkan ID jadwal: "))
        query = "SELECT * FROM jadwal_pelajaran WHERE id_jadwal = %s"
        parameter = (id_jadwal,)
    elif pilihan == '2':
        hari = input("Masukkan hari: ")
        query = "SELECT * FROM jadwal_pelajaran WHERE hari = %s"
        parameter = (hari,)
    elif pilihan == '3':
        id_kelas = int(input("Masukkan ID kelas: "))
        query = "SELECT * FROM jadwal_pelajaran WHERE id_kelas = %s"
        parameter = (id_kelas,)
    else:
        print("Pilihan tidak valid.")
        return

    try:
        cur.execute(query, parameter)
        jadwals = cur.fetchall()
        if jadwals:
            print("="*90)
            headers = ["ID Jadwal", "Hari", "Awal Pelajaran", "Akhir Pelajaran", "ID Guru", "ID Pelajaran", "ID Kelas"]
            print(f"{headers[0]:<12} {headers[1]:<9} {headers[2]:<16} {headers[3]:<17} {headers[4]:<8} {headers[5]:<12} {headers[6]:<8}")
            print("="*90)
            for jadwal in jadwals:
                awal_pelajaran = jadwal[2].strftime("%H:%M:%S")
                akhir_pelajaran = jadwal[3].strftime("%H:%M:%S")
                print(f"{jadwal[0]:<12} {jadwal[1]:<9} {awal_pelajaran:<16} {akhir_pelajaran:<17} {jadwal[4]:<8} {jadwal[5]:<12} {jadwal[6]:<8}")
                Detail_jadwal_a(cur, conn, id_admin)
        else:
            print("Jadwal tidak ditemukan.")
            Detail_jadwal_a(cur, conn, id_admin)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        Jadwal_pelajaran_a(cur, conn, id_admin)
        
def Login_guru(cur,conn):
    clear()
    tampilan_guru()
    nama_guru = input(f"Masukkan Nama : ")
    nip = input(f"Masukkan NIP  : ")
    select_query = "SELECT * FROM guru WHERE nama_guru = %s AND nip = %s"
    cur.execute(select_query, (nama_guru, nip))
    data2 = cur.fetchone()
    if data2:
        Menu_guru(cur,conn,nama_guru)
    else:
        input('Username atau password salah.')
        Login_guru(cur,conn)  
        
def Menu_guru(cur,conn,nama_guru):
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
            Jadwal_pelajaran_g(cur,conn,nama_guru)
        case '2':
            Jenis_tugas(cur,conn,nama_guru)
        case '3':
            Nilai_Siswa(cur, conn, nama_guru)
        case '4':
            Menu_utama(cur,conn) 
        case _:
            input("Perintah tidak diketahui!")
            Menu_guru(cur,conn,nama_guru) 

def Jadwal_pelajaran_g(cur, conn,nama_guru):
    print("=" * 31)
    print("|" + " " * 6 + "Jadwal Pelajaran" + " " * 7 + "|")
    print("=" * 31)
    print("[1] Detail")
    print("[2] Kembali")
    print("=" * 31)
    pilih_menu = input(f"Pilih menu nomor (1/2) : ")
    match pilih_menu:
        case '1':
            Detail_jadwal_g(cur, conn,nama_guru)
        case '2':
            Menu_guru(cur,conn,nama_guru)
        case _:
            input("Perintah tidak diketahui!")
            Jadwal_pelajaran_g(cur, conn,nama_guru)

def Detail_jadwal_g(cur, conn,nama_guru):
    print("--Detail Jadwal--")
    print("Pilih jenis pencarian:")
    print("[1] Berdasarkan ID Jadwal")
    print("[2] Berdasarkan Hari")
    print("[3] Berdasarkan ID Kelas")
    pilihan = input("Masukkan pilihan (1/2/3): ")

    query = ""
    parameter = None

    if pilihan == '1':
        id_jadwal = int(input("Masukkan ID jadwal: "))
        query = "SELECT * FROM jadwal_pelajaran WHERE id_jadwal = %s"
        parameter = (id_jadwal,)
    elif pilihan == '2':
        hari = input("Masukkan hari: ")
        query = "SELECT * FROM jadwal_pelajaran WHERE hari = %s"
        parameter = (hari,)
    elif pilihan == '3':
        id_kelas = int(input("Masukkan ID kelas: "))
        query = "SELECT * FROM jadwal_pelajaran WHERE id_kelas = %s"
        parameter = (id_kelas,)
    else:
        print("Pilihan tidak valid.")
        return

    try:
        cur.execute(query, parameter)
        jadwals = cur.fetchall()
        if jadwals:
            print("="*90)
            headers = ["ID Jadwal", "Hari", "Awal Pelajaran", "Akhir Pelajaran", "ID Guru", "ID Pelajaran", "ID Kelas"]
            print(f"{headers[0]:<12} {headers[1]:<9} {headers[2]:<16} {headers[3]:<17} {headers[4]:<8} {headers[5]:<12} {headers[6]:<8}")
            print("="*90)
            for jadwal in jadwals:
                awal_pelajaran = jadwal[2].strftime("%H:%M:%S")
                akhir_pelajaran = jadwal[3].strftime("%H:%M:%S")
                print(f"{jadwal[0]:<12} {jadwal[1]:<9} {awal_pelajaran:<16} {akhir_pelajaran:<17} {jadwal[4]:<8} {jadwal[5]:<12} {jadwal[6]:<8}")
                Jadwal_pelajaran_g(cur, conn,nama_guru)
        else:
            print("Jadwal tidak ditemukan.")
            Detail_jadwal_g(cur, conn,nama_guru)
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        Jadwal_pelajaran_g(cur, conn,nama_guru)

def Jenis_tugas(cur,conn,nama_guru):
    clear()
    print("=" * 41)
    print("|" + " " * 14 + "Jenis Tugas" + " " * 14 + "|")
    print("=" * 41)
    print(f"{'No':<13} {'ID':<13} {'Jenis Tugas'}")
    print("-"*41)
    query_kelas = '''SELECT * FROM jenis_tugas'''
    cur.execute(query_kelas)
    data = cur.fetchall()
    No = 0;
    for i in data:
        No += 1;
        print(f"{No:<13} {i[0]:<13} {i[1]}")
    print("="*41)
    print("[1] Tambah")
    print("[2] Edit")
    print("[3] Hapus")
    print("[4] Kembali")
    print("="*41)
    pilih_menu = input(f"Pilih menu nomor (1/2/3/4) : ")
    match pilih_menu:
        case '1':
            Tambah_jenis_tugas(cur,conn,nama_guru)
        case '2':
            Edit_jenis_tugas(cur,conn,nama_guru)
        case '3':
            Hapus_jenis_tugas(cur,conn,nama_guru)
        case '4':
            Menu_guru(cur,conn,nama_guru)
        case _:
            input("Perintah tidak diketahui!")
            Jenis_tugas(cur,conn,nama_guru)  

def Tambah_jenis_tugas(cur,conn,nama_guru):
    print(f"-- Tambah Jenis Tugas  --")
    total_input = int(input(f"Ingin Menambahkan Berapa Data : "))
    for i in range(total_input):
        id_tugas = input(f"Masukkan ID Tugas (Angka) : ")
        cek_query = '''SELECT * FROM jenis_tugas'''
        cur.execute(cek_query)
        cek = cur.fetchall()
        for data in cek:
            if data[0] == id_tugas:
                print("ID Jenis Tugas Sudah Ada")
                Tambah_jenis_tugas(cur,conn,nama_guru)

            else:
                jenis_tugas = input(f"Masukkan Jenis Tugas    : ")
                query_tambah_jenis_tugas = '''INSERT INTO jenis_tugas (id_tugas, jenis_tugas) 
                                VALUES(%s, %s)'''
                cur.execute(query_tambah_jenis_tugas,(id_tugas, jenis_tugas))
                conn.commit()
                Jenis_tugas(cur,conn,nama_guru)

def Edit_jenis_tugas(cur,conn,nama_guru):
    print(f"-- Edit Jenis Tugas --")
    id_tugas= input(f"Masukkan ID Tugas Yang Ingin Diupdate: ")
    select_query_jenis_tugas = '''SELECT * FROM jenis_tugas WHERE id_tugas = %s'''
    cur.execute(select_query_jenis_tugas, (id_tugas,))
    cek = cur.fetchone()
    if cek:
        print("Data Saat Ini")
        print(f"ID Tugas       :  {cek[0]}")
        print(f"Jenis Tugas    :  {cek[1]}")
        Nama_Kelas = input(f"Masukkan Nama Jenis Tugas : ") or cek[1]
        update_query_jenis_tugas = '''
            UPDATE jenis_tugas
            SET jenis_tugas = %s
            WHERE id_tugas = %s
        '''
        cur.execute(update_query_jenis_tugas, (Nama_Kelas, id_tugas))
        conn.commit()
        input("Data Jenis Tugas Telah Diperbarui.")
        Jenis_tugas(cur,conn,nama_guru)
    else:
        print("ID Jenis Tugas Tidak Ditemukan.")
        Edit_jenis_tugas(cur,conn,nama_guru)

def Hapus_jenis_tugas(cur,conn,nama_guru):
    print(f"-- Hapus Jenis TUgas --")
    id_tugas = input(f"Masukkan ID Tugas Yang Ingin Dihapus : ")
    select_query_jenis_tugas = '''SELECT * FROM jenis_tugas WHERE id_tugas = %s'''
    cur.execute(select_query_jenis_tugas,(id_tugas,))
    cek = cur.fetchone()
    if cek:
        print("Data Saat Ini")
        print(f"ID Tugas       :  {cek[0]}")
        print(f"Jenis Tugas    :  {cek[1]}")
        konfir = input(f"Apakah Anda Yakin Untuk Menghapus? (y/n) : ")
        if konfir == "y":
            query_delete_jenis_tugas = '''DELETE FROM jenis_tugas WHERE id_tugas = %s'''
            cur.execute(query_delete_jenis_tugas,(id_tugas,))
            conn.commit()
            input("Hapus Data Jenis Tugas Berhasil.")
            Jenis_tugas(cur,conn,nama_guru)
        else:
            Jenis_tugas(cur,conn,nama_guru)
    else:
        print("ID Jenis Tugas Tidak Ditemukan.")
        Hapus_jenis_tugas(cur,conn,nama_guru)
        
def Nilai_Siswa(cur,conn,nama_guru):
    clear()
    cek_kelas = """
            select *
            from kelas
            """
    cur.execute(cek_kelas)
    data_kelas = cur.fetchall()
    print("="*18)
    print("|" + " " * 3 + "Nilai Siswa" + " " * 2 + "|")
    print("="*18)
    print(f'No\tKelas\n{"-"*18}')
    for i in data_kelas:
        print(f'{i[0]}\t{i[1]}')
    print("="*18)

    while True:
        id = input ("Nomer Kelas : ")
        if id != "":
            id = int(id)
            break
    for kelas in data_kelas:
        if kelas[0] == id:
            pkelas = kelas[1]
#=================================================================
    clear()
    cek_siswa = f'''select *
                    from siswa
                    where id_kelas = {id}'''
    cur.execute(cek_siswa)
    data_siswa = cur.fetchall()

    # cek_seluruh_siswa = f'''select *
    #                 from siswa'''
    # cur.execute(cek_siswa)
    # data_siswa = cur.fetchall()

    print("="*30)
    print("|" + " " * 9 + "Nilai Siswa" + " " * 8 + "|")
    print("="*30)
    print(f"| {' '*6} Kelas {pkelas} {' '*5} |")
    print("="*30)
    print(f'No\tNama\n{"-"*30}')
    No = 0
    for x in data_siswa:
        No+=1
        print(f'{No}\t{x[2]}')
    print("="*30)

    while True:
        id = input ("Nomer Siswa : ")
        if id != "":
            id = int(id)
            break
    cek_nomer = 0
    for c in data_siswa:
        cek_nomer += 1
        if cek_nomer == id:
            absen = c
        
#=================================================================
    clear()
    guru = "select * from guru"
    cur.execute(guru)
    cek_guru = cur.fetchall()
    for data_guru in cek_guru:
        if data_guru[1] == nama_guru:
            id_guru = data_guru
    cek_nilai= f''' select *
                    from nilai_siswa ns
                    join jenis_tugas jt on ns.id_tugas = jt.id_tugas
                    where id_siswa = {id} and id_guru = {id_guru[0]}'''
    cur.execute(cek_nilai)
    data_nilai = cur.fetchall()

    print("="*30)
    print("|" + " " * 9 + "Nilai Siswa" + " " * 8 + "|")
    print("="*30)
    print(f'No\tTugas\t\tNilai\n{"-"*30}')
    No=0
    for y in data_nilai:
        No+=1
        print(f"{No}\t{y[6]}\t\t{y[1]}")
    print("="*30)
    print("[1] Tambah")
    print("[2] Edit")
    print("[3] Hapus")
    print("[4] Kembali")
    print("="*30)
    pilih_menu = input(f"Pilih menu nomor (1/2/3/4) : ")
    match pilih_menu:
        case '1':
            Tambah_Nilai(cur,conn,absen,nama_guru)
        case '2':
            print('edit data')
            Update_Nilai(cur,conn,absen,nama_guru)
        case '3':
            print('hapus data')
            Delete_Nilai(cur,conn,absen,nama_guru)
        case '4':
            print('kembali')
            
        case _:
            input("Perintah tidak diketahui!")
            Nilai_Siswa(cur,conn,)

def Tambah_Nilai(cur,conn,absen,nama_guru):
    clear()

    query_tugas = "select * from jenis_tugas"
    cur.execute(query_tugas)
    cek_tugas = cur.fetchall()
    id_tugas = 0
    for jenis in cek_tugas:
        id_tugas+=1
        print(f"{jenis[0]}\t{jenis[1]}")
    id_tugas+=1
    tugas = input("Nama tugas   : ")
    verif = False
    for a in cek_tugas:
        if a[1] == tugas:
            verif = True
            id_tugas = a[0]
            break
    if verif == False:
        while True:
            jenis_baru = input("Jenis tugas Tidak ada. Apakah ingin menambahkan jenis tugas baru ? (y/n) : ")
            if jenis_baru == 'n':
                Tambah_Nilai(cur,conn)
            elif jenis_baru == 'y':

                query_tambah_tugas = '''insert into jenis_tugas (id_tugas, jenis_tugas)
                            values(%s, %s)'''
                cur.execute(query_tambah_tugas, (id_tugas, tugas))
                conn.commit()
                break
    
    Try = True
    while Try == True:
        Try = False
        Nilai = input("Nilai        : ")
        try:
            Nilai = int(Nilai)
        except SyntaxError:
            Try = True

    query_tambah_nilai = '''insert into nilai_siswa (nilai_tugas, id_guru, id_siswa, id_tugas)
                            values(%s, %s, %s, %s)'''
    cur.execute(query_tambah_nilai, (Nilai, 1, absen[0], id_tugas))
    conn.commit()

    ulang = input ("Nilai behasil ditambahkan!\nApakah ingin memasukkan nilai lain ? (y/n)")
    if ulang == 'y':
        Tambah_Nilai(cur,conn,absen,nama_guru)
    elif ulang == 'n':
        Nilai_Siswa(cur, conn,nama_guru)

def Update_Nilai(cur,conn,absen,nama_guru):
    clear()
    guru = "select * from guru"
    cur.execute(guru)
    cek_guru = cur.fetchall()
    for data_guru in cek_guru:
        if data_guru[1] == nama_guru:
            id_guru = data_guru

    cek_nilai= f''' select *
                    from nilai_siswa ns
                    join jenis_tugas jt on ns.id_tugas = jt.id_tugas
                    where id_siswa = {absen[0]} and id_guru = {id_guru[0]} '''
    cur.execute(cek_nilai)
    data_nilai = cur.fetchall()
    print("=" * 30)
    print("|" + " " * 5 + "Update Nilai Siswa" + " " * 5 + "|")
    print("=" * 30)
    print(f'No\tTugas\t\tNilai\n{"-"*30}')
    No=0
    for y in data_nilai:
        No+=1
        print(f"{No}\t{y[6]}\t\t{y[1]}")
    print("="*30)
    valid = False
    while valid == False:
        tugas = input("Nama tugas    : ")
        for jenis in data_nilai:
            if jenis[6] == tugas:
                valid = True
                tugas = jenis[4]
                break
        if valid == False:
            input("Tugas tidak ada! Silahkan masukkan tugas kembali")

    x=True
    while x == True:
        x=False
        Nilai = input("Nilai terbaru : ")
        try:
            Nilai = int(Nilai)
        except SyntaxError:
            x=True
    query_update_nilai = f'''update nilai_siswa set nilai_tugas = {Nilai}
                            where id_tugas = {tugas} and id_siswa = {absen[0]} and id_guru = {id_guru[0]} '''
    cur.execute(query_update_nilai)
    conn.commit()

    ulang = input ("Nilai berhasil diubah!\nApakah ingin mengubah nilai lain ? (y/n)")
    if ulang == 'y':
        Update_Nilai(cur,conn,absen,nama_guru)
    elif ulang == 'n':
        Nilai_Siswa(cur, conn, nama_guru)

def Delete_Nilai(cur,conn,absen,nama_guru):
    clear()
    guru = "select * from guru"
    cur.execute(guru)
    cek_guru = cur.fetchall()
    for data_guru in cek_guru:
        if data_guru[1] == nama_guru:
            id_guru = data_guru

    cek_nilai = f"""select *
                    from nilai_siswa ns
                    join jenis_tugas jt on ns.id_tugas = jt.id_tugas
                    where id_siswa = {absen[0]} and id_guru = {id_guru[0]}"""
    cur.execute(cek_nilai)
    data_nilai = cur.fetchall()
    print("=" * 30)
    print("|" + " " * 5 + "Update Nilai Siswa" + " " * 5 + "|")
    print("=" * 30)
    print(f'No\tTugas\t\tNilai\n{"-"*30}')
    No=0
    for y in data_nilai:
        No+=1
        print(f"{No}\t{y[6]}\t\t{y[1]}")
    print("="*30)
    valid = False
    while valid == False:
        tugas = input("Nama tugas yang akan dihapus    : ")
        for jenis in data_nilai:
            if jenis[6] == tugas:
                valid = True
                tugas = jenis[0]
                break
        if valid == False:
            input("Tugas tidak ada! Silahkan masukkan tugas kembali")
    x=True
    while x == True:
        confirm = input("Apakah anda ingin menghapus nilai ini ? (y/n) : ")
        if confirm == 'y':
            x = False
        elif confirm == 'n':
            x = False
            Nilai_Siswa(cur, conn,absen,nama_guru)
    print(tugas)
    query_delete_nilai = f'''delete from nilai_siswa where id_nilai_siswa = {tugas}'''
    cur.execute(query_delete_nilai)
    conn.commit()

    ulang = input ("Nilai berhasil dihapus!\nApakah ingin menghapus data lain ? (y/n)")
    if ulang == 'y':
        Delete_Nilai(cur,conn,absen,nama_guru)
    elif ulang == 'n':
        Nilai_Siswa(cur, conn,nama_guru)


if __name__ == "__main__":
    Main()
