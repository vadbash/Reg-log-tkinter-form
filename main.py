from tkinter import *
import mysql.connector

connection = mysql.connector.connect(host="localhost",
                                         database="lesson",
                                         user="user",
                                         password="user")
root = Tk()
Label(root, text = "Enter name: ").grid(row = 0, sticky = W)
Label(root, text = "Enter password: ").grid(row = 1, sticky = W)
Label(root, text = "Confirm password: ").grid(row = 2, sticky = W)

name = Entry(root)
password = Entry(root)
password2 = Entry(root)



name.grid(row = 0, column = 1)
password.grid(row = 1, column = 1)
password2.grid(row = 2, column = 1)
def getInput():

    lastname = name.get()
    lastpassword = password.get()
    lastpassword2 = password2.get()
    root.destroy()

    global params
    params = [lastname,lastpassword,lastpassword2]

Button(root, text = "Зберегти",command = getInput).grid(row = 5, sticky = W)

mainloop()
def audit():
    if params[0] == '':
        print("Zapownit vsi radki")
        exit()
    elif params[1] != params[2]:
        print("password ne zbigaetsa, try one more time")
        exit()
    elif params[1] == '':
        print("Zapownit vsi radki")
        exit()



def input(): 
    cursor = connection.cursor()
    cursor.execute("insert into customers(name, password) values(%s, %s)" ,(params[0], params[1]))
    print("Regestration are successful")
    connection.commit()
    cursor.execute("SELECT * FROM customers")
    data = cursor.fetchall()
    print(data)

audit()
input()

