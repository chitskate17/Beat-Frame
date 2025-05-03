from diffusers import StableDiffusionPipeline
import torch
import gc
import os
from PIL import Image
from tqdm import tqdm
import psutil

# Ensure CUDA is available
assert torch.cuda.is_available(), "CUDA (GPU) is not available!"

# Reduce noise
os.environ["TRANSFORMERS_NO_ADVISORY_WARNINGS"] = "1"

# Load pipeline
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    use_safetensors=True,
    safety_checker=None
).to("cuda")

# VRAM optimizations
pipe.enable_attention_slicing()
pipe.enable_vae_slicing()

# Input/output
with open("assets/prompts.txt", "r", encoding="utf-8") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

output_dir = "images"
os.makedirs(output_dir, exist_ok=True)

# Configs
num_inference_steps = 20
guidance_scale = 7.5
image_height = 512
image_width = 512

# Log GPU memory
def log_gpu_memory(tag=""):
    allocated = torch.cuda.memory_allocated() / 1024**2
    reserved = torch.cuda.memory_reserved() / 1024**2
    print(f"[{tag}] GPU Memory - Allocated: {allocated:.2f} MB, Reserved: {reserved:.2f} MB")

# Generate images
for i, line in enumerate(tqdm(lines, desc="Generating images")):
    prompt = f"cinematic scene of: {line}"
    print(f"\n🖼 Generating {i + 1}/{len(lines)}: '{line}'")
    log_gpu_memory("Before")

    try:
        result = pipe(
            prompt,
            height=image_height,
            width=image_width,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale
        )
        image = result.images[0]
        image.save(os.path.join(output_dir, f"frame_{i + 1:02d}.png"))

    except Exception as e:
        print(f"❌ Error on line {i+1}: {e}")

    log_gpu_memory("After")

    # Cleanup
    torch.cuda.empty_cache()
    gc.collect()

print("\n✅ All images generated.")
