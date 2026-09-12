import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder


input_file = "data/dataset_processed.csv"  
try:
    df = pd.read_csv(input_file)
    print(f"Dataset loaded successfully from {input_file}")
    print("First few rows of the dataset:")
    print(df.head())  
except Exception as e:
    print(f"Error loading dataset: {e}")


df['symptoms_list'] = df['symptoms_list'].apply(lambda x: eval(x) if isinstance(x, str) else [])


print("\nFirst few symptoms lists:")
print(df['symptoms_list'].head())  


all_symptoms = set()


for symptom_list in df['symptoms_list']:
    symptoms = symptom_list  
    all_symptoms.update(symptoms)


SYMPTOM_VOCAB = sorted(list(all_symptoms))


symptom2idx = {symptom: idx for idx, symptom in enumerate(SYMPTOM_VOCAB)}


print("\nSymptom Vocabulary (first 20 symptoms):")
print(SYMPTOM_VOCAB[:20])  


def merge_subwords(symptom_list):
    merged_symptoms = []
    for symptom in symptom_list:
        if symptom.startswith("##"): 
            if merged_symptoms:  
                merged_symptoms[-1] += symptom[2:]  
        else:
            merged_symptoms.append(symptom)
    return merged_symptoms


def symptoms_to_vector(symptoms_list):
    symptoms_list = merge_subwords(symptoms_list)  
    vec = np.zeros(len(SYMPTOM_VOCAB))  
    
    
    symptoms_list = [symptom.lower() for symptom in symptoms_list]

    for symptom in symptoms_list:
        
        if symptom in symptom2idx:
            vec[symptom2idx[symptom]] = 1  
        else:
            
            for vocab_symptom in SYMPTOM_VOCAB:
                if vocab_symptom.lower() in symptom:
                    vec[symptom2idx[vocab_symptom]] = 1
                    break

    return vec


X = np.array([symptoms_to_vector(symptom_list) for symptom_list in df['symptoms_list']])


print("\nFirst 5 symptom vectors:")
print(X[:5])  


label_encoder = LabelEncoder()
y = label_encoder.fit_transform(df['disease_label'])


training_data = pd.DataFrame(X, columns=SYMPTOM_VOCAB)
training_data['disease_label'] = y


output_file = 'data/training_data.csv'
training_data.to_csv(output_file, index=False)

print(f"Training data saved as: {output_file}")
