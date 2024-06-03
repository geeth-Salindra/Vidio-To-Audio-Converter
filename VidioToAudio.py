import tkinter as tk
from tkinter import filedialog, messagebox
import os
from moviepy.editor import VideoFileClip

class VideoToAudioConverterApp:
    def __init__(self, master):
        self.master = master
        master.title("VideoToAudio Converter")
        master.resizable(False, False)

        window_width = 400
        window_height = 200
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        x_coordinate = (screen_width - window_width) // 2
        y_coordinate = (screen_height - window_height) // 2

        master.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

        self.menu_bar = tk.Menu(master)
        master.config(menu=self.menu_bar)

        self.title_label = tk.Label(master, text="VideoToAudio Converter", font=("Helvetica", 16, "bold"))
        self.title_label.pack(pady=10)

        self.input_label = tk.Label(master, text="Select Video File (.mp4, .mkv):")
        self.input_label.pack()

        self.input_path_entry = tk.Entry(master, width=50)
        self.input_path_entry.pack()

        self.browse_input_button = tk.Button(master, text="Browse", command=self.browse_video)
        self.browse_input_button.pack()

        self.output_label = tk.Label(master, text="Select Output Directory:")
        self.output_label.pack()

        self.output_directory_entry = tk.Entry(master, width=50)
        self.output_directory_entry.pack()

        self.browse_output_button = tk.Button(master, text="Browse", command=self.browse_output_directory)
        self.browse_output_button.pack()

        self.convert_button = tk.Button(master, text="Convert to .MP3", command=self.convert_to_mp3)
        self.convert_button.pack()

    def browse_video(self):
        file_path = filedialog.askopenfilename(filetypes=[("Video files", "*.mp4;*.mkv")])
        self.input_path_entry.delete(0, tk.END)
        self.input_path_entry.insert(0, file_path)

    def browse_output_directory(self):
        output_directory = filedialog.askdirectory()
        self.output_directory_entry.delete(0, tk.END)
        self.output_directory_entry.insert(0, output_directory)

    def convert_to_mp3(self):
        video_path = self.input_path_entry.get()
        output_directory = self.output_directory_entry.get()

        if not video_path or (not video_path.endswith(".mp4") and not video_path.endswith(".mkv")):
            messagebox.showerror("Error", "Please select a valid MP4 or MKV video file.")
            return

        if not output_directory:
            messagebox.showerror("Error", "Please select an output directory.")
            return

        try:
            # Generate output file name based on the video file's name
            output_file_path = os.path.join(output_directory, os.path.splitext(os.path.basename(video_path))[0] + ".mp3")

            # Convert video to audio using moviepy
            video_clip = VideoFileClip(video_path)
            audio_clip = video_clip.audio
            audio_clip.write_audiofile(output_file_path)

            messagebox.showinfo("Conversion Complete", f"Audio file saved at: {os.path.abspath(output_file_path)}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during conversion: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = VideoToAudioConverterApp(root)
    root.mainloop()
