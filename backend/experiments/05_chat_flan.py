import sys, time
from transformers import pipeline
prompt = "User: I have a sore throat and mild fever.\nAssistant: " if len(sys.argv)<2 else " ".join(sys.argv[1:])
name = "google/flan-t5-small"
gen = pipeline("text2text-generation", model=name)
print(gen(prompt, max_new_tokens=80)[0]["generated_text"])
