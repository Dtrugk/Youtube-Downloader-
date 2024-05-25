import customtkinter
from customtkinter import *
from pytube import YouTube
from tkinter import filedialog, messagebox

set_appearance_mode("Dark")


def main():
    app = CTk()
    app.title("Doi ten project vao day")
    app.geometry("850x450")
    app.resizable(False, False)

    # Function to handle downloading with progress callback
    def download_video():
        youtube_link = entry_url.get()
        download_folder = entry_path.get()
        selected_resolution = cbb_resolution.get()

        if youtube_link and download_folder:
            try:
                # Update progress bar to 0% initially
                progress_bar.set(0)

                # Download video with progress callback
                get_video = YouTube(youtube_link, on_progress_callback=progress_callback)
                video_stream = get_video.streams.filter(res=selected_resolution, mime_type="video/mp4",
                                                        progressive=True).first()

                if video_stream:
                    video_stream.download(output_path=download_folder)
                    # Show success message
                    messagebox.showinfo("Thành công", f"Đã tải xuống và lưu tại\n{download_folder}")
                    progress_bar.set(0)
                else:
                    messagebox.showerror("Lỗi", "Không tìm thấy video với độ phân giải được chọn.")
            except Exception as e:
                # Show error message if download fails
                messagebox.showerror("Lỗi", f"Lỗi khi tải xuống video: {str(e)}")

        else:
            messagebox.showerror("Error", "Chưa nhập URL hoặc Saving path")

    def progress_callback(stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percentage = bytes_downloaded / total_size * 100
        progress_bar.set(percentage / 100)
        app.update_idletasks()  # Update the GUI

    def clear_entry():
        entry_url.delete(0, END)

    def browse_directory():
        download_directory = filedialog.askdirectory(initialdir="Đường dẫn thư mục của bạn", title="Lưu Video")
        entry_path.delete(0, END)
        entry_path.insert(0, download_directory)

    def pause_download():
        pass

    # Label container for history in scroll frame (contain names of downloaded videos, a progess bar and a pause button)
    def add_history():
        label_container = CTkFrame(master=scroll_frame, fg_color="#65B741")
        label_container.pack(expand=True, fill='both', padx=10, pady=10)

        label = CTkLabel(master=label_container, text="Video name")
        label.pack(expand=True, pady=1, padx=1)

        btn_pause = CTkButton(master=frame2, text="Pause", height=35, command=pause_download, hover=True, width=189)
        # Place using grid layout
        btn_pause.pack(expand=True, pady=1, padx=1)

    # Frame 1
    frame1 = CTkFrame(master=app, fg_color="#65B741")
    frame1.pack(expand=True, fill='both', side='left')

    # Create scroll frame in frame1 for history
    scroll_frame = customtkinter.CTkScrollableFrame(master=frame1, width=100, height=200)
    scroll_frame.pack(expand=True, fill='both', padx=10, pady=10)

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

    btn_download = CTkButton(master=frame2, text="Download", height=35, command=download_video, hover=True, width=225)
    btn_download.place(x=20, y=300)

    btn_pause = CTkButton(master=frame2, text="Pause", height=35, command=pause_download, hover=True, width=189)
    btn_pause.place(x=250, y=300)

    cbb_resolution = customtkinter.CTkComboBox(master=frame2, values=["1080p", "720p", "480p", "360p", "240p", "144p"],
                                               width=421)
    cbb_resolution.place(x=20, y=180)

    # Add progress bar
    progress_bar = customtkinter.CTkProgressBar(master=frame2, width=421)
    progress_bar.place(x=20, y=350)
    progress_bar.set(0)

    app.mainloop()


if __name__ == '__main__':
    main()
