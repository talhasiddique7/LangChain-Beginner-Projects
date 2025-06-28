# transcript_loader.py

from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

def extract_video_id(url: str) -> str:
    parsed_url = urlparse(url)
    if 'youtube' in parsed_url.netloc:
        return parse_qs(parsed_url.query).get("v", [""])[0]
    elif 'youtu.be' in parsed_url.netloc:
        return parsed_url.path.lstrip("/")
    else:
        raise ValueError("Invalid YouTube URL")

def get_video_transcript(video_url: str) -> str:
    video_id = extract_video_id(video_url)
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id)
    full_text = " ".join([t["text"] for t in transcript_list])
    return full_text
    