import customtkinter
from customtkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

set_appearance_mode("Dark")

### This for testing only. Main file is TestNewDesign.py

def main():
    app = CTk()
    app.title("Doi ten project vao day")
    app.geometry("750x450")

    # Function to handle downloading
    def download_video():
        youtube_link = entry_url.get()
        download_folder = entry_path.get()
        selected_resolution = cbb_resolution.get()
        print(selected_resolution)

        if youtube_link and download_folder:
            try:
                # Download video
                get_video = YouTube(youtube_link)
                # Filter streams based on the selected resolution
                if selected_resolution == "1080p":
                    video_stream = get_video.streams.get_highest_resolution()
                elif selected_resolution == "144p":
                    video_stream = get_video.streams.get_lowest_resolution()
                else:
                    video_stream = get_video.streams.filter(resolution=str(selected_resolution), mime_type="video/mp4",
                                                            progressive=True).first()

                if video_stream:
                    video_stream.download(download_folder)
                    # Show success message
                    messagebox.showinfo("Thành công", f"Đã tải xuống và lưu tại\n{download_folder}")
                else:
                    messagebox.showerror("Lỗi", "Không tìm thấy video với độ phân giải được chọn.")
            except Exception as e:
                # Show error message if download fails
                messagebox.showerror("Lỗi", f"Lỗi khi tải xuống video: {str(e)}")
        else:
            messagebox.showerror("Error", "Chưa nhập URL hoặc Saving path")

    def clear_entry():
        entry_url.delete(0, END)

    def browse_directory():
        download_directory = filedialog.askdirectory(initialdir="Đường dẫn thư mục của bạn", title="Lưu Video")
        entry_path.delete(0, END)
        entry_path.insert(0, download_directory)

    # Frame 1
    frame1 = CTkFrame(master=app, fg_color="#65B741")
    frame1.pack(expand=True, fill='both', side='left')

    label1 = CTkLabel(master=frame1, text="frame 1")
    label1.pack(expand=True, pady=1, padx=1)

    # Frame 2
    frame2 = CTkFrame(master=app)
    frame2.pack(expand=True, fill='both', side='right')

    label2 = CTkLabel(master=frame2, text="Youtube Downloader")
    label2.place(x=30, y=35)

    entry_url = CTkEntry(master=frame2, placeholder_text="Enter Youtube URL", width=420, height=55)
    entry_url.place(x=20, y=120)

    entry_path = CTkEntry(master=frame2, placeholder_text="Enter saving path", width=350, height=55)
    entry_path.place(x=20, y=220)

    btn_clear = CTkButton(master=frame2, text="Clear", height=45, width=30, command=clear_entry)
    btn_clear.place(x=394, y=124.5)

    btn_browse = CTkButton(master=frame2, text="Browse", height=55, width=30, command=browse_directory)
    btn_browse.place(x=382, y=219.75)

    btn_download = CTkButton(master=frame2, text="Download", height=35, command=download_video, hover=True)
    btn_download.place(x=20, y=300)

    cbb_resolution = customtkinter.CTkComboBox(master=frame2, values=["1080p", "720p", "480p", "360p", "240p", "144p"],
                                               width=421)
    cbb_resolution.place(x=20, y=180)

    app.mainloop()


if __name__ == '__main__':
    main()
