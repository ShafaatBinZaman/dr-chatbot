import sys, time
from transformers import pipeline
text = "Severe headache, nausea, and stiff neck since yesterday." if len(sys.argv)<2 else " ".join(sys.argv[1:])
name = "d4data/biomedical-ner-all"
t0=pipeline("token-classification", model=name, aggregation_strategy="simple")
print({"model":name,"loaded":True})
ents = t0(text)
print(ents)
