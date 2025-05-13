#All the required libraries are imported
from tkinter import *
from tkinter import filedialog,messagebox
from PIL import Image,ImageTk
import os
from stegano import lsb
#Function needs to be executed when open image button is clicked
def open_img():
    global var
    var = filedialog.askopenfilename(initialdir=os.getcwd(),
                                     title='Select File Type',
                                     filetypes=(('PNG','*.png'),('JPG','*.jpg'),
                                                ('JPEG','*.jpeg')))
    img = Image.open(var)
    if img.mode != 'RGB':
        img = img.convert('RGB')
    img.thumbnail((frame_width, frame_height)) 
    img = ImageTk.PhotoImage(img)
    lf1.configure(image=img)
    lf1.image = img
#Function needs to be executed when hide text button is clicked
def hide_text():
    global hide_msg
    pswd = code.get()
    msg = text1.get(1.0, END).strip()
    if msg == '':
        messagebox.showerror('ERROR', 'No text to hide')
        return
    if pswd == '':
        messagebox.showerror('ERROR','Please Enter Secret Key')
        return
    try:
        img = Image.open(var)
        if img.mode != 'RGB':
            img = img.convert('RGB')
            img.save("temp_rgb.png")  
            img_path = "temp_rgb.png"
        else:
            img_path = var
        msg += pswd
        msg += str(len(pswd))
        hide_msg = lsb.hide(img_path, msg)
        messagebox.showinfo("Success", "Message hidden successfully!")
    except NameError as e:
        messagebox.showerror('Error',"Please Select an Image")
    except Exception as e:
        messagebox.showerror("Error", "Failed to hide text")     
#Function needs to be executed when save image button is clicked
def save_img():
    try:
        hide_msg.save('Secret File.png')
        messagebox.showinfo("Saved", "Image saved successfully!")
        lf1.configure(image='')        
        lf1.image = None               
        text1.delete(1.0, END)     
        code.set('')              
    except:
        messagebox.showerror('Error','Please Hide Text First')
#Function needs to be executed when show data button is clicked   
def show_data():
    try:
        show_msg = lsb.reveal(var)
        print(show_msg)
        if show_msg is None:
            raise TypeError("No hidden message found.")

        n = int(show_msg[-1])
        show_msg = show_msg[:-1]
        pswd = show_msg[len(show_msg)-n:]
        show_msg = show_msg[:-n]
        print(pswd)
    except NameError:
        messagebox.showerror('Error', 'Please open an image first.')
        return
    except (TypeError, IndexError, ValueError):
        messagebox.showerror('Error', 'Image is invalid.')
        return

    pswd1 = code.get()
    if not pswd1:
        messagebox.showerror('Error', 'Please enter the secret key to reveal data.')
        return

    if pswd == pswd1:
        text1.delete(1.0, END)
        text1.insert(END, show_msg)
    else:
        messagebox.showerror('Error', 'Incorrect Secret Key')
#Creating a window for GUI
window = Tk()
window.geometry('700x600')
window.config(bg='black')
#Creating a Label
Label(window, text="Image Steganography", font='Impact 30 bold', bg='black', fg='red').place(x=190, y=20)
steps_text = (
    "How does it works?\n"
    "1. Open an Image\n"
    "2. Enter the Text to be Hidden\n"
    "3. Enter the Secret Key\n"
    "4. Click on \"Hide Text\"\n"
    "5. Click on \"Save Image\"\n"
    "6. Open Image with title \"Secret File\"\n"
    "7. Enter the Secret Key and Click \"Show Data\""
)
Label(window, text=steps_text, font='Arial 10', justify=LEFT, bg='black', fg='lightgreen').place(x=30, y=70)
#Creating a frame to show image thumbnail
frame_width = 250
frame_height = 220
frame_x_start = (700 - (frame_width * 2 + 30)) // 2  
f1 = Frame(window, width=frame_width, height=frame_height, bd=0, bg='white')
f1.place(x=frame_x_start, y=220)
lf1 = Label(f1, bg='white')
lf1.place(x=0, y=0)
#Creating a frame to enter text to be hidden
f2 = Frame(window, width=frame_width, height=frame_height, bd=0, bg='white')
f2.place(x=frame_x_start + frame_width + 30, y=220)
text1 = Text(f2,font='arial 15 bold',wrap=WORD)
text1.place(x=0,y=0,width=230,height=200)
# Creating a label "Enter Secret Key"
label_x = (700 - 150) // 2  
Label(window, text='Enter Secret Key', font='10', bg='black', fg='yellow').place(x=label_x, y=450)
# Creating an entry to enter Secret Code
entry_width = 200 
entry_x = (700 - entry_width) // 2
code = StringVar()
e = Entry(window, textvariable=code, bd=2, font='Impact 15 bold', show='*')
e.place(x=entry_x, y=480, width=entry_width)
# Aligned note below the entry field
Label(window, text='Secret key length must be between 1 to 9 characters',
      font='Arial 9 italic', bg='black', fg='lightgray').place(x=entry_x-50, y=510)
#Creating the necessary buttons 
button_width = 120
button_spacing = (700 - (button_width * 4)) // 5  
x1 = button_spacing  
x2 = x1 + button_width + button_spacing
x3 = x2 + button_width + button_spacing
x4 = x3 + button_width + button_spacing
open_button = Button(window, text='Open Image', bg='blue', fg='white', font='arial 12', cursor='hand2',command=open_img)
open_button.place(x=x1, y=547, width=button_width)
hide_button = Button(window, text='Hide Text', bg='red', fg='white', font='arial 12', cursor='hand2',command=hide_text)
hide_button.place(x=x2, y=547, width=button_width)
save_button = Button(window, text='Save Image', bg='green', fg='white', font='arial 12', cursor='hand2',command=save_img)
save_button.place(x=x3, y=547, width=button_width)
show_button = Button(window, text='Show Data', bg='orange', fg='white', font='arial 12', cursor='hand2',command=show_data)
show_button.place(x=x4, y=547, width=button_width)
mainloop()