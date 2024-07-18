import mysql.connector as con

a = con.connect(
        host="localhost",
        user="root",
        password="",
        database="self"
        )
cursor=a.cursor()
def save(data):
    try:
        data1=(',').join(data)
        cursor.execute("INSERT INTO images (images) VALUES (%s)", (data1,))
        a.commit()
        return True
    except:
        return False
    
def view():
    a=cursor.execute("SELECT * FROM images ORDER BY id DESC")
    b=cursor.fetchone()[1]
    # a=cursor.execute("SELECT MAX(id) FROM images")
    # b=cursor.execute("SELECT * FROM images WHERE id=%s",a)
    print(b)
    return b
# class Db:
#     try:
#         a = con.connect(
#         host="localhost",
#         user="root",
#         password=""
#         )
#         cursor=a.cursor()
#         cursor.execute('CREATE DATABASE self')
#     except:
#         a = con.connect(
#         host="localhost",
#         user="root",
#         password="",
#         database="self"
#         )
#     cursor=a.cursor()
#     def save():
#                 data1=(',').join(['a','b','c','d'])
#         # try:
#         #     try:
#         #         Db.cursor.execute("CREATE TABLE Images(id int(30) AUTO_INCREMENT, images varchar(255), PRIMARY KEY(id))")
#         #         Db.cursor.execute("INSERT INTO Images(images) VALUES(%s)",data1)
#         #         Db.a.commit()
#         #     except:
#                 # print(data)
#                 Db.cursor.execute("INSERT INTO images (images) VALUES (%s)",('a'))
#                 Db.a.commit()
#         #     return True
#         # except:
#         #     return False

# a=Db()
# a.save()