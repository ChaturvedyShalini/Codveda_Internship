
import yt_dlp

# Video URL
video_url = "https://youtu.be/LvC68w9JS4Y?si=sawpvoG7lx-qBCJP"

# Output filename (optional)
output_path = "ML_Course.mp4"

# yt-dlp options
ydl_opts = {
    'format': 'bestvideo[height=1080]+bestaudio/best',
    'merge_output_format': 'mp4',  # Ensure final file is MP4
    'outtmpl': output_path,  # Save file as ML_Course.mp4
}

# Download video
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([video_url])

print("Download completed!")
