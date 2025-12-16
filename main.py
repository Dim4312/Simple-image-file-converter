import tkinter as tk
from tkinter import *
from tkinter import filedialog
from PIL import Image

im_in=""
im_out=""
patch = ""

w = Tk()
w.geometry("600x250")
w.title("Image converter 3000")
icon = PhotoImage(file="picture.png")
w.iconphoto(True, icon)

folder_icon = PhotoImage(file="folder(1).png")

OPTIONS = ["AVIF","BMP","GIF", "ICO","JPG","JPEG","PNG","TIFF","WEBP",]

FORMAT_MAP = {
    "AVIF": ".avif",
    "BMP": ".bmp",
    "GIF": ".gif",
    "ICO": ".ico",
    "JPG": ".jpg",
    "JPEG": ".jpeg",
    "PNG": ".png",
    "TIFF": ".tiff",
    "WEBP": ".webp",
}


def select_file():
    root = Tk()
    root.withdraw()


    file_path = filedialog.askopenfilename(
        title="Select a file",
        initialdir="/",
        filetypes=(("All files", "*.*"), ("Text files", "*.txt"))
    )

    root.destroy()
    return file_path

def set_patch():
    global patch
    patch = select_file()

def clen(text):
    char_to_find = '.'

    last_index = text.rfind(char_to_find)

    if last_index != -1:
        text = text[:last_index]
        return text
    else:
        return text

def image():
    global patch
    if patch.lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif', '.tiff', '.webp', '.ico', '.psd', '.eps', '.avif', '.ps', '.odd')):
        im = Image.open(patch)
        im.save(clen(patch)+FORMAT_MAP[im_out])
    else:
        print("Unsupported file format")

def show_selection():
    global im_in
    im_in = variable_in.get()
    print(im_in)

def show_selection_out():
    global im_out
    im_out = variable_out.get()
    print(im_out)

variable_in = tk.StringVar(w)
variable_in.set(OPTIONS[0])

variable_out = tk.StringVar(w)
variable_out.set(OPTIONS[0])

dropdown = tk.OptionMenu(w, variable_out, *OPTIONS)
dropdown.grid(column=0, row=2, padx="20")

button_out = tk.Button(w, text="Show Selection out", command=show_selection_out)
button_out.grid(column=1, row=2, padx=10)

inp = Button(w,
            image=folder_icon,
            bg="#ffb6c1",
            width="100",
            height="100",
            command=set_patch
            )
inp.grid(column=4, row=2, padx="20", pady="20")

cunt = Button(w,
              text="Convert",
              bg="white",
                width="10",
                height="5",
              command=image
              )
cunt.grid(column=5, row=2, padx="10",)

laib = Label(w, text="Image is going to be in the same directory \nas the original, if no error occurred, \nprobably unsupported format.")

laib.grid(column=1, row=3,)

w.config(bg="#ffb6c1")
w.mainloop()