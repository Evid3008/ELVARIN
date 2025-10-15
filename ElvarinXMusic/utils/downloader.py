from os import path
import yt_dlp
from yt_dlp.utils import DownloadError

ytdl = yt_dlp.YoutubeDL(
    {
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "format": "bestaudio[ext=m4a]",
        "geo_bypass": True,
        "nocheckcertificate": True,
    }
)


def download(url: str, my_hook) -> str:
    ydl_optssx = {
        "format": "bestaudio[ext=m4a]/bestaudio[ext=webm]/bestaudio/best",
        "outtmpl": "downloads/%(id)s.%(ext)s",
        "geo_bypass": True,
        "nocheckcertificate": True,
        "quiet": True,
        "no_warnings": True,
        "concurrent_fragment_downloads": 5,
        "http_chunk_size": 20971520,
        "retries": 5,
        "fragment_retries": 5,
        "socket_timeout": 30,
        "extractor_retries": 3,
        "skip_unavailable_fragments": True,
        "http_headers": {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    }
    try:
        info = ytdl.extract_info(url, False)
        if not info:
            raise Exception("Failed to extract video info")
        
        x = yt_dlp.YoutubeDL(ydl_optssx)
        x.add_progress_hook(my_hook)
        dloader = x.download([url])
        
        xyz = path.join("downloads", f"{info['id']}.{info['ext']}")
        return xyz
    except Exception as y_e:
        print(f"Download error: {y_e}")
        raise y_e
