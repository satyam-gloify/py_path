import requests
import torch
from PIL import Image
from transformers import MllamaForConditionalGeneration, AutoProcessor

model_id = "meta-llama/Llama-3.2-11B-Vision-Instruct"

model = MllamaForConditionalGeneration.from_pretrained(
    model_id,
    torch_dtype=torch.bfloat16,
    device_map="auto",
)
processor = AutoProcessor.from_pretrained(model_id)

url = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/0052a70beed5bf71b92610a43a52df6d286cd5f3/diffusers/rabbit.jpg"
image = Image.open(requests.get(url, stream=True).raw)

messages = [
    {"role": "user", "content": [
        {"type": "image"},
        {"type": "text", "text": "If I had to write a haiku for this one, it would be: "}
    ]}
]

# Tokenize the input text
input_text = processor.apply_chat_template(messages, add_generation_prompt=True)
inputs = processor(
    image,
    input_text,
    add_special_tokens=False,
    return_tensors="pt"
).to(model.device)

# Generate text
output = model.generate(**inputs, max_new_tokens=30)

# Decode the generated text
print(processor.decode(output[0]))








# # Load model directly
# from transformers import AutoProcessor, AutoModelForPreTraining

# processor = AutoProcessor.from_pretrained("meta-llama/Llama-3.2-11B-Vision-Instruct")
# model = AutoModelForPreTraining.from_pretrained("meta-llama/Llama-3.2-11B-Vision-Instruct")

# Tokenize the input text
prompt = "Tell me a story about a robot who dreams of becoming a chef."
inputs = processor(prompt, return_tensors="pt")


# Generate text
outputs = model.generate(inputs.input_ids, max_length=200, num_beams=4)
# Decode the generated text
generated_text = processor.decode(outputs[0], skip_special_tokens=True)

print(generated_text)

# from transformers import AutoModelForCausalLM, AutoTokenizer
# # Load model directly
# from transformers import AutoProcessor, AutoModelForPreTraining

# processor = AutoProcessor.from_pretrained("meta-llama/Llama-3.2-11B-Vision-Instruct")
# model = AutoModelForPreTraining.from_pretrained("meta-llama/Llama-3.2-11B-Vision-Instruct")
# Download the model
# model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-3.2-11B-Vision-instruct")

# Download the tokenizer
# tokenizer = AutoTokenizer.from_pretrained("meta-llama/Llama-3.2-11B-Vision-instruct")

# Tokenize the input text
prompt = "Tell me a story about a robot who dreams of becoming a chef."
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text
outputs = model.generate(inputs.input_ids, max_length=200, num_beams=4)

# Decode the generated text
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)