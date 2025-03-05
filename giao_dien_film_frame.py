import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import customtkinter as ctk
from typing import Dict, List


class MovieCard(ctk.CTkFrame):
    def __init__(self, master, title: str, date: str, image_path: str, **kwargs):
        super().__init__(master, fg_color="transparent", **kwargs)

        self.container = ctk.CTkFrame(self, width=220, height=450,
                                      fg_color="white", corner_radius=30)
        self.container.pack(expand=True, fill="both")
        self.container.pack_propagate(False)

        try:
            img = Image.open(image_path) if os.path.exists(image_path) else \
                Image.new('RGB', (220, 450), color=(240, 240, 240))
            img = img.resize((220, 450), Image.LANCZOS)
            self.photo = ImageTk.PhotoImage(img)

            self.image_label = tk.Label(self.container, image=self.photo,
                                        bg=self.container.cget("fg_color"))
            self.image_label.place(relx=0.5, rely=0.5, anchor="center")

            if title or date:
                overlay = ctk.CTkFrame(self.container, corner_radius=0,
                                       fg_color="black", height=120)  # Đổi màu sang black
                overlay.place(relx=0.5, rely=1, anchor="s",
                              relwidth=1, relheight=0.3)  # Tăng chiều cao lên 0.3

                gradient_label = tk.Label(overlay, bg="#333333")  # Dùng màu tối thay vì trong suốt
                gradient_label.place(relx=0.5, rely=1, anchor="s",
                                     relwidth=1, relheight=1)

                gradient_label.lower()

                if title:
                    title_label = ctk.CTkLabel(overlay, text=title,
                                               text_color="white",
                                               font=("Arial", 18, "bold"))
                    title_label.place(relx=0.1, rely=0.3, anchor="w")

                if date:
                    date_label = ctk.CTkLabel(overlay, text=date,
                                              text_color="white",
                                              font=("Arial", 12))
                    date_label.place(relx=0.1, rely=0.7, anchor="w")

        except Exception as e:
            print(f"Error loading image: {e}")

