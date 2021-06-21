from tabulate import tabulate
import mysql.connector
con=mysql.connector.connect(host="localhost",user="root",password="",database="studentmarks")
if con:
     print("mysql is connected")
else:
     print("error")
def insert(name,department,collage_id,mark1,mark2,mark3,mark4,mark5,total,average,grade):
     res=con.cursor()
     sql="insert into student(name,department,collage_id,mark1,mark2,mark3,mark4,mark5,total,average,grade) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
     student=(name,department,collage_id,mark1,mark2,mark3,mark4,mark5,total,average,grade)
     res.execute(sql,student)
     con.commit()
     print("Data Insert Success")
def update(name,department,collage_id,mark1,mark2,mark3,mark4,mark5,total,average,grade,id):
    res = con.cursor()
    sql = "update student set name=%s,department=%s,collage_id=%s,mark1=%s,mark2=%s,mark3=%s,mark4=%s,mark5=%s,total=%s,average=%s,grade=%s where id=%s"
    student = (name, department, collage_id, mark1, mark2, mark3, mark4, mark5, total, average, grade,id)
    res.execute(sql,student)
    con.commit()
    print("Data update Success")
def get():
    res = con.cursor()
    sql = "select id,name,department,collage_id,mark1,mark2,mark3,mark4,mark5,total,average,grade from student"
    res.execute(sql)
    result = res.fetchone()
    print(result)
def select():
    res = con.cursor()
    sql = "select id,name,department,collage_id,mark1,mark2,mark3,mark4,mark5,total,average,grade from student"
    res.execute(sql)
    result = res.fetchall()
    print(tabulate(result,headers=["id","name","department","collage_id","mark1","mark2","mark3","mark4","mark5","total","average","grade"]))
def delete(id):
    res = con.cursor()
    sql = "delete from student where id=%s"
    student = (id,)
    res.execute(sql, student)
    con.commit()
    print("data delete success")
while True:
     print("1.insert data")
     print("2.update data")
     print("3.get data")
     print("4.select data")
     print("5.delete data")
     print("6.exit")
     choice=(int(input("Enter your choice: ")))
     if choice == 1:
        name = input("Enter name= ")
        department = input("Enter department= ")
        collage_id = input("Enter collage_id= ")
        mark1 = int(input("Enter mark1= "))
        mark2 = int(input("Enter mark2= "))
        mark3 = int(input("Enter mark3= "))
        mark4 = int(input("Enter mark4= "))
        mark5 = int(input("Enter mark5= "))
        total = (mark1 + mark2 + mark3 + mark4 + mark5)
        average = total / 5
        print(total)
        print(average)
        if (average >= 80):
             grade = 'A'
             print('A')
        elif (average < 80) or (average >=60 ):
             grade = 'B'
             print('B')
        else:
             grade = 'C'
             print("C")
        insert(name, department, collage_id, mark1, mark2, mark3, mark4, mark5, total, average, grade)
     elif choice == 2:
          id =int(input("Enter id= "))
          name = input("Enter name= ")
          department = input("Enter department= ")
          collage_id = input("Enter collage_id= ")
          mark1 = int(input("Enter mark1= "))
          mark2 = int(input("Enter mark2= "))
          mark3 = int(input("Enter mark3= "))
          mark4 = int(input("Enter mark4= "))
          mark5 = int(input("Enter mark5= "))
          total = (mark1 + mark2 + mark3 + mark4 + mark5)
          average = total / 5
          print(total)
          print(average)
          if (average >= 80):
              grade = 'A'
              print('A')
          elif (average < 80) or (average >= 60):
              grade = 'B'
              print('B')
          else:
              grade = 'C'
              print("C")
          update(name, department, collage_id, mark1, mark2, mark3, mark4, mark5, total, average, grade, id)
     elif choice == 3:
          get()
     elif choice == 4:
          select()
     elif choice == 5:
          id =input("Enter the Id to delete:  ")
          delete(id)
     elif choice == 6:
          exit()
     else:
          print("invalid selection,try again!")
