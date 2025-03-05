import tkinter as tk
from PIL import Image, ImageTk
from frames.sign_in_frame import create_sign_in_frame

def switch_to_sign_in():
    create_sign_in_frame(root)

root = tk.Tk()
root.title("Cadty Cinema")
root.geometry("1271x782")
root.resizable(False, False)

bg_image = Image.open("D:/HuynhNgocNhuY_/KTLT/libs/BG1.png")
bg_image = bg_image.resize((1271, 782), Image.Resampling.LANCZOS)
bg_photo = ImageTk.PhotoImage(bg_image)

logo_image = Image.open("D:/HuynhNgocNhuY_/KTLT/libs/ICON.png")
logo_image = logo_image.resize((538, 538), Image.Resampling.LANCZOS)
logo_photo = ImageTk.PhotoImage(logo_image)

canvas = tk.Canvas(root, width=1271, height=782, bg="#761214")
canvas.pack(fill="both", expand=True)
canvas.create_image(0, 0, image=bg_photo, anchor="nw")
canvas.create_image(635, 391, image=logo_photo, anchor="center")

root.after(1000, switch_to_sign_in)

root.mainloop()
