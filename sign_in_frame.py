

import customtkinter as ctk
from PIL import ImageTk, Image
from tkinter import StringVar

from frames.giao_dien_film_frame import CinemaApp


def create_sign_in_frame(root):
    for widget in root.winfo_children():
        widget.destroy()

    sign_in_frame = ctk.CTkFrame(root, fg_color="transparent")
    sign_in_frame.pack(fill="both", expand=True)  # Đảm bảo frame hiển thị

    sign_in_canvas = ctk.CTkCanvas(sign_in_frame, width=1271, height=782,
                                   highlightthickness=0)
    sign_in_canvas.pack(fill="both", expand=True)

    bgsi_image = Image.open("D:\HuynhNgocNhuY_\KTLT\libs\SIBG.png")
    bgsi_image = bgsi_image.resize((1271, 782), Image.Resampling.LANCZOS)
    bgsi_photo = ImageTk.PhotoImage(bgsi_image)

    sign_in_canvas.image = bgsi_photo
    sign_in_canvas.create_image(0, 0, image=bgsi_photo, anchor="nw")

    card_frame = ctk.CTkFrame(sign_in_frame,
                              width=728,
                              height=525,
                              corner_radius=25,
                              fg_color=("#610503", "#610503"),  # Deep red color
                              border_width=5,
                              border_color="#382E13")  # Golden border

    card_frame.place(relx=0.5, rely=0.5, anchor="center")
    sign_in_label = ctk.CTkLabel(card_frame,
                                 text="SIGN IN",
                                 font=("Aleo", 48, "bold"),
                                 text_color="#ffffff")
    sign_in_label.pack(pady=(30, 20), )
    email_label = ctk.CTkLabel(card_frame, text="Email", font=("Georgia", 18), text_color="#ffffff", anchor="w")
    email_label.pack(padx=30, pady=(20, 5), anchor="w")
    email_entry = ctk.CTkEntry(card_frame, placeholder_text="username@gmail.com",
                               font=("Arial", 16), width=340, height=40, corner_radius=5,
                               fg_color="#ffffff", text_color="#333333", placeholder_text_color="#bfbfbf")
    email_entry.pack(padx=30, pady=(0, 15))

    password_label = ctk.CTkLabel(card_frame, text="Password", font=("Georgia", 18), text_color="#ffffff", anchor="w")
    password_label.pack(padx=30, pady=(0, 5), anchor="w")
    password_entry = ctk.CTkEntry(card_frame, placeholder_text="Password",
                                  font=("Arial", 16), width=340, height=40, corner_radius=5,
                                  fg_color="#ffffff", text_color="#333333",
                                  placeholder_text_color="#bfbfbf", show="*")
    password_entry.pack(padx=30, pady=(0, 25))

    sign_in_button = ctk.CTkButton(card_frame, text="Sign in",
                                   font=("Georgia", 18), width=340, height=45, corner_radius=5,
                                   fg_color="#6d3b47", hover_color="#5d2b37",
                                   text_color="#ffffff")
    sign_in_button.pack(padx=30, pady=(10, 30))

    def toggle_password_visibility(password_entry, show_var, eye_button):
        current_show = show_var.get()
        if current_show == "*":
            show_var.set("")
            password_entry.configure(show="")
            eye_button.configure(text="👁️")
        else:
            show_var.set("*")
            password_entry.configure(show="*")
            eye_button.configure(text="👁️‍🗨️")
        eye_button = ctk.CTkButton(password_entry,
                                   text="👁️‍🗨️",
                                   width=30,
                                   height=30,
                                   fg_color="transparent",
                                   hover_color="#dddddd",
                                   corner_radius=5,
                                   command=lambda: toggle_password_visibility(password_entry, show_var, eye_button))
        eye_button.place(relx=0.92, rely=0.5, anchor="center")


    def open_main_app(root):
        for widget in root.winfo_children():
            widget.destroy()

        cinema_frame = CinemaApp(root)
        cinema_frame.pack(fill="both", expand=True)

    sign_in_button.configure(command=lambda: open_main_app(root))

    return sign_in_frame
