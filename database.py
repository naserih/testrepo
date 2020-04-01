import psycopg2
import env


database_name = env.PG_DATABASE
user_name = env.PG_USER
password = env.PG_PASSWORD
host = env.PG_HOST
port = env.PG_PORT

con = psycopg2.connect(database=database_name, user=user_name, password=password, host=host, port=port)

print("Database opened successfully")

cur = con.cursor()

cur.execute('''CREATE TABLE PATIENT
      (PATIENTID INT PRIMARY KEY     NOT NULL,
      NAME           TEXT    NOT NULL,
      AGE            INT     NOT NULL,
      WEIGHT        INT,
      TREATMENT        CHAR(1));''')

con.commit()
print("Table created successfully")

patients_list = [
        [1, 'A', 38, 68, 'x'],
        [2, 'C', 52, 87, 'x'],
        [3, 'G', 87, 75, 'y'],
        [4, 'D', 32, 60, 'z'],
        [5, 'L', 15, 91, 'x'],
        [6, 'J', 32, 93, 'y'],
        [7, 'P', 45, 78, 'z'],
        [8, 'I', 32, 87, 'z'],
        [9, 'E', 79, 54, 'y'],
        [10, 'N', 31, 43, 'y'],
        [11, 'B', 90, 79, 'x'],
        [12, 'M', 22, 90, 'y'],
        [13, 'O', 15, 86, 'z'],
        [14, 'F', 8, 72, 'z'],
        [15, 'K', 63, 73, 'x']
]
for row in patients_list:
    print (row)
    cur.execute("INSERT INTO PATIENT (PATIENTID,NAME,AGE,WEIGHT,TREATMENT) VALUES (%i, '%s', %i, %i, '%s')"%(row[0],row[1],row[2], row[3], row[4]))
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'John', 18, 'Computer Science', 'ICT')")
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')")
# cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')")

# print("Record inserted successfully")


# con.commit()

# cur.execute("SELECT admission, name, age, course, department from STUDENT")
# cur.execute("SELECT name, age, department from STUDENT WHERE ADMISSION = 3421")
# cur.execute("SELECT name, age, department from STUDENT WHERE NAME = 'John' ")
# cur.execute("SELECT name, age, department from STUDENT WHERE DEPARTMENT = 'ICT       ' ")
# cur.execute("SELECT name, age, department from STUDENT WHERE DEPARTMENT = 'ICT       ' OR NAME='Antony'")
cur.execute("SELECT NAME, WEIGHT from PATIENT")
rows = cur.fetchall()

for row in rows:
    print (row)


# cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3420")
# con.commit()


# cur.execute("DELETE from STUDENT where ADMISSION=3420;")
# con.commit()

con.close()
