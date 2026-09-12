import sys, time
from transformers import AutoTokenizer, AutoModelForSequenceClassification, pipeline

text = "I have a headache and mild fever" if len(sys.argv)<2 else " ".join(sys.argv[1:])

name = "distilbert-base-multilingual-cased"
t0=time.perf_counter()
clf = pipeline("text-classification", model=name, top_k=None)
load_s = time.perf_counter()-t0

t1=time.perf_counter()
out = clf(text)
infer_s = time.perf_counter()-t1

print({"model":name, "load_s":round(load_s,2), "infer_s":round(infer_s,3), "out":out})
