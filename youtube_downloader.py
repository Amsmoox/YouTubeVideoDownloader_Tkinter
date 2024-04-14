#Ayoub Mharrech
import tkinter as tk
from tkinter import filedialog, messagebox  # Import necessary tkinter modules for GUI and dialogs
from pytube import YouTube  # Import YouTube from pytube for downloading YouTube videos

class YouTubeDownloader:
    def __init__(self, master):
        self.master = master  # Reference to the main window of the application
        self.master.title("YouTube Video Downloader")  # Set the title of the window
        self.master.geometry("500x200")  # Set the size of the window
        
        self.url_label = tk.Label(master, text="Enter YouTube URL:")  # Label to prompt user to enter URL
        self.url_label.pack()  # Pack the label into the master window
        
        self.url_entry = tk.Entry(master, width=50)  # Entry widget for user to input YouTube URL
        self.url_entry.pack()  # Pack the entry widget into the master window
        
        self.download_button = tk.Button(master, text="Download", command=self.download_video)  # Button to trigger download
        self.download_button.pack()  # Pack the button into the master window
        
        self.status_label = tk.Label(master, text="", fg="red")  # Label to show status messages
        self.status_label.pack()  # Pack the status label into the master window

    def download_video(self):
        url = self.url_entry.get()  # Get the URL from the entry widget
        save_path = filedialog.askdirectory()  # Open a dialog to ask user for a directory to save the video
        
        if not save_path:
            self.status_label.config(text="Download cancelled, no folder selected.")  # Update status if no folder selected
            return
        
        try:
            yt = YouTube(url)  # Create a YouTube object with the URL
            stream = yt.streams.get_highest_resolution()  # Get the highest resolution stream available
            stream.download(output_path=save_path)  # Download the video to the selected path
            self.status_label.config(text="Download completed successfully!", fg="green")  # Update status on success
        except Exception as e:
            self.status_label.config(text=f"Error: {str(e)}", fg="red")  # Update status on error

def main():
    root = tk.Tk()  # Create the main window
    app = YouTubeDownloader(root)  # Create an instance of YouTubeDownloader
    root.mainloop()  # Start the tkinter event loop

main() # Finally this will run the application

# This is Ayoub Mharrech's work, a software engineer.
# If you have any questions, feel free to contact me at email: mharrech.ayoub@gmail.com
# This script is designed for beginners.
