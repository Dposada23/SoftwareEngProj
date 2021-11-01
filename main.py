from AddCourse import *
from DeleteCourse import *
from ViewCourseList import *

# Add your own database name and password here to reflect in the code
mypass = "Password1!"
mydatabase = "projdb"

con = pymysql.connect(host="127.0.0.1", user="root", password=mypass, database=mydatabase)
cur = con.cursor()

root = Tk()
root.title("My Course Management")
# open image file
bg = ImageTk.PhotoImage(file="zoom_bg (1).jpg")

# create canvas
canvas = Canvas(root, width=700, height=3500)
canvas.pack(fill=BOTH, expand=True)

# place the image inside canvas
canvas.create_image(0, 0, image=bg, anchor='nw')


# resize function for resizing the image
# with proper width and height of root window
def resize_bg(e):
    global bg, resized, bg2
    # open image to resize it
    bg = Image.open('zoom_bg (1).jpg')
    # resize the image with width and height of root
    resized = bg.resize((e.width, e.height), Image.ANTIALIAS)

    bg2 = ImageTk.PhotoImage(resized)
    canvas.create_image(0, 0, image=bg2, anchor='nw')


headingFrame1 = Frame(root, bg='white', bd=5)
headingFrame1.place(relx=0.2, rely=0.1, relwidth=0.6, relheight=0.16)

headingLabel = Label(headingFrame1, text="Welcome", bg='#4169E1', fg='#FFB800', font=('Helvetica', 20))
headingLabel.place(relx=0, rely=0, relwidth=1, relheight=1)

btn1 = Button(root, text="Add Courses", relief="solid", highlightthickness=4, borderwidth=2, bg='white', fg='#4169E1', font=('Helvetica', 12), command=addCourse)
btn1.place(relx=0.28, rely=0.4, relwidth=0.45, relheight=0.1)

btn2 = Button(root, text="Remove Courses", relief="solid", highlightthickness=4, borderwidth=2, bg='white', fg='#4169E1', font=('Helvetica', 12), command=delete)
btn2.place(relx=0.28, rely=0.52, relwidth=0.45, relheight=0.1)

btn3 = Button(root, text="View Courses List", relief="solid", borderwidth=2, bg='white', fg='#4169E1', font=('Helvetica', 12), command=View)
btn3.place(relx=0.28, rely=0.64, relwidth=0.45, relheight=0.1)

# bind resized function with root window
# root.bind("<Configure>", resize_bg)
root.mainloop()