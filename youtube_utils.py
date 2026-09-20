import os
from pathlib import Path

import yt_dlp

from config import settings


def ensure_dirs():
    Path(settings.audio_dir).mkdir(parents=True, exist_ok=True)
    Path(settings.output_dir).mkdir(parents=True, exist_ok=True)


def download_audio_from_youtube(url: str) -> str:
    """
    Downloads audio from a YouTube URL using yt-dlp.
    Returns path to the downloaded .m4a (or similar) file.
    """
    ensure_dirs()

    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": os.path.join(settings.audio_dir, "%(id)s.%(ext)s"),
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=True)
        # Sometimes the best audio is in a different extension; yt-dlp handles it.
        # We'll just find the file that was written.
        # For simplicity, assume the file path is in 'requested_downloads'.
        if "requested_downloads" in info and info["requested_downloads"]:
            file_path = info["requested_downloads"][0]["filepath"]
        else:
            # Fallback: search directory for newest file
            files = list(Path(settings.audio_dir).glob("*"))
            files.sort(key=lambda p: p.stat().st_mtime, reverse=True)
            file_path = str(files[0])

    return file_path