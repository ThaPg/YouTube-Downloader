# importing packages
from pytube import YouTube
import os

# Where to save
SAVE_PATH = "Downloaded\mp3"

links = [
    "https://www.youtube.com/watch?v=-Er2djXB_6s",
    "https://www.youtube.com/watch?v=jA8Qfbidf38",
]

for link in links:

    try:
        # Object creation using YouTube which was imported in the beginning
        yt = YouTube(link)
    except:
        # Handle exception
        print("Connection Error")

    # extract only audio
    audio = yt.streams.filter(only_audio=True).first()

    try:
        # download the audio file
        out_file = audio.download(output_path=SAVE_PATH)
        # save the file
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        print("Audio downloaded successfully!")
    except:
        print("Some Error!")

print("Task Completed!")
