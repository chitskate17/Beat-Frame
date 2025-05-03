import librosa
import json
import numpy as np

y, sr = librosa.load("music/song.mp3")
tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
beat_times = librosa.frames_to_time(beats, sr=sr)

with open("assets/beat_times.json", "w") as f:
    json.dump(beat_times.tolist(), f)

if isinstance(tempo, (list, np.ndarray)):
    tempo_val = float(tempo[0])
else:
    tempo_val = float(tempo)
print(f"Tempo: {tempo_val:.2f} BPM")

print(f"Saved {len(beat_times)} beat timestamps.")
