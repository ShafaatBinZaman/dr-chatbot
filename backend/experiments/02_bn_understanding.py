import sys, time
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

text = "আমার মাথাব্যথা এবং জ্বর আছে" if len(sys.argv)<2 else " ".join(sys.argv[1:])
name = "sagorsarker/bangla-bert-base"

t0=time.perf_counter()
tok = AutoTokenizer.from_pretrained(name)
mdl = AutoModelForSequenceClassification.from_pretrained(name)
pipe = pipeline("text-classification", model=mdl, tokenizer=tok)
print({"model":name, "loaded":round(time.perf_counter()-t0,2)})

print(pipe(text))
