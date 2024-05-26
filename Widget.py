# Create class widget that contains infomation about downloaded videos inside history frame
from customtkinter import *


class Widget:
    def __init__(self, master, video_name, progress_bar, pause_button):
        self.master = master
        self.video_name = video_name
        self.progress_bar = progress_bar
        self.pause_button = pause_button
        self.container = None  # Container for widget

    def add_history(self):
        self.container = CTkFrame(master=self.master, fg_color="#65B741")
        self.container.pack(expand=True, fill='both', padx=10, pady=10)

        label = CTkLabel(master=self.container, text=self.video_name)
        label.pack(expand=True, pady=1, padx=15, anchor='w')

        self.pause_button = CTkButton(master=self.container, text="Pause", height=55, command=self.pause_download,
                                      hover=True, width=40)
        # Use pack
        self.pause_button.pack(side='right', padx=10, pady=10)

        # Progress bar under label
        self.progress_bar = CTkProgressBar(master=self.container, width=421, height=10)
        self.progress_bar.pack(expand=True, fill='both', padx=10, pady=10)
        self.progress_bar.set(0)

    # Decorator for delete widget
    def delete_widget(self):
        self.container.destroy()

    def pause_download(self):
        pass
