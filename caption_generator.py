from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import random

# Load model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

funny_endings = [
    "…because calories don’t count today 😜",
    "vibes too strong 💥",
    "caption game = strong 💅",
    "just your daily dose of wow ✨",
    "can you even handle this?! 🔥",
    "this goes straight to the gram 📸",
    "serving looks and pixels 🤳",
    "I came. I saw. I captioned. 🎯"
]

def generate_caption(image_path):
    image = Image.open(image_path).convert('RGB')
    inputs = processor(images=image, return_tensors="pt")
    output = model.generate(**inputs)
    caption = processor.decode(output[0], skip_special_tokens=True)
    caption += " " + random.choice(funny_endings)
    return caption
