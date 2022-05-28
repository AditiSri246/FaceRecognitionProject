import tkinter as tk
import os
from PIL import Image, ImageTk


def run():
    os.system('FaceRecognitionSystem.py')   # Face Recognition
    att_rec = tk.Label(root, text="Attendance Recorded", font="Times 15 bold")
    att_rec.place(x=600, y=490)


def register_here():
    os.system('RegistrationForm.py')   # Registration Form


def view_users():
    os.system('View.py')     # View Registered Users


def close():
    root.destroy()     # Exit App


def view():
    os.system('ViewAttendees.py')      # View Attendees


root = tk.Tk()
root.title("Face Recognition Based Entry System")
root.resizable(0, 0)
root.geometry("1366x693+0+0")
root.iconbitmap('icon1.ico')

ins = tk.Label(root, text="Face Recognition Based Entry System", font="Times 25 bold")
ins.place(x=420, y=30)

pic = Image.open('Pic.png')
pic = ImageTk.PhotoImage(pic)
pic_label = tk.Label(image=pic)
pic_label.image = pic
pic_label.place(x=410, y=150)

run_button = tk.Button(root, text="Mark Attendance", command=lambda: run(), font="Times", bg="#00254D", bd=2, relief="solid", fg="white", height=3, width=17)
run_button.place(x=600, y=550)

view_button = tk.Button(root, text="View Attendees", command=lambda: view(), font="Times", bg="#00254D", bd=2, relief="solid", fg="white", height=3, width=17)
view_button.place(x=850, y=550)

register_button = tk.Button(root, text="Register Here", command=lambda: register_here(), font="Times", bg="#00254D", bd=2, relief="solid", fg="white", height=3, width=17)
register_button.place(x=100, y=550)

show_users_button = tk.Button(root, text="View Registered Users", command=lambda: view_users(), font="Times", bg="#00254D", bd=2, relief="solid", fg="white", height=3, width=17)
show_users_button.place(x=350, y=550)

exit_button = tk.Button(root, text="Exit", command=lambda: close(), font="Times", bg="#00254D", bd=2, relief="solid", fg="white", height=3, width=17)
exit_button.place(x=1100, y=550)

root.mainloop()
