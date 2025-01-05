import pandas as pd
import numpy as np
import mysql.connector
import datetime
import tkinter as tk
import sqlalchemy as sq


 
from tkinter import *
import os
 
# Designing window for registration
 
def register():
    global register_screen
    register_screen = Toplevel(main_screen)
    register_screen.title("Register")
    register_screen.geometry("300x250")
 
    global username
    global password
    global username_entry
    global password_entry
    username = StringVar()
    password = StringVar()
 
    Label(register_screen, text="Please enter details below", bg="blue").pack()
    Label(register_screen, text="").pack()
    username_lable = Label(register_screen, text="Username * ")
    username_lable.pack()
    username_entry = Entry(register_screen, textvariable=username)
    username_entry.pack()
    password_lable = Label(register_screen, text="Password * ")
    password_lable.pack()
    password_entry = Entry(register_screen, textvariable=password, show='*')
    password_entry.pack()
    Label(register_screen, text="").pack()
    Button(register_screen, text="Register", width=10, height=1, bg="blue", command = register_user).pack()
 
 
# Designing window for login 
 
def login():
    global login_screen
    login_screen = Toplevel(main_screen)
    login_screen.title("Login")
    login_screen.geometry("300x250")
    Label(login_screen, text="Please enter details below to login").pack()
    Label(login_screen, text="").pack()
 
    global username_verify
    global password_verify
 
    username_verify = StringVar()
    password_verify = StringVar()
 
    global username_login_entry
    global password_login_entry
 
    Label(login_screen, text="Username * ").pack()
    username_login_entry = Entry(login_screen, textvariable=username_verify)
    username_login_entry.pack()
    Label(login_screen, text="").pack()
    Label(login_screen, text="Password * ").pack()
    password_login_entry = Entry(login_screen, textvariable=password_verify, show= '*')
    password_login_entry.pack()
    Label(login_screen, text="").pack()
    Button(login_screen, text="Login", width=10, height=1, command = login_verify).pack()
 
# Implementing event on register button
 
def register_user():
 
    username_info = username.get()
    password_info = password.get()
 
    file = open(username_info, "w")
    file.write(username_info + "\n")
    file.write(password_info)
    file.close()
 
    username_entry.delete(0, END)
    password_entry.delete(0, END)
 
    Label(register_screen, text="Registration Success", fg="green", font=("calibri", 11)).pack()
 
# Implementing event on login button 
 
def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()
    username_login_entry.delete(0, END)
    password_login_entry.delete(0, END)
 
    list_of_files = os.listdir()
    if username1 in list_of_files:
        file1 = open(username1, "r")
        verify = file1.read().splitlines()
        if password1 in verify:
            login_sucess()
 
        else:
            password_not_recognised()
 
    else:
        user_not_found()
 
# Designing popup for login success
 
def login_sucess():
    global login_success_screen
    login_success_screen = Toplevel(login_screen)
    login_success_screen.title("Success")
    login_success_screen.geometry("150x100")
    Label(login_success_screen, text="Login Success").pack()
    Button(login_success_screen, text="OK", command=delete_login_success).pack()
 
# Designing popup for login invalid password
 
def password_not_recognised():
    global password_not_recog_screen
    password_not_recog_screen = Toplevel(login_screen)
    password_not_recog_screen.title("Success")
    password_not_recog_screen.geometry("150x100")
    Label(password_not_recog_screen, text="Invalid Password ").pack()
    Button(password_not_recog_screen, text="OK", command=delete_password_not_recognised).pack()
 
# Designing popup for user not found
 
def user_not_found():
    global user_not_found_screen
    user_not_found_screen = Toplevel(login_screen)
    user_not_found_screen.title("Success")
    user_not_found_screen.geometry("150x100")
    Label(user_not_found_screen, text="User Not Found").pack()
    Button(user_not_found_screen, text="OK", command=delete_user_not_found_screen).pack()
 
# Deleting popups
 
def delete_login_success():
    login_success_screen.destroy()
 
 
def delete_password_not_recognised():
    password_not_recog_screen.destroy()
 
 
def delete_user_not_found_screen():
    user_not_found_screen.destroy()
 
 
# Designing Main(first) window
 
def main_account_screen():
    global main_screen
    main_screen = Tk()
    main_screen.geometry("300x250")
    main_screen.title("Account Login")
    Label(text="Select Your Choice", bg="blue", width="300", height="2", font=("Calibri", 13)).pack()
    Label(text="").pack()
    Button(text="Login", height="2", width="30", command = login).pack()
    Label(text="").pack()
    Button(text="Register", height="2", width="30", command=register).pack()

    main_screen.mainloop()
main_account_screen()
###################################
def dataframe():
    con=sq.create_engine("mysql+mysqlconnector://root:shu@localhost/test")
    df=pd.read_sql("tick",con)
    print(df)
