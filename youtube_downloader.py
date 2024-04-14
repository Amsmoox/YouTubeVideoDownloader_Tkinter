#Ayoub Mharrech
import tkinter as tk
from tkinter import filedialog, messagebox
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, master):
        self.master = master
        self.master.title("YouTube Video Downloader")
        self.master.geometry("500x200")
        
        self.url_label = tk.Label(master, text="Enter YouTube URL:")
        self.url_label.pack()
        
        self.url_entry = tk.Entry(master, width=50)
        self.url_entry.pack()
        
        self.download_button = tk.Button(master, text="Download", command=self.download_video)
        self.download_button.pack()
        
        self.status_label = tk.Label(master, text="", fg="red")
        self.status_label.pack()

    def download_video(self):
        url = self.url_entry.get()
        save_path = filedialog.askdirectory()
        
        if not save_path:
            self.status_label.config(text="Download cancelled, no folder selected.")
            return
        
        try:
            yt = YouTube(url)
            stream = yt.streams.get_highest_resolution()
            stream.download(output_path=save_path)
            self.status_label.config(text="Download completed successfully!", fg="green")
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg="red")

def main():
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()

main()
