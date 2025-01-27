import os
import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
API_TOKEN = os.getenv("HG_TOKEN")  # Get Hugging Face token from GitHub Secrets
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Function to query the API
def query(prompt):
    response = requests.post(API_URL, headers=headers, json={"inputs": prompt})
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")

# Read prompts from environment variable
prompts = os.getenv("PROMPTS", "").split(";")
if not prompts or prompts == [""]:
    raise ValueError("No prompts provided!")

# Generate images for each prompt
for idx, prompt in enumerate(prompts, start=1):
    try:
        print(f"Generating image for prompt: {prompt}")
        image_bytes = query(prompt)

        # Load the image with PIL
        image = Image.open(io.BytesIO(image_bytes))

        # Define 16:9 aspect ratio dimensions
        width, height = 1600, 900
        image_resized = image.resize((width, height))

        # Save the resized image in the 'Images/' folder
        output_path = f"Images/generated_image_{idx}.png"
        image_resized.save(output_path)
        print(f"Image saved as '{output_path}' with size {width}x{height}")
    except Exception as e:
        print(f"Error generating image for prompt '{prompt}': {e}")
