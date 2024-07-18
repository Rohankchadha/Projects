import mysql.connector

Info=mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    db="to_do"
)
cursor=Info.cursor()

def login(data):
    try:
        cursor.execute("SELECT * from register WHERE email = %s and password = %s",data)
        return cursor.fetchone()
    except:
        return False

def addUser(data):
    try:
        print(data)
        cursor.execute("INSERT INTO register (name, gender, contact_number, email, password) VALUES (%s,%s,%s,%s,%s)",data)
        Info.commit()
        return True
    except:
        return False

def addtask(data):
    try:
        print(data)
        cursor.execute("INSERT INTO task (user_id,task_name, description, start_date, end_date, Importance) VALUES (%s,%s,%s,%s,%s,%s)",data)
        Info.commit()
        return True
    except:
        return False

def view_tasks(arg):
    try:
        # print(data)
        cursor.execute(" SELECT * FROM task where user_id=%s",arg)
        # info_data.commit()
        return cursor.fetchall()
    except:
        return False

def deleteTask(data):
    try:
        print("del",data)
        cursor.execute(" Delete FROM task WHERE id = %s",data)
        Info.commit()
        return True
    except:
        return False


def editTask(data):
    try:
        print("editfloor",data)
        cursor.execute(" SELECT * FROM task WHERE id = %s",data)
        return cursor.fetchone()
    except:
        return False


def update_task(data):  

    try:
        cursor.execute(" UPDATE task SET task_name  =%s, description =%s,start_date =%s, end_date =%s,Importance  =%s WHERE id = %s",data)
        Info.commit()
        return True
    except:
        return False

def singleSearch(data):
    try:
        cursor.execute(" SELECT * FROM task WHERE user_id = %s and Importance=%s",data)
        return cursor.fetchall()
    except:
        return False


def view_today(data):
    try:
        cursor.execute(" SELECT * FROM task WHERE user_id = %s and start_date =%s",data)
        return cursor.fetchall()
    except:
        return False

def view_completed(data):
    try:
        cursor.execute(" SELECT * FROM task WHERE user_id = %s and start_date =%s and Status ='Completed'",data)
        return cursor.fetchall()
    except:
        return False

def view_pending(data):
    try:
        cursor.execute(" SELECT * FROM task WHERE user_id = %s and start_date =%s and Status ='Pending'",data)
        return cursor.fetchall()
    except:
        return False

def updateStatus(taskId):
    try:
        cursor.execute('UPDATE task SET Status = "Completed" WHERE ID = %s', (taskId, ))
        Info.commit()
        return True
    except:
        return False