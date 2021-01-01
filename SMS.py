from tkinter import *
from tkinter import ttk, messagebox
import pymysql

class student():

    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1370x700+0+0")
        #This is for tittle
        title = Label(self.root, text="Student Management System", bd=9, relief=GROOVE, font=("times new roman", 50, "bold"), bg="pink", fg="red")
        title.pack(side=TOP, fill=X)

        #AlL Variables
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.search_by = StringVar()
        self.search_txt = StringVar()




        #Manage frame
        Manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        Manage_frame.place(x=20, y=100, width=450, height=585)

        m_title = Label(Manage_frame, text="Manage Student", bg="yellow", fg="black", font=("times new roman", 40, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_frame, text="Roll No", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")
        txt_Roll = Entry(Manage_frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_frame, text="Name", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_frame, text="Email", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_email = Entry(Manage_frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_frame, text="Gender", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_frame, textvariable=self.gender_var, font=("times new roman", 15, "bold"),state="readonly")
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20,)

        lbl_contact = Label(Manage_frame, text="Contact", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_contact = Entry(Manage_frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_frame, text="D.O.B", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_dob = Entry(Manage_frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_frame, text='Address', bg='blue', fg='white', font=('times new roman', 20, 'bold'))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky='w')
        self.txt_address = Text(Manage_frame, width=30, height=3, font=('times new roman', 10, 'bold'), bd=5, relief=GROOVE)
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky='w')

        #Manage Button##

        btn_frame = Frame(Manage_frame, bd=3, relief=RIDGE, bg='black')
        btn_frame.place(x=10, y=525, width=420)


        Addbtn = Button(btn_frame,text="Add",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn = Button(btn_frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10, pady=10)
        deletebtn = Button(btn_frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10, pady=10)
        clearbtn = Button(btn_frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)

        ####Details frame#######
        Details_frame = Frame(self.root, bd=4, relief=RIDGE, bg="blue")
        Details_frame.place(x=500, y=100, width=800, height=585)

        lbl_search = Label(Details_frame, text="Search By", bg="blue", fg="white", font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, padx=10, pady=20)

        combo_search = ttk.Combobox(Details_frame, textvariable=self.search_by, font=("times new roman", 15, "bold"), width=10, state="readonly")
        combo_search['values'] = ("Roll_No", "Name", "Address")
        combo_search.grid(row=0, column=1, pady=10, padx=20, )

        txt_search = Entry(Details_frame, textvariable=self.search_txt, font=("times new roman", 15, "bold"), width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky='w')

        searchbtn = Button(Details_frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showallbtn = Button(Details_frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        ####Table frame#######
        Table_frame = Frame(Details_frame, bd=4, relief=RIDGE, bg="crimson")
        Table_frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)

        self.Student_table = ttk.Treeview(Table_frame, column=("roll", "Name", "Email", "Gender", "Contact", "dob", "Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table. heading("roll", text="Roll No.")
        self.Student_table.heading("Name", text="Name")
        self.Student_table.heading("Email", text="Email")
        self.Student_table.heading("Gender", text="Gender")
        self.Student_table.heading("Contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")

        self.Student_table['show'] = 'headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("Name", width=100)
        self.Student_table.column("Email", width=100)
        self.Student_table.column("Gender", width=100)
        self.Student_table.column("Contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("Address", width=150)

        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()


        ######Codding for Database with connected database SQL#####

    def add_students(self):
        if self.Roll_No_var.get()=="" or self.name_var.get()=="":
            messagebox.showerror("Error", "All fields are required to fill")
        else:
           con = pymysql.connect(host="localhost", user="root", password="santoshsql@100", database="sms")
           cur = con.cursor()
           cur.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                            self.name_var.get(),
                                                                            self.email_var.get(),
                                                                            self.gender_var.get(),
                                                                            self.contact_var.get(),
                                                                            self.dob_var.get(),
                                                                            self.txt_address.get('1.0', END)
                                                                            ))
           con.commit()
           self.fetch_data()
           self.clear()
           con.close()
           messagebox.showinfo("success", "Record has been inserted")
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="santoshsql@100", database="sms")
        cur = con.cursor()
        cur.execute("select * from student")
        rows = cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
            con.commit()
        con.close()

    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete(1.0, END)
        self.txt_address.insert(END, row[6])


    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0", END)

    def update_data(self):
        con = pymysql.connect(host="localhost", user="root", password="santoshsql@100", database="sms")
        cur = con.cursor()
        cur.execute("update student set name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s where roll_no=%s",(
                                                                    self.name_var.get(),
                                                                    self.email_var.get(),
                                                                    self.gender_var.get(),
                                                                    self.contact_var.get(),
                                                                    self.dob_var.get(),
                                                                    self.txt_address.get('1.0', END),
                                                                    self.Roll_No_var.get()
                                                                     ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("success", "Record has been updated")

    def delete_data(self):
        con = pymysql.connect(host="localhost", user="root", password="santoshsql@100", database="sms")
        cur = con.cursor()
        cur.execute("delete from student where roll_no=%s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="santoshsql@100", database="sms")
        cur = con.cursor()
        cur.execute("select * from student where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
            con.commit()
        con.close()

class Student():
    pass
    root = Tk()
    obj = student(root)
    root.mainloop()

