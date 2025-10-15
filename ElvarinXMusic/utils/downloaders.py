import os
from yt_dlp import YoutubeDL

ydl_opts = {
    "format": "bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,
    "extract_flat": False,
    "writethumbnail": False,
    "writeinfojson": False,
    "concurrent_fragment_downloads": 3,
    "http_chunk_size": 10485760,
    "retries": 3,
    "fragment_retries": 3,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "192",  # Reduced quality for faster processing
        }
    ],
}
ydl = YoutubeDL(ydl_opts)


def audio_dl(url: str) -> str:
    sin = ydl.extract_info(url, False)
    x_file = os.path.join("downloads", f"{sin['id']}.mp3")
    if os.path.exists(x_file):
        return x_file
    ydl.download([url])
    return x_file
