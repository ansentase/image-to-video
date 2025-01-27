import requests
import io
from PIL import Image

API_URL = "https://api-inference.huggingface.co/models/black-forest-labs/FLUX.1-dev"
headers = {"Authorization": "Bearer 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"}

# Function to query the API
def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    return response.content

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
image_resized.save("Images/generated_image_16x9.png")  # Save as PNG format
print(f"Image saved as 'Images/generated_image_16x9.png' with size {width}x{height}")
