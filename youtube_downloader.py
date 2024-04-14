#Ayoub Mharrech
import tkinter as tk
# Import necessary tkinter modules for GUI and dialogs
from tkinter import filedialog, messagebox 
# Import YouTube from pytube for downloading YouTube videos
from pytube import YouTube

class YouTubeDownloader:
    def __init__(self, master):
        self.master = master  # Reference to the main window of the application
        self.master.title("YouTube Video Downloader")  # Set the title of the window
        self.master.geometry("500x200")  # Set the size of the window
        
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

# This is Ayoub Mharrech's work, a software engineer.
# If you have any questions, feel free to contact me at email: mharrech.ayoub@gmail.com
# This script is designed for beginners.
