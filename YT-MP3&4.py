import yt_dlp

def download_video(url):
    try:
        ydl_opts = {
            'format': 'bestvideo+bestaudio/best',
            'outtmpl': 'downloads/videos/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Video downloaded successfully!")
    except Exception as e:
        print(f"Error downloading video: {e}")

def download_audio(url):
    try:
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
            'outtmpl': 'downloads/audio/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Audio downloaded successfully!")
    except Exception as e:
        print(f"Error downloading audio: {e}")

def main():
    url = input("Enter the URL of the video: ")
    print("1. Download Video - MP4")
    print("2. Download Audio - MP3")
    try:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            download_video(url)
        elif choice == 2:
            download_audio(url)
        else:
            print("Invalid choice")
    except ValueError:
        print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
