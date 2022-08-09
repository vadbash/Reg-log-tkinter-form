from tkinter import *
import mysql.connector

connection = mysql.connector.connect(host="localhost",
                                         database="lesson",
                                         user="user",
                                         password="user")
root = Tk()
Label(root, text = "Enter name: ").grid(row = 0, sticky = W)
Label(root, text = "Enter password: ").grid(row = 1, sticky = W)

name = Entry(root)
password = Entry(root)



name.grid(row = 0, column = 1)
password.grid(row = 1, column = 1)
def getInput():

    lastname = name.get()
    lastpassword = password.get()
    root.destroy()

    global params
    params = [lastname,lastpassword]

Button(root, text = "Зберегти",command = getInput).grid(row = 5, sticky = W)


mainloop()
def audit():
    if params[0] == '':
        print("Zapownit vsi radki")
        exit()
    if params[1] == '':
        print("Zapownit vsi radki")
        exit()

def input():
    cursor = connection.cursor()
    cursor.execute("select name, password from customers where name = %s and password = %s" ,(params[0], params[1]))
    if not cursor.fetchone():
            print("You don't have an account, or password is incorrect")
            exit()
    else:
            print("Login successful, HI")
    connection.commit()
    cursor.execute("SELECT * FROM customers")
    data = cursor.fetchall()
    cursor.close()
    print(data)

audit()
input()