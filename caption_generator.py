from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import random

# Load BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

# Style templates for Instagram captions
style_templates = [
    "📸 {caption} #InstaVibes",
    "✨ Just wow — {caption} 💫",
    "Feeling it: {caption} 😍 #AestheticGoals",
    "When life gives you moments like this... {caption} 💕",
    "Unfiltered magic: {caption} 🌈 #DreamyVibes",
    "{caption} ❤️ #CapturedWithLove",
    "Serving looks with this vibe: {caption} 🔥",
    "Mood: {caption} 🌟 #WeekendGoals"
]

def generate_caption(image_file):
    image = Image.open(image_file).convert('RGB')
    inputs = processor(images=image, return_tensors="pt")
    output = model.generate(**inputs, num_return_sequences=1, do_sample=True, top_k=50)
    caption = processor.decode(output[0], skip_special_tokens=True)

    # Make it Instagram-style
    styled_caption = random.choice(style_templates).format(caption=caption.capitalize())
    return styled_caption
