# import psycopg2
# import os
# conn = psycopg2.connect(database='SMAN3', 
#                            user='postgres', 
#                            password='321', 
#                            host='localhost', 
#                            port=5432)
# cur = conn.cursor()

# def clear():
#    os.system('cls')
 
import psycopg2
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')  # Clear screen for portability

def tampilan():
    print("=" * 31)
    print("|" + " " * 7 + "SMAN 3 LUMAJANG" + " " * 7 + "|")
    print("=" * 31)

def menu_utama(cur):
    clear()
    tampilan()
    print("[1] Login Admin")
    print("[2] Login Guru")
    print("=" * 31)

    while True:
        pilih_menu = input("Pilih menu nomor (1/2) : ")

        if pilih_menu == '1':
            login_admin(cur)
            break  
        elif pilih_menu == '2':
            print("Fitur login guru belum tersedia.")
            break  
        else:
            print("Perintah tidak diketahui!")

def login_admin(cur):
   clear()
   query = "SELECT * FROM admin" 
   cur.execute(query)
   data = cur.fetchall()
   for i in data:
      print(i)
   username = input(f"Masukkan Username :")
   password = input(f"Masukkan Password :")
   select_query = "SELECT * FROM admin WHERE username = %s AND password = %s"
   cur.execute(select_query, (username, password))
   data2 = cur.fetchone()
   if data2:
      Admin()
   else:
      print('Username atau password salah.')
def Admin():
   print("yaholosse")
def main():
    try:
        conn = psycopg2.connect(database='SMAN3',
                                 user='postgres',
                                 password='321',
                                 host='localhost',
                                 port=5432)
        cur = conn.cursor()

        while True:
            menu_utama(cur)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        if conn:
            cur.close()
            conn.close()

if __name__ == "__main__":
    main()
