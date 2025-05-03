from diffusers import StableDiffusionPipeline
import torch

# Ensure CUDA is available
assert torch.cuda.is_available(), "CUDA (GPU) is not available!"

# Load the model to the GPU in float16 precision
pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16  # Keep FP16 to optimize memory usage on RTX 2050
).to("cuda")

# Read the lyrics from file
with open("assets/lyrics.txt", "r") as f:
    lines = [line.strip() for line in f.readlines() if line.strip()]

# Batch processing: Grouping lines for faster processing
batch_size = 4  # Adjust this to balance VRAM usage and speed
num_inference_steps = 25  # Reduce the number of inference steps for faster generation
guidance_scale = 7.5  # Adjust for a balance between quality and speed

# Generate and save images for each batch of lines
for i in range(0, len(lines), batch_size):
    batch_lines = lines[i:i + batch_size]
    prompts = [f"cinematic scene of: {line}" for line in batch_lines]

    # Generate images for the current batch
    images = pipe(prompts, num_inference_steps=num_inference_steps, guidance_scale=guidance_scale).images

    # Save images for each line in the batch
    for j, image in enumerate(images):
        image.save(f"images/frame_{i + j + 1:02d}.png")

print("Image generation completed.")
