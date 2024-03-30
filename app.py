from transformers import AutoModelForImageClassification, AutoFeatureExtractor
import torch
import torch.nn.functional as F
from PIL import Image
import gradio as gr

model_name = "model"
model = AutoModelForImageClassification.from_pretrained(model_name)
feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)

def classify_image(image):
    image = Image.fromarray(image.astype('uint8'), 'RGB')  # Convert image to PIL format
    inputs = feature_extractor(images=image, return_tensors="pt")
    with torch.no_grad():
        predictions = model(**inputs)
    probs = F.softmax(predictions.logits, dim=-1)
    top_probs, top_indices = probs.topk(5)
    top_probs = top_probs.tolist()[0]  # Assuming a batch size of 1
    top_indices = top_indices.tolist()[0]
    
    # Create a dictionary of {class_name: probability} without formatting as strings
    result = {model.config.id2label[index]: prob for index, prob in zip(top_indices, top_probs)}
    return result

sample_images = [
    "binturong_6.jpg",
    "desert cat_9.jpg",
    "h. hyaena_6.jpg",
    "namadapa squirrel_7.jpg",
    "Pallas cat_8.jpg",
    # Add as many samples as you want
]

iface = gr.Interface(fn=classify_image, 
                     inputs=gr.Image(), 
                     outputs=gr.Label(num_top_classes=5),
                     examples=sample_images,
                     title="Image Classification",
                     description="Upload an image and the model will predict the top 5 classes.")

if __name__ == "__main__":
    iface.launch()
