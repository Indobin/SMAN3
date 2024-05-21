import psycopg2

conn = psycopg2.connect(database = 'Coba',
                        user = 'postgres',
                        password = '321',
                        host = 'localhost',
                        port = 5432)
cur = conn.cursor()
# select mata kulih
def read_mata_kuliah(cur):
  query = '''SELECT * FROM mata_kuliah'''
  cur.execute(query)
  data = cur.fetchall()
  for i in data:
   print(i)
  # cur.close()
  # conn.close()

# Dynamic Insert Data 
# total_input = int(input(f"Ingin Menambahkan Berapa Data"))
# for i in range(total_input):
#  nama_mata_kuliah = input(f"Masukkan Nama Mata Kuliah :")
#  sks = int(input(f"Masukkan Jumlah Sks :"))
#  semester = int(input(f"Masukkan Semester :"))
#  query = f"INSERT INTO mata_kuliah (nama_mata_kuliah, sks, semester_id) VALUES(%s, %s, %s)"
# conn.commit()
# read_mata_kuliah(cur)
# cur.close()
# conn.close()

# Update
# query = '''UPDATE mata_kuliah SET nama_mata_kuliah = %s, sks = %s, semester_id = %s'''
# # read_mata_kuliah(cur)

# # read semua mata kuliah
# query_select  = '''SELECT * FROM mata_kuliah'''
# cur.execute(query=query_select)
# data = cur.fetchall()
# for i in data:
#  print(i)
 
# # read mata kuliah berdasarkan id 
# id_matkul = input(f"Masukan id mata kuliah yang di update : ")
# select_query = '''SELECT * FROM mata_kulah WHERE id_mata_kuliah = %s'''
# cur.execute(query=select_query, vars=(id_matkul))
# data2 = cur.fetchone()
# if data2:
#  print("Data Saat Ini")
#  print(f"id mata kuliah : {data2[0]}")
#  print(f"nama mata kuliah : {data2[1]}")
#  print(f"sks mata kuliah : {data2[2]}")
#  print(f"semester mata kuliah : {data2[3]}")
 
# nama_mata_kuliah = input(f"Masukkan Nama Mata Kuliah :") or data[1]
# sks = input(f"Masukkan Jumlah Sks :") or data2[2]
# sks = int(sks)
# semester_id = int(input(f"Masukkan Semester :")) or data2[3]
# query_update = '''UPDATE mata_kuliah SET nama_mata_kuliah = %s, sks = %s,
# semester_id = %s WHERE id_mata_kuliah = %s'''
# cur.execute(query=query_update, vars=(nama_mata_kuliah, sks, semester_id, id_matkul))
# conn.commit()
# cur.close()
# conn.close()

# Delete
read_mata_kuliah(cur=cur)
id_mata_kuliah = input("Masukan Id mata kuliah yang ingin di hapus :")
query_delete = '''DELETE FROM mata_kuliah WHERE id_mata_kuliah = {id_mata_kuliah}'''
cur.execute(query=query_delete)

conn.commit()
cur.close()
conn.close()