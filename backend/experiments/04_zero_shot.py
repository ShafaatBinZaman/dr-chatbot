import sys, time
from transformers import pipeline
text = "High fever, joint pain, and rash" if len(sys.argv)<2 else " ".join(sys.argv[1:])
labels = ["dengue","influenza","gastritis","migraine","covid-19","pneumonia"]

name = "facebook/bart-large-mnli"  # heavy; swap later if slow
clf = pipeline("zero-shot-classification", model=name)
res = clf(text, candidate_labels=labels, multi_label=True)
print({"top": list(zip(res['labels'][:3], [round(s,3) for s in res['scores'][:3]]))})
