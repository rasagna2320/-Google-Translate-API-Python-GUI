from tkinter import *
from tkinter import ttk, messagebox
import googletrans
import textblob
from PIL import Image, ImageTk
from googletrans import Translator

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")
root.resizable(False,False)
root.configure(background = "white")

def label_change():
    c=combo1.get()
    c1=combo2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1)

def translate_now():
    global language
    try:
        translator = Translator()
        text_=text1.get(1.0,END).strip()
        c3=combo2.get()
        if not text_:
            messagebox.showerror("Error", "Input text cannot be empty")
            return
        words=textblob.TextBlob(text_)
        lan = translator.detect(text_).lang
        lan_ = None
        for i, j in language.items():
                if j.lower() == c3.lower():  # Case-insensitive match
                    lan_ = i
        if lan_ is None:
                messagebox.showerror("Error", "Language not recognized")
                return

        words=translator.translate(text_,src= lan, dest=lan_).text
        text2.delete(1.0,END)
        text2.insert(END,words)
    except Exception as e:
        print(f"Error: {e}")
        messagebox.showerror("googletrans","please try again")
        

# Load image icon with Pillow
img = Image.open("google_translator_pic.jpg")
# Convert the image to a format Tkinter can handle
img_tk = ImageTk.PhotoImage(img)
root.iconphoto(False,img_tk)

#arrow
# Open and load the image using Pillow
img = Image.open("arrow.png")
img = img.resize((130, 130), Image.LANCZOS)
arrow_image = ImageTk.PhotoImage(img)


image_label = Label(root, image = arrow_image,width = 150)
image_label.place(x=460,y=50)


language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

combo1 = ttk.Combobox(root,values=languageV,font = "Roboto 14",state = "r")
combo1.place(x=110,y=20)
combo1.set("ENGLISH")

label1 = Label(root,text="ENGLISH",font = "segoe 30 bold",bg = "white",width=18,bd=5,relief=GROOVE)
label1.place(x=10,y=50)


f = Frame(root,bg = "Black",bd = 5)
f.place(x=10,y=118,width=440,height=210)

text1 = Text(f,font = "Robote 20",bg = "white",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=430,height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side = "right",fill = "y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand = scrollbar1.set)


combo2 = ttk.Combobox(root,values=languageV,font = "RobotV 14",state="r")
combo2.place(x=730,y=20)
combo2.set("SELECT LANGUAGE")

label2 = Label(root,text="ENGLISH",font = "segoe 30 bold",bg = "white",width=18,bd=5,relief=GROOVE)
label2.place(x=620,y=50)

f1 = Frame(root,bg = "Black",bd = 5)
f1.place(x=620,y=118,width=440,height=210)

text2 = Text(f1,font = "Robote 20",bg = "white",relief=GROOVE,wrap=WORD)
text2.place(x=0,y=0,width=430,height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side = "right",fill = "y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand = scrollbar2.set)

#translate button
translate=Button(root,text="Translate",font="Roboto 15 bold italic",activebackground = "purple",cursor="hand2",bd=5,bg="red",fg="white",command=translate_now)
translate.place(x=480,y=250)

label_change()

root.configure(bg = "white")
root.mainloop()
