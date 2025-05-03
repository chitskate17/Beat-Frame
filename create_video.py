import json
import os
from pathlib import Path
from moviepy import AudioFileClip, CompositeVideoClip, ImageClip

# === Load audio ===
audio_path = "music/song.mp3"
audio_clip = AudioFileClip(audio_path)
audio_duration = audio_clip.duration

# === Load lyrics segments with timestamps ===
with open("assets/lyrics_segments.json") as f:
    segments = json.load(f)

# === Load available image frames ===
image_folder = "images"
image_files = sorted([f for f in os.listdir(image_folder) if f.endswith(".png")])

if not image_files:
    raise RuntimeError("No images found in 'images/' folder.")

# === Create image clips based on segment timings ===
clips = []
num_images = len(image_files)

for i, segment in enumerate(segments):
    start = segment["start"]
    end = segment["end"]
    duration = end - start

    image_path = os.path.join(image_folder, image_files[i % num_images])
    img = ImageClip(image_path).with_start(start).with_duration(duration)
    clips.append(img)

# === Composite video with image overlays ===
video = CompositeVideoClip(clips, size=(512, 512)).with_duration(audio_duration)

# === Add audio and export ===
video = video.with_audio(audio_clip)

# Ensure output folder exists
Path("video").mkdir(exist_ok=True)

# Export video
video.write_videofile("video/final_music_video.mp4", fps=24)
