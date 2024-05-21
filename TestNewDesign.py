import customtkinter
from customtkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

set_appearance_mode("Dark")


def main():
    app = CTk()
    app.title(string="Doi ten project vao day")
    app.geometry("750x450")

    # Function to handle downloading
    def download_video():
        youtube_link = entry_url.get()
        download_folder = entry_path.get()

        if youtube_link != "" and download_folder != "":
            try:
                # Download video
                get_video = YouTube(youtube_link)
                # Progress Bar maybe ?
                video_stream = get_video.streams.first()
                video_stream.download(download_folder)

                # Show success message
                messagebox.showinfo("Thành công", f"Đã tải xuống và lưu tại\n{download_folder}")
            except Exception as e:
                # Show error message if download fails
                messagebox.showerror("Lỗi", f"Lỗi khi tải xuống video: {str(e)}")
        else:
            messagebox.showinfo("Error", f"Chưa nhập URL hoặc Saving path")

    def Clear():
        while entry_url.get() != "":
            entry_url.delete(first_index=0)

    # Frame 1 ------------------------------------------------
    # Tự thiet ke them vao day
    frame1 = CTkFrame(master=app, fg_color="#65B741")
    frame1.pack(expand=True, fill='both', side='left')

    label1 = CTkLabel(master=frame1, text="frame 1")
    label1.pack(expand=True, pady=1, padx=1)

    # Frame 2 -------------------------------------------------
    # T cha nghi them duoc function gi
    frame2 = CTkFrame(master=app)
    frame2.pack(expand=True, fill='both', side='right')

    label2 = CTkLabel(master=frame2, text="Youtube Downloader")
    label2.place(x=30, y=35)

    entry_url = CTkEntry(master=frame2, placeholder_text="Enter Youtube URL", width=420, height=55)
    entry_url.place(x=20, y=150)

    entry_path = CTkEntry(master=frame2, placeholder_text="Enter saving path", width=350, height=55)
    entry_path.place(x=20, y=220)

    btn_clear = CTkButton(master=frame2, text="Clear", height=45, width=30, command=lambda: Clear())
    btn_clear.place(x=394, y=154.5)

    btn_browse = CTkButton(master=frame2, text="Browse", height=55, width=30, command=lambda: Browse(entry_path))
    btn_browse.place(x=382, y=219.75)

    btn_download = CTkButton(master=frame2, text="Download", height=35, command=download_video, hover=True)
    btn_download.place(x=20, y=300)

    app.mainloop()


def Browse(entry_path):
    download_directory = filedialog.askdirectory(initialdir="Đường dẫn thư mục của bạn", title="Lưu Video")
    entry_path.insert(index=0, string=download_directory)


if __name__ == '__main__':
    main()
