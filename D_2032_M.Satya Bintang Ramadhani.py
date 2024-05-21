import psycopg2

conn = psycopg2.connect(database='Coba', user='postgres', password='321', host='localhost', port=5432)

cur = conn.cursor()

# SELECT MATA KULIAH

def read_mata_kuliah(cur):    
    query = "SELECT * FROM mata_kuliah"
    cur.execute(query)
    data = cur.fetchall()
    for i in data:
        print(i)
    # cur.close()
    # conn.close()

# SELECT SEMESTER
# query = "SELECT * FROM semester"
# cur.execute(query)
# data = cur.fetchall()
# for i in data:
#     print(i)
# cur.close()
# conn.close()

# DYNAMIC INSERT DATA
# total_input = int(input(f"Mau menambahkan berapa data?: "))

# for i in range(total_input):
#     nama_mata_kuliah = input(f"Masukkan nama mata kuliah: ")
#     sks = int(input(f"Masukkan jumlah sks: "))
#     semester_id = int(input(f"Masukkan semester: "))
#     query = f"INSERT INTO mata_kuliah(nama_mata_kuliah, sks, semester_id) VALUES('{nama_mata_kuliah}', {sks}, {semester_id})"
#     # query = f"INSERT INTO mata_kuliah(nama_mata_kuliah, sks, semester_id) VALUES(%s, %s, %s)"
#     cur.execute(query, (nama_mata_kuliah, sks, semester_id))

# conn.commit()

# read_mata_kuliah(cur)
# cur.close()
# conn.close()

# UPDATE
# UPDATE nama_table SET nama_kolom = value_kolom
# read_mata_kuliah(cur)

# READ SEMUA MATA KULIAH
# query_select = "SELECT * FROM mata_kuliah ORDER BY id_mata_kuliah ASC"
# cur.execute(query_select)
# data1 = cur.fetchall()
# for i in data1:
#     print(i)

# # READ MATA KULIAH YANG DIPILIH OLEH USER
# id_mata_kuliah =input('Masukkan id mata kuliah yang ingin di update: ')
# select_query = "SELECT * FROM mata_kuliah WHERE id_mata_kuliah = %s"
# cur.execute(select_query, (id_mata_kuliah))
# data2 = cur.fetchone()

# if data2:
#     print('Data saat ini:')
#     print(f'id mata kuliah saat ini: {data2[0]}')
#     print(f'nama mata kuliah saat ini: {data2[1]}')
#     print(f'sks mata kuliah saat ini: {data2[2]}')
#     print(f'semester mata kuliah saat ini: {data2[3]}')

# # UPDATE
# nama_mata_kuliah = input(f"Masukkan nama mata kuliah: ") or data2[1]
# sks = input(f"Masukkan jumlah sks: ") or data2[2]
# sks = int(sks)
# semester_id = input(f"Masukkan semester: ") or data2[3]

# query_update = f"UPDATE mata_kuliah SET nama_mata_kuliah = '{nama_mata_kuliah}', sks = {sks}, semester_id = {semester_id} WHERE id_mata_kuliah = {id_mata_kuliah}"

# # -- Manipulasi string
# # cur.execute(query_update, (nama_mata_kuliah, sks, semester_id, id_mata_kuliah))

# # -- Fstring
# cur.execute(query_update)

# conn.commit()
# print(f"total baris yang diubah: {cur.rowcount}")

# cur.close()
# conn.close()

# DELETE
read_mata_kuliah(cur=cur)
id_mata_kuliah = input('Masukkan id mata kuliah yang ingin dihapus: ')
query_delete = f"DELETE FROM mata_kuliah WHERE id_mata_kuliah = {id_mata_kuliah}"
cur.execute(query_delete)

print(f"total baris yang dihapus: {cur.rowcount}")

conn.commit()
cur.close()
conn.close()
