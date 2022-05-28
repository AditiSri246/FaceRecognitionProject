from tkinter import *
import cv2
from tkinter import messagebox
import mysql.connector


def register():
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Aditi@246_Sri",
        database='register'
    )
    cur_obj = db.cursor()
    cur_obj.execute("INSERT INTO USER (First_Name, Last_Name, Aadhaar, Phone, Email, Age, Gender) VALUES (%s, %s, %s, %s, %s, %s, %s)",
                    (
                        firstnameValue.get(),
                        lastnameValue.get(),
                        aadhaarValue.get(),
                        phoneValue.get(),
                        emailValue.get(),
                        ageValue.get(),
                        genderValue.get()
                    )
                    )
    db.commit()
    messagebox.showinfo("Instruction", "Webcam will be opened now. Press Space Bar to click photo")
    cam = cv2.VideoCapture(0)
    count = 0
    user_name = firstnameValue.get()+"_"+lastnameValue.get()
    while count == 0:
        ret, frame = cam.read()
        if not ret:
            print("Failed To Open Webcam")
            break

        cv2.imshow("Take Image", frame)
        k = cv2.waitKey(1)
        # Press Escape To Close
        if k % 256 == 27:
            print("Escape Hit, Closing Webcam")
            break
        # Press Space To Capture Image
        elif k % 256 == 32:
            img_name = "images/{}.png".format(user_name)
            cv2.imwrite(img_name, frame)
            count = 1
    cam.release()
    cv2.destroyAllWindows()

    messagebox.showinfo("Registration Successful", "Registered Successfully")
    firstnameValue.set("")
    lastnameValue.set("")
    aadhaarValue.set("")
    phoneValue.set("")
    emailValue.set("")
    genderValue.set("Male")
    ageValue.set("")


def reset():
    firstnameValue.set("")
    lastnameValue.set("")
    aadhaarValue.set("")
    phoneValue.set("")
    emailValue.set("")
    genderValue.set("Male")
    ageValue.set("")


def close():
    root.destroy()


root = Tk()
root.title("Registration Form")
root.geometry("600x650+400+25")
root.resizable(0, 0)
root.iconbitmap('icon2.ico')
root.configure(bg="light cyan")

label1 = Label(root, text="Registration Form", font="Times 25 bold", bg="light cyan")
label1.place(x=150, y=20)
label2 = Label(root, text="First Name", font="Arial 15", bg="light cyan")
label2.place(x=100, y=150)
label3 = Label(root, text="Last Name", font="Arial 15", bg="light cyan")
label3.place(x=100, y=200)
label4 = Label(root, text="Aadhaar", font="Arial 15", bg="light cyan")
label4.place(x=100, y=250)
label5 = Label(root, text="Phone", font="Arial 15", bg="light cyan")
label5.place(x=100, y=300)
label6 = Label(root, text="Email", font="Arial 15", bg="light cyan")
label6.place(x=100, y=350)
label7 = Label(root, text="Age", font="Arial 15", bg="light cyan")
label7.place(x=100, y=400)
label8 = Label(root, text="Gender", font="Arial 15", bg="light cyan")
label8.place(x=100, y=450)

# Entry Variables

firstnameValue = StringVar()
lastnameValue = StringVar()
aadhaarValue = StringVar()
phoneValue = StringVar()
emailValue = StringVar()
genderValue = StringVar()
ageValue = StringVar()

# Entry Fields

firstnameEntry = Entry(root, textvariable=firstnameValue, width=25, bd=2, font=15)
firstnameEntry.place(x=250, y=150)
lastnameEntry = Entry(root, textvariable=lastnameValue, width=25, bd=2, font=15)
lastnameEntry.place(x=250, y=200)
aadhaarEntry = Entry(root, textvariable=aadhaarValue, width=25, bd=2, font=15)
aadhaarEntry.place(x=250, y=250)
phoneEntry = Entry(root, textvariable=phoneValue, width=25, bd=2, font=15)
phoneEntry.place(x=250, y=300)
emailEntry = Entry(root, textvariable=emailValue, width=25, bd=2, font=15)
emailEntry.place(x=250, y=350)
ageEntry = Entry(root, textvariable=ageValue, width=25, bd=2, font=15)
ageEntry.place(x=250, y=400)

# Radio Button

genderValue.set("Male")
rb1 = Radiobutton(root, text="Male", variable=genderValue, value="Male", bg="light cyan")
rb2 = Radiobutton(root, text="Female", variable=genderValue, value="Female", bg="light cyan")
rb1.place(x=250, y=450)
rb2.place(x=350, y=450)

# Buttons

registerButton = Button(root, text="Register", command=lambda: register(), font="Times 15", width=8, height=1, bg="#001833", fg="white")
registerButton.place(x=115, y=550)
resetButton = Button(root, text="Reset", command=lambda: reset(), font="Times 15", width=8, height=1, bg="#001833", fg="white")
resetButton.place(x=265, y=550)
closeButton = Button(root, text="Close", command=lambda: close(), font="Times 15", width=8, height=1, bg="#001833", fg="white")
closeButton.place(x=415, y=550)

root.mainloop()