class CinemaApp(ctk.CTkFrame):
    def __init__(self,master):
        super().__init__(master)



        self.bg_color = "#761213"  # Red background
        self.nav_color = "#C69E89"  # Beige/brown navigation bar
        self.accent_color = "#ffbb07"  # Yellow accent

        self.configure(fg_color=self.bg_color)

        self.main_container = ctk.CTkFrame(self, fg_color=self.bg_color,
                                           corner_radius=0)
        self.main_container.pack(fill="both", expand=True, padx=20, pady=20)

        self.create_navigation_bar()
        self.content_frame = ctk.CTkFrame(self.main_container, fg_color="transparent")
        self.content_frame.pack(fill="both", expand=True, pady=(20, 0))

        self.current_tab = "Film"
        self.show_film_tab()

    def create_navigation_bar(self):
        self.nav_frame = ctk.CTkFrame(self.main_container,
                                      fg_color=self.nav_color,
                                      corner_radius=40)
        self.nav_frame.pack(fill="x", ipady=15)

        logo_frame = ctk.CTkFrame(self.nav_frame, fg_color="transparent")
        logo_frame.pack(side="left", padx=30)

        logo_text = ctk.CTkLabel(logo_frame, text="cadty",
                                 font=("Arial", 28, "bold"),
                                 text_color="white")
        logo_text.pack(side="left")

        dot = ctk.CTkLabel(logo_frame, text=".",
                           font=("Arial", 28, "bold"),
                           text_color=self.accent_color)
        dot.pack(side="left")

        cinema_text = ctk.CTkLabel(logo_frame, text="CINEMA",
                                   font=("Arial", 10),
                                   text_color="white")
        cinema_text.place(x=12, y=38)

        tabs_frame = ctk.CTkFrame(self.nav_frame, fg_color="transparent")
        tabs_frame.pack(side="left", expand=True)

        tabs = ["Film", "Ticket", "Theatre", "Contact"]
        self.tab_buttons = {}

        for i, tab in enumerate(tabs):
            if tab == "Film":  # Active tab
                btn = ctk.CTkButton(tabs_frame, text=tab,
                                    fg_color="#d54d4d",
                                    hover_color="#c43c3c",
                                    corner_radius=20,
                                    text_color="white",
                                    width=100)
            else:
                btn = ctk.CTkButton(tabs_frame, text=tab,
                                    fg_color="transparent",
                                    hover_color="#d8b5a5",
                                    corner_radius=20,
                                    text_color="white",
                                    width=100)

            btn.pack(side="left", padx=10)
            btn.configure(command=lambda t=tab: self.switch_tab(t))
            self.tab_buttons[tab] = btn

        search_frame = ctk.CTkFrame(self.nav_frame, fg_color="transparent")
        search_frame.pack(side="right", padx=30)

        search_container = ctk.CTkFrame(search_frame,
                                        fg_color=("#EEEEEE", "#555555"),  # Light/dark mode colors
                                        corner_radius=20,
                                        height=40)
        search_container.pack(side="left", padx=(0, 20))
        search_container.pack_propagate(False)

        search_entry = ctk.CTkEntry(search_container,
                                    width=200,
                                    height=40,
                                    placeholder_text="Search...",
                                    fg_color="transparent",
                                    border_width=0,
                                    text_color="white",
                                    placeholder_text_color="white")
        search_entry.pack(side="left", padx=(15, 5), fill="both", expand=True)

        search_icon = ctk.CTkLabel(search_container, text="🔍", text_color=self.accent_color)
        search_icon.pack(side="right", padx=(0, 15))

        user_btn = ctk.CTkButton(search_frame,
                                 width=40,
                                 height=40,
                                 text="👤",
                                 fg_color=self.accent_color,
                                 hover_color="#e6a800",
                                 corner_radius=20)
        user_btn.pack(side="right")

    def switch_tab(self, tab_name):
        for tab, btn in self.tab_buttons.items():
            if tab == tab_name:
                btn.configure(fg_color="#d54d4d")
            else:
                btn.configure(fg_color="transparent")

        for widget in self.content_frame.winfo_children():
            widget.destroy()

        self.current_tab = tab_name
        if tab_name == "Film":
            self.show_film_tab()
        elif tab_name == "Ticket":
            self.show_ticket_tab()
        elif tab_name == "Theatre":
            self.show_theatre_tab()
        elif tab_name == "Contact":
            self.show_contact_tab()

    def show_film_tab(self):
        movies_frame = ctk.CTkFrame(self.content_frame, fg_color="transparent")
        movies_frame.pack(fill="both", expand=True, padx=20, pady=20)
        scroll_frame = ctk.CTkScrollableFrame(movies_frame, orientation="horizontal",
                                              fg_color="transparent", height=500)
        scroll_frame.pack(fill="both", expand=True)
        movies = [
            ("", "", r"D:/HuynhNgocNhuY_/KTLT/libs/phim_macarong(2).png"),
            ("MUOI", "KHỞI CHIẾU: 30.09.2022", r"D:/HuynhNgocNhuY_/KTLT/libs/phim_muoi.png"),
            ("CAPTAIN AMERICA", "14.02.2025", r"D:/HuynhNgocNhuY_/KTLT/libs/phim_america.png"),
            ("KẺ ĂN HỒN", "08.12.2023", r"D:/HuynhNgocNhuY_/KTLT/libs/phim_keanhon.png"),
            ("", "", r"D:/HuynhNgocNhuY_/KTLT/libs/phim_muoi.png")
        ]

        for title, date, image in movies:
            card = MovieCard(scroll_frame, title, date, image)
            card.pack(side="left", padx=10)

    def show_ticket_tab(self):
        label = ctk.CTkLabel(self.content_frame, text="vé  vủng",
                             font=("Arial", 24, "bold"), text_color="white")
        label.pack(expand=True)

    def show_theatre_tab(self):
        label = ctk.CTkLabel(self.content_frame, text="rạp",
                             font=("Arial", 24, "bold"), text_color="white")
        label.pack(expand=True)

    def show_contact_tab(self):
        label = ctk.CTkLabel(self.content_frame, text="thông tin ",
                             font=("Arial", 24, "bold"), text_color="white")
        label.pack(expand=True)


