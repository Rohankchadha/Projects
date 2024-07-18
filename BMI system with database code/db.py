import mysql.connector

con = mysql.connector.connect(
  host='localhost',
  user="root",
  passwd="",
  database="bmibase"
)

cursor = con.cursor()

def saveclient(tup,tup1):
    # print(tup[0])
    try:
      cursor.execute("select * from logindata where username=%s",(tup[0],))
      if len(cursor.fetchall())>0:
        return False, "User Already Regitered"
      else:
        cursor.execute('insert into logindata(username,pas) values(%s,%s)',tup)
        cursor.execute('insert into userdetails(username,age,weight,height) values(%s,%s,%s,%s)',tup1)
        con.commit()
        # print('true')
        return True, "User Registeration Successful"
    except:
      # print('false')
      return False, "Enter valid data"

def showClients():
  try:
    cursor = con.cursor(dictionary=True)
    cursor.execute("select * from userdetails")
    return cursor.fetchall()
  except:
    return []
def insertbydate(a):
  try:
    cursor.execute("select * from totalcal where username = %s and day = %s",(a[0],a[-1]))
    a1=cursor.fetchall()
    if len(a1)==0 or a1==None:
      cursor.execute("insert into totalcal values(%s,%s,%s,%s)",a)
    else:
      cursor.execute("update totalcal set(items=%s,cal=%s) where username=%s and day=%s",(a1[1]+','+a[1],int(a1[2])+int(a[2]),a[0],a[-1]))
  except:
    return []
def showbyday(a):
  try:
    cursor.execute("select * from totalcal where username = %s and day = %s",a)
    return cursor.fetchone()
  except:
    return []
def find(data):
  try:
    cursor = con.cursor(dictionary=True)
    cursor.execute("select * from logindata where username=%s and pas=%s",data)
    return cursor.fetchone()
  except :
    return None
# data=('Rohan','123')
# saveclient(data)
