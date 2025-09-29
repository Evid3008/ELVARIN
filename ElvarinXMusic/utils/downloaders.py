import os
from yt_dlp import YoutubeDL

ydl_opts = {
    "format": "bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio[ext=opus]/bestaudio/best",
    "outtmpl": "downloads/%(id)s.%(ext)s",
    "geo_bypass": True,
    "nocheckcertificate": True,
    "quiet": True,
    "no_warnings": True,
    "prefer_ffmpeg": True,
    "extract_flat": False,
    "writethumbnail": False,
    "writeinfojson": False,
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "320",
        },
        {
            "key": "FFmpegAudioFilters",
            "preprocessor_args": [
                "-af", "bass=g=12:f=120,treble=g=6:f=12000,volume=1.2,highpass=f=15,lowpass=f=20000,acompressor=threshold=0.3:ratio=3:attack=5:release=50"
            ]
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
