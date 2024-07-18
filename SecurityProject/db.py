import mysql.connector

con = mysql.connector.connect(
  host='localhost',
  user="root",
  passwd="",
  database="users"
)

cursor = con.cursor()

def saveclient(tup):
    try:
      cursor.execute('insert into active_users(userid,passid) values(%s,%s)',tup)
      con.commit()
      return True
    except:
      return False

def showClients():
  try:
    cursor = con.cursor(dictionary=True)
    cursor.execute("select * from clients")
    return cursor.fetchall()
  except:
    return []
def find(data):
  try:
    cursor = con.cursor(dictionary=True)
    cursor.execute("select * from active_users where userid=%s and passid=%s",data)
    return cursor.fetchone()
  except :
    return None