def cancellation():
    dataframe()
    db1=mysql.connector.connect(host="localhost",user="root",password="password",database="test")
    cursor=db1.cursor()
    s=str(input("Enter your name for cancellation : "))
    sql="DELETE FROM tick WHERE Name ='%s'"%(s)
    try:
        cursor.execute(sql)
        print("<<<<<<<<<<<CANCELLATION COMPLETED>>>>>>>>>>>")
        db1.commit()
    except:
        db1.rollback()
        db1.close()


def reservation():
    print('\t\t\t  <<<<<<<<<RESERVATION>>>>>>>>>>>\t\t\t\t')
    df =pd.read_excel("C:\\Users\\HP\\Downloads\\new railway data.xlsx")
    pd.set_option("display.max_rows",1000)
    pd.set_option("display.max_columns",1000)
    pd.set_option("display.width",1000)
    df.set_index("sl_No",inplace=True)
    print(df)
    print("\n1.REGISTRATION ")
    print("\n2.CANCELLATION")
    print("\n3.BACK TO MAINMENU")
    ch=int(input("\t\nEnter your Choice: "))
    if ch==1:
        registration()
    elif ch==2:
        cancellation()
    elif ch==3:
        program()
    else:
        print("!!!!!!!!!!!!WRONG ENTRY!!!!!!!!!!!!!!!!!")



def registration():
    now=datetime.datetime.now()
    con=sq.create_engine("mysql+mysqlconnector://root:shu@localhost/test")
    a=int(input("\nEnter Train no: "))
    b=str(input("\nEnter your Name: "))
    c=int(input("\nEnter your Age: "))
    print("Write in the form of M-Male and F-Female")
    d=str(input("\nEnter your Gender: "))
    e=now.strftime("%Y-%m-%d")
    df=pd.DataFrame({"Train_no":[a],"Name":[b],"Age":[c],"Gender":[d],"Registration_date":[e]},index=[1])
    df1=df.set_index("Train_no")
    print(df1)
    df1.to_sql("tick",con,if_exists="append",index=True)
    print("\n\t{{{{{{{{{{{{{{{{{{{ REGISTRATION COMPLETED}}}}}}}}}}}}}}}}}}}}}")

    
def retustrainno():
    df =pd.read_excel("C:\\Users\\HP\\Downloads\\new railway data.xlsx")
    df.set_index("sl_No",inplace=True)
    print("\nEnter the train number whose details you want see")
    x=int(input("\nEnter the number : "))
    print(df.loc[df.Train_No==x])

def retustrainname():
     df =pd.read_excel("C:\\Users\\HP\\Downloads\\new railway data.xlsx")
     pd.set_option("display.max_rows",1000)
     pd.set_option("display.max_columns",1000)
     pd.set_option("display.width",1000)
     df.set_index("sl_No",inplace=True)
     print("\nEnter the train name whose details you want see")
     x=(input("\nEnter the name :"))
     print(df.loc[df.Train_Name==x])
     
     
def retusorgin():
    df=pd.read_excel("C:\\Users\\HP\\Downloads\\new railway data.xlsx")
    pd.set_option("display.max_rows",1000)
    pd.set_option("display.max_columns",1000)
    pd.set_option("display.width",1000)
    df.set_index("sl_No",inplace=True)

    x=(input("\nEnter the origin:"))
    print(df.loc[df.Origin==x] )

def retusdest():
    df=pd.read_excel("C:\\Users\\HP\\Downloads\\new railway data.xlsx")
    pd.set_option("display.max_rows",1000)
    pd.set_option("display.max_columns",1000)
    pd.set_option("display.width",1000)
    df.set_index("sl_No",inplace=True)
    

    y=(input("\nEnter the Destination: "))
    print(df.loc[df.Destination==y] )
   
    
def schedule():
    print('\t\t\t   <<<<<<<<<---Schedule--->>>>>>>>')

    df =pd.read_excel("C:\\Users\\HP\\Downloads\\new railway data.xlsx")
    pd.set_option("display.max_rows",1000)
    pd.set_option("display.max_columns",1000)
    pd.set_option("display.width",1000)
    df.set_index("sl_No",inplace=True)
    print(df)
    print("***********************************************************************")
    print("\n1.Retrive train details using train number")
    print("\n2.Retrive train details using train name")
    print("\n3.Retrive train details using Starting point")
    print("\n4.Retrive train details using Destination")
    print("\n5.Back to mainmenu")
    print("\n*********************************************************************")
    option=int(input("\nEnter the your option : "))
    if option==1:
               retustrainno()
    elif option==2:
        retustrainname()
    elif option==3:
        retusorgin()
    elif option==4:
        retusdest()
    elif option==5:
        program()
    else:
        df.close()


def program():    
    print("\n<<<<<<<<<<<<WELCOME TO RAILWAY RESERVATION>>>>>>>>>>>>>>>>>")

    
    print('\t\n1.RESEVERVATION' )
    print('\n2.SCHEDULE')


    choice=int(input("\t\nEnter your choice :"))
    if choice==1:
        reservation()
    elif choice==2:
        schedule()
    else:
        print(df)

#main_account_screen()
program()

                   
