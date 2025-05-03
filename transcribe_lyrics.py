import whisper
import json

# Paths
audio_path = "music/song.mp3"
lyrics_path = "assets/lyrics.txt"
segments_path = "assets/lyrics_segments.json"

# Load Whisper model
print("Loading Whisper model (base)...")
model = whisper.load_model("base").to("cuda")  # Switched to "base" for better memory efficiency

# Transcribe the song with optimized settings
print("Transcribing audio...")
result = model.transcribe(
    audio_path,
    fp16=True,                               # Use FP16 for reduced memory usage
    language="en",                           # Set language if known (auto-detect if not)
    beam_size=3,                             # Reduced beam size for less memory and faster results
    best_of=3,                               # Use the best of 3 decoding attempts (lower than 5 for efficiency)
    condition_on_previous_text=False,        # Avoids biasing based on earlier lines (better for songs)
    compression_ratio_threshold=2.4,         # Prevents hallucinated text (default is 2.4)
    logprob_threshold=-1.0,                  # Filter out very low-confidence segments
    no_speech_threshold=0.6                  # Skip silent segments confidently
)

# Save raw text (optional)
text = result["text"]

# Save cleaned lines
lines = []
segments = []

for segment in result["segments"]:
    start = segment["start"]
    end = segment["end"]
    line = segment["text"].strip().capitalize()
    if line:
        lines.append(line)
        segments.append({
            "start": start,
            "end": end,
            "text": line
        })

# Save lyrics as plain text
with open(lyrics_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))

# Save timestamped segments as JSON
with open(segments_path, "w", encoding="utf-8") as f:
    json.dump(segments, f, indent=2, ensure_ascii=False)

print(f"Transcribed {len(lines)} lines")
