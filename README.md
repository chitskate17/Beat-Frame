AI Music Video Generator
This project generates AI-driven music videos by transcribing lyrics from an audio file and generating synchronized images for each line using Stable Diffusion.

🚀 Features
✅ Transcribe audio (.mp3) to timestamped lyrics using [OpenAI Whisper]
✅ Generate images for each lyric line using [Stable Diffusion]
✅ Sync images and audio to create a dynamic, beat-matched music video
✅ GPU-accelerated (CUDA) support for faster processing on NVIDIA GPUs

📂 Folder Structure
bash
Copy
Edit
.
├── assets/
│   ├── song.mp3           # Your input song
│   ├── lyrics.txt         # Generated or provided lyrics
│   └── lyrics_segments.json  # Timestamps + lines from Whisper
├── generated_frames/      # Output images (one per lyric line)
├── output/                # Final rendered music video
├── transcribe_lyrics.py   # Script to extract lyrics + timestamps
├── generate_images.py     # Script to generate Stable Diffusion frames
├── create_video.py        # Script to assemble the final video
├── requirements.txt       # Python dependencies
└── README.md              # This file
🛠 Requirements
Python 3.8+

NVIDIA GPU (recommended for performance)

CUDA Toolkit (e.g., 12.8)

ffmpeg (must be added to system PATH)

📦 Installation
1️⃣ Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/ai-music-video-generator.git
cd ai-music-video-generator
2️⃣ Create and activate a virtual environment:

bash
Copy
Edit
python -m venv .venv
source .venv/bin/activate   # On Windows: .venv\Scripts\activate
3️⃣ Install dependencies (with GPU support):

bash
Copy
Edit
pip install -r requirements.txt
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
4️⃣ Install and set up ffmpeg:

Download from: https://www.gyan.dev/ffmpeg/builds/

Extract and add the bin folder to your system PATH.

🎵 Usage
1️⃣ Place your audio file:

Copy song.mp3 into the assets/ folder.

2️⃣ Transcribe lyrics:

bash
Copy
Edit
python transcribe_lyrics.py
This creates lyrics.txt and lyrics_segments.json in assets/.

3️⃣ Generate images for each lyric line:

bash
Copy
Edit
python generate_images.py
4️⃣ Create the final music video:

bash
Copy
Edit
python create_video.py
⚙️ Configuration
You can modify the prompts and visual style in generate_images.py to change the artistic output.

The create_video.py script uses ffmpeg to assemble images + audio; adjust settings there for resolution, FPS, or visual effects.

⚡ GPU Acceleration
Make sure:

torch.cuda.is_available() returns True

Both Whisper and Stable Diffusion models are moved to .to("cuda")
This will greatly speed up processing on machines with compatible GPUs.

📋 Example
Here’s what the workflow looks like:

Step	Output
Transcribe	Timestamped lyric JSON + text file
Generate Images	AI-generated frames per lyric line
Create Video	Final .mp4 synchronized video file

📜 License
MIT License

🙌 Acknowledgments
OpenAI Whisper

Hugging Face Diffusers

ffmpeg
