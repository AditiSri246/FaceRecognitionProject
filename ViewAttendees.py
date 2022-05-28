import mysql.connector
from tkinter import *
from tkinter import ttk

root = Tk()
root.title("Attendees")
root.resizable(0, 0)
root.geometry(f"500x550+400+25")
root.iconbitmap('icon3.ico')
root.configure(bg="light cyan")

label = Label(root, text="Attendees", font="Times 20 bold", bg="light cyan")
label.place(x=180, y=20)

# Adding Style
style = ttk.Style()

# Theme
style.theme_use('clam')

#  Configure Treeview
style.configure("Treeview", background="#D3D3D3", foreground="black", rowheight=20, fieldbackround="silver")

# Change Selected Colour
style.map('Treeview', background=[('selected', 'black')])

tree = ttk.Treeview(root, columns=("Name", "Time", "Date"), show='headings', height=20)
tree.column("# 1", anchor=CENTER, width=150)
tree.heading("# 1", text="Name")
tree.column("# 2", anchor=CENTER, width=150)
tree.heading("# 2", text="Time")
tree.column("# 3", anchor=CENTER, width=150)
tree.heading("# 3", text="Date")
tree.place(x=22, y=80)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Aditi@246_Sri",
    database='attendance'
)
cur_obj = db.cursor()
query_extract = "SELECT Name,Time,Date FROM ATTENDEES"
cur_obj.execute(query_extract)
l_name = cur_obj.fetchall()

for row in l_name:
    tree.insert('', 'end', text="1", value=row)

root.mainloop()
