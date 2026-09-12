import pandas as pd
from transformers import pipeline
from tqdm import tqdm


input_file = "data/dataset.csv"         
output_file = "data/dataset_processed.csv"  

print(f"Loading dataset from {input_file}...")
df = pd.read_csv(input_file)


print("Loading Biomedical NER model...")
ner = pipeline(
    "ner",
    model="d4data/biomedical-ner-all",
    aggregation_strategy="simple"
)


def extract_symptoms(text):
    try:
        entities = ner(text)
        symptoms = []

        for ent in entities:
            word = ent.get("word", "").lower().strip()

            
            if word.startswith("##"):
                if symptoms:
                    symptoms[-1] += word[2:]  
            else:
                symptoms.append(word)

        
        seen = set()
        unique_symptoms = []
        for s in symptoms:
            if s not in seen:
                seen.add(s)
                unique_symptoms.append(s)

        return unique_symptoms

    except Exception as e:
        print(f" Error processing text: {text}")
        print("Reason:", e)
        return []


print("\n Debugging NER for first dataset sentence:")
test_text = df['user_text'].iloc[0]
print(" Input text:", test_text)
print(" NER output:", ner(test_text))
print("\n")


print("Extracting symptoms using NER...\n")
tqdm.pandas()  
df['symptoms_list'] = df['user_text'].progress_apply(extract_symptoms)


df.to_csv(output_file, index=False)
print("\n Processing complete!")
print(f" New dataset saved as: {output_file}\n")

print(df.head())
