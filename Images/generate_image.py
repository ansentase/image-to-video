import requests
import io
import os
from PIL import Image

# Define API details
API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
API_TOKEN = os.getenv("HG_TOKEN")  # Get the token from environment variable
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Function to query the API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        return response.content
    else:
        raise Exception(f"API call failed with status code {response.status_code}: {response.text}")

try:
    # Query the API for the image
    image_bytes = query({
        "inputs": "future city",
    })

    # Load the image with PIL
    image = Image.open(io.BytesIO(image_bytes))

    # Define 16:9 aspect ratio dimensions, e.g., 1600x900
    width = 1600
    height = 900
    image_resized = image.resize((width, height))

    # Save the resized image in the 'Images/' folder
    output_path = "Images/generated_image_16x9.png"
    image_resized.save(output_path)  # Save as PNG format
    print(f"Image saved as '{output_path}' with size {width}x{height}")
except Exception as e:
    print(f"Error: {e}")
