import sqlite3
def create_DB():
    con=sqlite3.connect(database="rms.db")
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS course(cid INTEGER PRIMARY KEY AUTOINCREMENT,name text,semister text,year text,description text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS student(roll INTEGER PRIMARY KEY AUTOINCREMENT,name text,email text,gender text,dob text,contact text,admission text,course text,state text,city text,pin text,address text)")
    con.commit()
    
    cur.execute("CREATE TABLE IF NOT EXISTS result(rid INTEGER PRIMARY KEY AUTOINCREMENT,roll text,name text,course text,marks_ob text,full_marks text,per text)")
    con.commit()

    cur.execute("CREATE TABLE IF NOT EXISTS employee(did INTEGER PRIMARY KEY AUTOINCREMENT,f_name text,l_name text,email text,contact text,question text,answer text,password text)")
    con.commit()

    con.close()

create_DB()