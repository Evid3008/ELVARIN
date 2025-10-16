import os
from yt_dlp import YoutubeDL

ydl_opts = {
    "format": "bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,
    "extract_flat": False,
    "writethumbnail": False,
    "writeinfojson": False,
    "extractor_retries": 3,
    "fragment_retries": 5,
    "skip_unavailable_fragments": True,
    "http_headers": {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    },
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        }
    ],
}
ydl = YoutubeDL(ydl_opts)


def audio_dl(url: str) -> str:
    try:
        sin = ydl.extract_info(url, False)
        if not sin:
            raise Exception("Failed to extract video info")
        
        x_file = os.path.join("downloads", f"{sin['id']}.mp3")
        if os.path.exists(x_file):
            return x_file
        
        ydl.download([url])
        return x_file
    except Exception as e:
        print(f"Audio download error: {e}")
        raise e
